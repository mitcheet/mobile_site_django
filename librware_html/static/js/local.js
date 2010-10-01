var jQT = $.jQTouch({
	icon: '/librware/static/img/zsr.cupola.57x57.png',
        statusBar: 'black'
});
$(document).ready(function() {
	$('#catalog').submit(function() {
		myQuery = escape($('#searchtext').val());
		myUrlBase = $('#urlbase').val();
		//alert (myQuery);
		$.ajax({
			type:"GET",
			url: 'http://erikmitchell.info/librware/search/?lookfor=' + myQuery,
			dataType: "json",
			success: function(data)
				{
				//alert(myUrlBase+myQuery);
				$('#search').empty();
				$('#search').append('<li class="sep">Results</li>');
				$.each(data.record2.docs, function(i, item) {
					var listItem = $('<li class="rounded"><a href="http://cloud.lib.wfu.edu/vufind/Record/' + item.id + '" target="_blank">' + item.title_short + ' - ' + item.callnumber + '</a></li>');
					$('#search').append(listItem);	
					if ( i == 5 ) return false;
				})
				}, 
			error: errorMsg
		});
		return false;
		//window.location.replace(myUrlBase + myQuery);
		//return false;
	});
	$('#search').click(function() {
	//This function was required because I removed the li in the search div that orig shows the first element of the twitterf feed.  the a did not work.
			window.location.replace($('#search a').attr('href'));
			});
 	$('.testfeed').bind('pageAnimationStart', function() {
		var myFeed = this.id;
		//$('.testfeed .toolbar h1').prepend('testing');
		feedurl = 'http://erikmitchell.info/librware/feed/' + myFeed;
		//alert(feedurl);
		$.ajax({
                	type: "GET",
               		url: feedurl,
                	dataType: "xml",
                	success: function(xml)
        			{
				//alert('parsing');
                		$('#' + myFeed + ' ul').empty();
				$(xml).find("item").each(function(i, j)
               					{
						var title = $(this).find('title').text();
                        			var pubDate = $(this).find('published').text();
                        			var summary = $(this).find('description').text();
						var link = $(this).find('link').text();
                        			var thumb1 = $(this).find('identifier').text()
						thumb = 'http://www.syndetics.com/index.php?isbn=/sc.gif&amp;client=YOURSITENAME&amp;upc=' + thumb1;
						bookcover = '<img class="thumbnail" max-height="75" src=' + thumb + ' />';
						var listItem = $('<li class="rounded"><span>' + title + '</span><a target="_blank" href="' + link + '">' + bookcover +  pubDate + '</a>' + '</li>');
                       				$('#' + myFeed + ' ul').append(listItem);
						
					});
				findImageSize();	
				},
                	error: errorMsg
		});	
	});
});


function errorMsg() {
	alert("error getting xml feed");
}
function findImageSize() {
 $('.testfeed').find('img').each(function() {
	if( $(this).width() < 2) {
		$(this).remove();
	}
});
}
