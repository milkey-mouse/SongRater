# -*- coding: cp1252 -*-
#Copyright Milkey Mouse 2015
from HTMLParser import HTMLParser
import simplejson as json
import feedparser
import webbrowser
import subprocess
import datetime
import urllib2
import string
import os

def cache(name):
    name = name.replace(" ", "+")
    address = "http://www.songlyrics.com/index.php?section=search&searchW="
    address = address + name
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
    #print html
    score = 0.00
    last_word = ""
    h = HTMLParser()
    for word2 in html.replace("\n", " ").split(" "):
        word = h.unescape(word2.lower())
        try:
            word = word.replace("’", "'")
        except:
            pass
        try:
            word = word.translate(string.maketrans("",""), string.punctuation)
        except:
            pass
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
                print "STUPID WORD:" + word
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
                if not '<div class="game-scrabble">' in response2:
                    isword = False
                else:
                    isword = True
            except:
                isword = True
            if isword == False:
                #print "NOT A WORD:" + word
                score = score + 2
            else:
                pass
                #print "IS A WORD: " + word
            if(word == "nah"):
                #print "CHANT REPEATED: " + word
                last_word = word
            elif(word == "na"):
                #print "CHANT REPEATED: " + word
                last_word = word
            elif(word == last_word):
                score = score + 1
                #print "WORD REPEATED: " + word
            last_word = word
            text = open("./cache/word/" + word + ".txt", 'w')
            text.write(str(score - lastscore))
            text.close()
            print "CACHED: " + word
    score = score / (len(html) - 1)
    score = score * 750

    if(score == 0):
        print "Sorry, we can't seem to be able to find that song."
    else:
        print str(score)[:str(score).find(".")] + "% crappy"
    #except:
    #    print "python is stupid and so are you"

y = 0
top = feedparser.parse('https://itunes.apple.com/us/rss/topsongs/limit=100/explicit=true/xml')
for y in range(0, 99):
    top2 = top.entries[y].title
    #top2 = top2[:top2.find(" - ")]
    print top2
    cache(top2)
