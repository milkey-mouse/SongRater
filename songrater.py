
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
x = 0
for x in range(0, len(html) - 1):
    if html[x:x+1] == ' ':
        space = x
    if html[x:x+1] == 'I':
        score = score + 1
    if html[x:x+4] == 'baby':
        score = score + 1
    if html[x:x+4] == 'butt':
        score = score + 1
    if html[x:x+2] == 'we':
        score = score + 1
    if html[x:x+2] == 'no':
        score = score + 1
    if html[x:x+2] == 'go':
        score = score + 1
    if html[x:x+2] == 'oh':
        score = score + 1
    if html[x:x+2] == 'my':
        score = score + 1
    if html[x:x+3] == 'she':
        score = score + 1
    if html[x:x+3] == 'him':
        score = score + 1
    if html[x:x+3] == 'her':
        score = score + 1
    if html[x:x+4] == 'back':
        score = score + 1
    if html[x:x+4] == 'gone':
        score = score + 1
    if html[x:x+4] == 'yeah':
        score = score + 1
    if html[x:x+4] == 'mine':
        score = score + 1
    if html[x:x+3] == 'fat':
        score = score + 1
    if html[x:x+4] == 'love':
        score = score + 1
    if html[x:x+2] == 'us':
        score = score + 1
    if html[x:x+5] == 'curves':
        score = score + 1
        
last_word = ""
for word2 in html.replace("\n", " ").split(" "):
    word = word2.lower()
    if(word != word.strip()):
        continue
    if(word == ""):
        continue
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
