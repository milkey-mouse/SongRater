# -*- coding: cp1252 -*-
#Copyright Milkey Mouse 2015
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
import feedparser
import subprocess
import datetime
import urllib2
import string
import uuid
import math
import sys
import os

celery = Celery("flaskserver")

y = 0
top = feedparser.parse('https://itunes.apple.com/us/rss/topsongs/limit=100/explicit=true/xml')
for y in range(0, 99):
    top2 = top.entries[y].title
    top2 = top2[:top2.find(" - ")]
    print top2
    aar = flasktasks.rate.delay(top2)
