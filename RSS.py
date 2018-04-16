#!/usr/bin/python3
import xml.etree.ElementTree as ET
from urllib.request import urlretrieve
import os
import shutil
import webbrowser as wb

shutil.rmtree("news/")
os.makedirs("news/")

def print_rssfeed(ticker):
    url_="http://finance.yahoo.com/rss/headline?s="+str(ticker) #url to be specified
    urlretrieve(url_,"news/data.xml")
    root=ET.parse("news/data.xml").getroot()
    iter=root.iter("item")
    counter=0
    for i in iter:
        counter=counter+1
        print(str(counter)+")" + str(i[0].text))
    
print_rssfeed(ticker="BTC-USD")
