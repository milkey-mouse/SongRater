# -*- coding: cp1252 -*-
from multiprocessing.managers import BaseManager
from HTMLParser import HTMLParser
import simplejson as json
import multiprocessing
import webbrowser
import datetime
import urllib2
import string
import Queue
import uuid
import math
import sys
import os

def rate(name, uid):
    webbrowser.open("ducksarethebest.com")
    #try:
    class QueueManager(BaseManager): pass
    QueueManager.register('get_queue')
    m = QueueManager(address=('localhost', 1234), authkey="hi")
    m.connect()
    rq = m.get_queue()
    rq.put_nowait((uid, 0))
    address = "http://www.songlyrics.com/index.php?section=search&searchW="
    address = address + name.replace("-", " ")
    response = urllib2.urlopen(address)
    html = response.read()
    done = False
    html = html[html.find('<div class="serpresult">'):]
    html = html[html.find('http://'):]
    html = html[:html.find('"')]
    #try:
    response = urllib2.urlopen(html)
    html = response.read()
    html = html[html.find('<p id="songLyricsDiv"'):]
    html = html[html.find('>') + 1:]
    html = html[:html.find('</p>')]
    html = html.replace("<br>", "\n")
    html = html.replace("<br />", "\n")
    score = 0.00
    last_word = ""
    h = HTMLParser()
    words = html.replace("\n", " ").split(" ")
    wc = len(words)
    wd = 0
    for word2 in words:
        try:
            word = h.unescape(word2.lower())
            try:
                word = word.replace("’", "'")
            except:
                pass
            try:
                word = word.translate(string.maketrans("",""), string.punctuation);
            except:
                pass
            wd += 1
            rq.put_nowait((uid, math.floor((wc / wd) * 100)))
            if(word != word.strip()):
                continue
            if(word == ""):
                continue
            if(os.path.exists("./cache/word/" + word + ".txt")):
                text = open("./cache/word/" + word + ".txt", 'r')
                score = score + int(float(text.read()))
                text.close()
            else:
                lastscore = score
                if word == 'I':
                    #print "STUPID WORD:" + word
                    score = score + 1
                if word == 'baby':
                    #print "STUPID WORD:" + word
                    score = score + 1
                if word == 'butt':
                    #print "STUPID WORD:" + word
                    score = score + 2
                if word == 'no':
                    #print "STUPID WORD:" + word
                    score = score + 1
                if word == 'oh':
                    #print "STUPID WORD:" + word
                    score = score + 0.5
                if word == 'back':
                    #print "STUPID WORD:" + word
                    score = score + 1
                if word == 'gone':
                    #print "STUPID WORD:" + word
                    score = score + 0.5
                if word == 'yeah':
                    #print "STUPID WORD:" + word
                    score = score + 1
                if word == 'mine':
                    #print "STUPID WORD:" + word
                    score = score + 1
                if word == 'fat':
                    #print "STUPID WORD:" + word
                    score = score + 2
                if word == 'love':
                    #print "STUPID WORD:" + word
                    score = score + 1.5
                if word == 'curves':
                    #print "STUPID WORD:" + word
                    score = score + 2.5
                if(lastscore != score):
                    continue
                isword = False
                try:
                    response2 = urllib2.urlopen("http://dictionary.reference.com/browse/" + word).read()
                    webbrowser.open("http://dictionary.reference.com/browse/" + word)
                    if not '<div class="game-scrabble">' in response2:
                        isword = False
                    else:
                        isword = True
                except:
                    isword = True
                if isword == False:
                    #print "NOT A WORD:" + word
                    score = score + 2
                if(word == "nah"):
                    #print "CHANT REPEATED: " + word
                    last_word = word
                    pass
                elif(word == "na"):
                    #print "CHANT REPEATED: " + word
                    last_word = word
                    pass
                elif(word == last_word):
                    score = score + 1
                    #print "WORD REPEATED: " + word
                    pass
                last_word = word
                text = open("./cache/word/" + word + ".txt", 'w')
                text.write(str(score - lastscore))
                text.close()
                #print "CACHED: " + word
        except:
            pass
    score = score / (len(html) - 1)
    score = score * 750
    rq.put_nowait((uid, "s" + str(score)))
    #except:
    #    pass
    return "s" + str(score)

rate(sys.argv[1], sys.argv[2])
