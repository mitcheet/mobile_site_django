#!/usr/bin/python2.6
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home5/erikmitc/.local/lib/python2.6")
sys.path.insert(0, "/home5/erikmitc/.local/lib/python2.6/site_packages")
sys.path.insert(0, "/home/erikmitc/.local/lib/python2.6/site-packages/librware")

# Switch to the directory of your project. (Optional.)
os.chdir("/home/erikmitc/.local/lib/python2.6/site-packages/librware")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "librware.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")

