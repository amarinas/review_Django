from bs4 import BeautifulSoup
from urllib2 import urlopen
# set a url, first try Coding Dojo, then try pulling from a few of your favorite sites!
url = 'http://www.codingdojo.com'
# ask beutifuk soup to open the below url and parse all html
soup = BeautifulSoup(urlopen(url), "html.parser")
# and print the results!
# print soup

def makeUrlList():
    urlArr = []
    for i in range(len(soup('a'))):
        urlArr.append(soup('a')[i]['href'])
    return urlArr
list = makeUrlList()
print list
def makeUrlDictionary():
    urlDict = {}
    for i in range(len(soup('a'))):
        if urlDict.has_key(soup('a')[i]['href']):
            urlDict[soup('a')[i]['href']] += 1
        else:
            urlDict[soup('a')[i]['href']] = 1
    return urlDict
print makeUrlDictionary()
