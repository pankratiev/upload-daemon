import os

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import pyinotify

# Register the streaming http handlers with urllib2
register_openers()


# Start the multipart/form-data encoding of the file "DSC0001.jpg"
# "image1" is the name of the parameter, which is normally set
# via the "name" parameter of the HTML <input> tag.

# headers contains the necessary Content-Type and Content-Length
# datagen is a generator object that yields the encoded parameters
#--datagen, headers = multipart_encode({"image1": open("DSC0001.jpg")})

# Create the Request object
#--request = urllib2.Request("http://localhost:5000/upload_image", datagen, headers)
# Actually do the request, and get the response
#--print urllib2.urlopen(request).read()

def uploadFile(fname):
    if os.path.isfile(fname):
        print 'Upload file: ' + fname
        datagen, headers = multipart_encode({"msg_file": open(fname)})
        request = urllib2.Request("http://localhost:5000/upload", datagen, headers)
        print urllib2.urlopen(request).read()
    

def uploadAllFilesFromDir(d):
    dirs = os.listdir(d)
    for f in dirs:
        fname = os.path.join(d, f)
        uploadFile(fname)


watchDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inbound')

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print "Close write:", event.pathname
        uploadFile(event.pathname)

# Instanciate a new WatchManager (will be used to store watches).
wm = pyinotify.WatchManager()
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wm.add_watch(watchDir, pyinotify.ALL_EVENTS)
notifier.loop()