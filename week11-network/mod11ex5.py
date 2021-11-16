#Importing Libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()#Next 3 lines for ssl
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:  ') #Requesting input
try:
    durl = urllib.request.urlopen(url, context=ctx).read() #Trying to open url
except:
    print('Sorry, that is not a valid URL.')#P2S
    exit()

ucount = input('Enter count: ')#Requesting input
try:
    ucount = int(ucount) #Trying to convert to a integer
except:
    print('Sorry, that is not a valid number.')#P2S
    exit()
upos = input('Enter Position: ')#Requesting input
try:
    upos = int(upos)#Trying to convert to a integer
except:
    print('Sorry, that is not a valid number.')#P2S
    exit()

for links in range(ucount): #Creating a for loop to run the specified number of times
    html = urllib.request.urlopen(url, context=ctx).read() #Opening url
    soup = BeautifulSoup(html, 'html.parser') #reading webpage html with BS
    tags = soup('a') #Looking for anchor tags
    count = 0 #Creating a counter
    for tag in tags: #Parsing through tags pulled from html
        count = count +1 #Plus one to counter
        if count > int(upos): #If count is greater than given pos, break
            break
        url = tag.get('href', None) #getting url and assigning it to url variable

print(url) #P2S
