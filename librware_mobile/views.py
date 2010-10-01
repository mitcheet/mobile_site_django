from librware.librware_mobile.models import *
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import urllib2
from xml.dom import minidom

# Create your views here.
def index(request):
	libraryList = Library.objects.all()
	#libraryList = get_object_or_404(Library)
	return render_to_response('librware_mobile/index.html', {'libraryList':libraryList}, context_instance=RequestContext(request))	
	#return HttpResponse("hello!")
def feed(request, feed_id):
	feed = get_object_or_404(Feed, pk=feed_id)	
	feedContents = urllib2.urlopen(feed.feedURI)
	return HttpResponse(feedContents, 'application/xml')
def detail(request, library_id):
	library = get_object_or_404(Library, pk=library_id)
	dom = minidom.parse(urllib2.urlopen(library.defaultFeed))
	title = dom.getElementsByTagName("title")[1].firstChild.data
	link =  dom.getElementsByTagName("link")[1].firstChild.data
	news = { 'title': title, 'link': link }	
#	return HttpResponse(news.toxml())
	return render_to_response('librware_mobile/detail.html', {'library':library, 'news':news}, context_instance=RequestContext(request))		
def search(request):
#, search_terms):
	search_terms = request.GET['lookfor']
	searchURL = 'http://cloud.lib.wfu.edu/vufind/Search/Results?type=AllFields&submit=Find&api=json&lookfor=' + search_terms 
	#search = get_object_or_404(request, searchURL)
	searchContents = urllib2.urlopen(searchURL)
	#return HttpResponse(searchURL)
	return HttpResponse(searchContents) #, 'application/javascript')

