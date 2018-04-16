#!/usr/bin/python3
import xml.etree.ElementTree as ET
from urllib.request import urlretrieve
import os
import shutil
import webbrowser as wb

shutil.rmtree("news/")
os.makedirs("news/")

def print_rssfeed_yahoo(ticker): #added yahoo name
    url_="http://finance.yahoo.com/rss/headline?s="+str(ticker) #url to be specified
    urlretrieve(url_,"news/data.xml")
    root=ET.parse("news/data.xml").getroot()
    iter=root.iter("item")
    counter=0
    for i in iter:
        counter=counter+1
        print(str(counter)+")" + str(i[0].text))
    
print_rssfeed_yahoo(ticker="BTC-USD")

def print_rssfeed_bitnewz(): #printing news from bitnewz
    reply = input("Do you want general (G) or specific (S) news about \
                  cryptocurrencies?")
    if reply.lower == "g":
        url_="http://www.bitnewz.net/rss/"
        urlretrieve(url_,"news/data.xml")
        root=ET.parse("news/data.xml").getroot()
        iter=root.iter("item")
        counter=0
        for i in iter:
           counter=counter+1
           print(str(counter)+")" + str(i[0].text))
    else:
       reply2 = input("Do you want a specific date (1), search term (2) \
                      or number of results (3)?")
       try:
            if reply2 == "1":
                a= input("day?")
                b= input("month?")
                c= input("year?")
                url_="http://www.bitnewz.net/rss/feed/"+b+"-"+a+"-"+c
                urlretrieve(url_,"news/data.xml")
                root=ET.parse("news/data.xml").getroot()
                iter=root.iter("item")
                counter=0
                for i in iter:
                  counter=counter+1
                  print(str(counter)+")" + str(i[0].text))
            elif reply2 == "2":
                d = input("What term do you want to search?")
                url_="http://www.bitnewz.net/rss/feed/"+d
                urlretrieve(url_,"news/data.xml")
                root=ET.parse("news/data.xml").getroot()
                iter=root.iter("item")
                counter=0
                for i in iter:
                  counter=counter+1
                  print(str(counter)+")" + str(i[0].text))
            else:
                e = input("How many results do you want?")
                url_="http://www.bitnewz.net/rss/feed/"+e
                urlretrieve(url_,"news/data.xml")
                root=ET.parse("news/data.xml").getroot()
                iter=root.iter("item")
                counter=0
                for i in iter:
                  counter=counter+1
                  print(str(counter)+")" + str(i[0].text))          
       except:
            print("You're supposed to enter either 1 or 2 or 3. Try again")
            if reply2 == "1":
                a= input("day?")
                b= input("month?")
                c= input("year?")
                url_="http://www.bitnewz.net/rss/feed/"+b+"-"+a+"-"+c
                urlretrieve(url_,"news/data.xml")
                root=ET.parse("news/data.xml").getroot()
                iter=root.iter("item")
                counter=0
                for i in iter:
                  counter=counter+1
                  print(str(counter)+")" + str(i[0].text))
            elif reply2 == "2":
                d = input("What term do you want to search?")
                url_="http://www.bitnewz.net/rss/feed/"+d
                urlretrieve(url_,"news/data.xml")
                root=ET.parse("news/data.xml").getroot()
                iter=root.iter("item")
                counter=0
                for i in iter:
                  counter=counter+1
                  print(str(counter)+")" + str(i[0].text))
            else:
                e = input("How many results do you want?")
                url_="http://www.bitnewz.net/rss/feed/"+e
                urlretrieve(url_,"news/data.xml")
                root=ET.parse("news/data.xml").getroot()
                iter=root.iter("item")
                counter=0
                for i in iter:
                  counter=counter+1
                  print(str(counter)+")" + str(i[0].text))
           
