# -*- coding: cp1252 -*-
#Copyright Milkey Mouse 2015
from HTMLParser import HTMLParser
import simplejson as json
import webbrowser
import subprocess
import urllib2
import string
import os

address = "http://www.songlyrics.com/index.php?section=search&searchW="
name = raw_input("Enter a song title and it will be auto-rated: ").replace(" ", "+")
#try:
songjson = json.loads(urllib2.urlopen("http://itunes.apple.com/search?term=" + name + "&entity=song&limit=1").read())
songlist = songjson['results']
songlist = songlist[0]
prevurl = songlist['previewUrl']
if prevurl.startswith("http://") == True:
    mp3file = urllib2.urlopen(prevurl)
    output = open('preview.m4a','wb')
    output.write(mp3file.read())
    output.close()
    webbrowser.open(os.path.abspath("preview.m4a"))
#except:
#    pass
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
    word = h.unescape(word2.lower()).replace("’", "'").translate(string.maketrans("",""), string.punctuation);
    if(word != word.strip()):
        continue
    if(word == ""):
        continue
    lastscore = score
    if word == 'I':
        print "STUPID WORD:" + word
        score = score + 1
    if word == 'baby':
        print "STUPID WORD:" + word
        score = score + 1
    if word == 'butt':
        print "STUPID WORD:" + word
        score = score + 2
    if word == 'no':
        print "STUPID WORD:" + word
        score = score + 1
    if word == 'oh':
        print "STUPID WORD:" + word
        score = score + 0.5
    if word == 'back':
        print "STUPID WORD:" + word
        score = score + 1
    if word == 'gone':
        print "STUPID WORD:" + word
        score = score + 0.5
    if word == 'yeah':
        print "STUPID WORD:" + word
        score = score + 1
    if word == 'mine':
        print "STUPID WORD:" + word
        score = score + 1
    if word == 'fat':
        print "STUPID WORD:" + word
        score = score + 2
    if word == 'love':
        print "STUPID WORD:" + word
        score = score + 1.5
    if word == 'curves':
        print "STUPID WORD:" + word
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
        print "NOT A WORD:" + word
        score = score + 2
    else:
        print "IS A WORD: " + word
    if(word == "nah"):
        print "CHANT REPEATED: " + word
        last_word = word
    elif(word == "na"):
        print "CHANT REPEATED: " + word
        last_word = word
    elif(word == last_word):
        score = score + 1
        print "WORD REPEATED: "
    last_word = word
score = score / (len(html) - 1)
score = score * 750
os.system("taskkill /im wmplayer.exe /f")
if(score == 0):
    print "Sorry, we can't seem to be able to find that song."
else:
    print str(score)[:str(score).find(".")] + "% crappy"
#except:
#    print "python is stupid and so are you"
