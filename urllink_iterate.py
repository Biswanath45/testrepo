#The program will use urllib to read the HTML from the data files below, extract the href= vaues 
#from the anchor tags, scan for a tag that is in a particular position relative to the first name 
#in the list,follow that link and repeat the process a number of times and report the last name you find.

#Download the file http://www.py4e.com/code3/bs4.zip
#unzip it in the same directory as this file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter URL:")
count= int(input("Enter count:"))
position=int(input("Enter position: "))

def f(u,p):
    html=urllib.request.urlopen(u, context=ctx).read()
    soup=BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    total=0
    for tag in tags:
        total=total+1
        if total==p:
            newurl=tag.get('href', None)
            break
    return newurl

for i in range(count):
    url=f(url,position)

lst=url.split('_')
lst_2=lst[len(lst)-1].split('.')
print(lst_2[0])

    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #total=total+int(tag.contents[0])
    #print('Attrs:', tag.attrs)
#print(total)