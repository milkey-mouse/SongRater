# -*- coding: cp1252 -*-
#Copyright Milkey Mouse 2015
from multiprocessing.managers import BaseManager
from HTMLParser import HTMLParser
from flask import render_template
from flask.ext.gzip import Gzip
from celery import Celery
from celery import task
from flask import request
from celery.task.control import inspect
import simplejson as json
import flasktasks
from flask import Flask
import multiprocessing
import subprocess
import datetime
import urllib2
import string
import uuid
import math
import sys
import os

#went a bit OCD on the imports there

#note: might add a qr code generator

#FLASK HATES MULTIPROCESSING! ARGH!

app = Flask(__name__)
celery = Celery(app.name)
celery.conf.update(app.config)
gzip = Gzip(app)

celery.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER = 'json',
    BROKER_URL = 'amqp://',
    CELERY_IGNORE_RESULT = False,
    CELERY_TASK_RESULT_EXPIRES = 18000,
    CELERY_ENABLE_UTC = True,
)

    
@app.route('/dict')
def dictlist():
    return urllib2.urlopen("http://localhost:5555/api/tasks").read()

@app.route('/')
def hello_world():
    songname = request.args.get('songname', '')
    if(songname != ""):
            # show the user profile for that user
        address = "http://www.songlyrics.com/index.php?section=search&searchW="
        name = songname.replace("+", " ")
        newname = name
        prevurl = ""
        reqid = str(uuid.uuid4())
        try:
            songjson = json.loads(urllib2.urlopen("https://itunes.apple.com/search?term=" + name.replace(" ", "%20") + "&entity=song&limit=1").read())
            songlist = songjson['results']
            songlist = songlist[0]
            newname = songlist['trackName']
            prevurl = songlist['previewUrl']
            year = songlist['releaseDate']
            if prevurl.startswith("http://") == True:
                year = year[:4]
                if(int(year) < datetime.datetime.now().year - 15):
                    #print "CLASSIC: Released in " + year
                    score = score - 10;
        except:
            pass
        aar = flasktasks.rate.delay(newname)
        print str(aar.id)
            #p = multiprocessing.Process(target=rate, args=(newname, reqid, rqe))

        return render_template('loadingscreen.html', songname=newname, songurl=prevurl, reqid=aar.id)
    else:
        return render_template('search.html')


@app.route('/<uid>.txt')
def getprogress(uid):
    #try:
    jason = json.loads(urllib2.urlopen("http://localhost:5555/api/task/info/" + uid).read())
    jstate = jason["state"]
    if jstate == "SUCCESS":
        jstate = jason["result"]
    return jstate
    #except:
     #   return "none"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=True)
    s.serve_forever()
