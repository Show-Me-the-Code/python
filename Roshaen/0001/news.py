#importing required libraries
import requests
from win32com.client import Dispatch
import time
# using windows Speak to convert text to speech
speak = Dispatch('SAPI.spvoice')
# Must enter your news API
url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=YOUR NEWS API KEY HERE'
# Getting news from above url
news = requests.get(url).json()

headlines = news['articles']
newslist1 = []
for i in headlines:
    newslist1.append(i['title'])
str1 = ''
# Speak top 10 headlines
speak.Speak('Today\'s headlines are: ')
for j in range(len(newslist1)):
    str1 = str(j+1) + ': ' + newslist1[j]
    print(str1)
    speak.Speak(str1)

