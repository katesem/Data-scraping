'''
In this program we are getting data from weather forecast site meteoprog.ua
'''
import re
import requests
from  bs4 import BeautifulSoup

page_url = requests.get('https://meteo.ua/34/kiev/today')
soup = BeautifulSoup(page_url.content, 'html.parser') #getting html content from page

week = soup.find(class_="ww_block no_js") #this variable contains html block (class "ww_block no_js")
weather_items = week.find_all(class_="wwt_cont")


#Operations for correct displaying months names:
#adding 'a' for Март and  Август for other - replacing 'ь' with 'я'

date = [
        (item.find(class_ = "wwt_num").get_text() + " " + item.find(class_ = "wwt_mon").get_text().replace('ь','я') #date of forecast
        if item.find(class_ = "wwt_mon").get_text().endswith('ь') else item.find(class_ = "wwt_mon").get_text()+'a') for item in weather_items ]


#Extracting short weather description:

short_desc = [item.find('img').get('title') for item in weather_items]

min_temp  =  [re.sub(r'\s', '', item.find('span', {'class':'wwt_tmp wwt_min'}).find('span', class_ = None).get_text())  for item in weather_items]

max_temp  =  [re.sub(r'\s', '', item.find('span', {'class':'wwt_tmp wwt_max'}).find('span', class_ = None).get_text())  for item in weather_items]
print(max_temp)
print(min_temp)









