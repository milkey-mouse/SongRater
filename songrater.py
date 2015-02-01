
from HTMLParser import HTMLParser
import urllib2
address = "http://www.songlyrics.com/index.php?section=search&searchW="
name = raw_input("Enter a song title and it will be auto-rated: ").replace(" ", "+")
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
    if(word != word.strip()):
        continue
    if(word == ""):
        continue
    if word == 'I':
        score = score + 1
    if word == 'baby':
        score = score + 1
    if word == 'butt':
        score = score + 1
    if word == 'we':
        score = score + 1
    if word == 'no':
        score = score + 1
    if word == 'go':
        score = score + 1
    if word == 'oh':
        score = score + 1
    if word == 'my':
        score = score + 1
    if word == 'she':
        score = score + 1
    if word == 'him':
        score = score + 1
    if word == 'her':
        score = score + 1
    if word == 'back':
        score = score + 1
    if word == 'gone':
        score = score + 1
    if word == 'yeah':
        score = score + 1
    if word == 'mine':
        score = score + 1
    if word == 'fat':
        score = score + 1
    if word == 'love':
        score = score + 1
    if word == 'us':
        score = score + 1
    if word == 'curves':
        score = score + 1
    if(word.endswith(",") == True):
        word = word[:len(word) - 1]
    if(word.endswith(")") == True):
        word = word[:len(word) - 1]
    if(word.endswith("(") == True):
        word = word[1:]
    if(word.endswith(".") == True):
        word = word[:len(word) - 1]
    #print "http://dictionary.reference.com/browse/" + word
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
    if(word == last_word):
        score = score + 1
        print "WORD REPEATED"
    last_word = word
score = score / (len(html) - 1)
score = score * 750
print str(score)[:str(score).find(".")] + "% crappy"
#except:
#    print "python is stupid and so are you"
