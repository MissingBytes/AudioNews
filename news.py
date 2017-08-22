from bs4 import BeautifulSoup
import requests
import pyttsx
import time

e=pyttsx.init()
r=requests.get('http://www.thehindu.com/')
data=r.text
soup=BeautifulSoup(data,'lxml')

for link in soup.find_all('h3'):
    #if not link.a is None:
    print(link.a.get_text().encode('utf-8'))
    e.say('%s'%link.a.get_text())
    e.runAndWait()
    time.sleep(0.5)
