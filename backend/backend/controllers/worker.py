import os
import logging
import json
import shutil

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect

from backend.lib.base import BaseController, render
import backend.lib.helpers as h

log = logging.getLogger(__name__)

class WorkerController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/worker.mako')
        # or, return a string
        return 'Hello World'
        
    def get_keys(self):
        d = []
        d['key1'] = 'somestr123544123'
        d['key2'] = 'anotherstr8080345'
        return json.dumps(d)
    
    def upload(self):        
        if request.method == 'POST':
            uploadDir = os.path.join(config['pylons.paths']['static_files'], 'storage')
            myfile = request.params['msg_file']
            permanent_file = open(os.path.join(uploadDir, h.randomStr(16)) + '.dat', 'w')
            shutil.copyfileobj(myfile.file, permanent_file)
            myfile.file.close()
            permanent_file.close()
            print 'Received a new file'
            
        else:
            #print os.path.abspath(__file__)
            print config['pylons.paths']['static_files']
            return render('upload.html')
