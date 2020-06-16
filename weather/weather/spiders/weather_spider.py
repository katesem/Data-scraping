
# Data scrapping using selectors

import scrapy
import pandas

class WeatherSpider(scrapy.Spider):
    
    name = 'weather'  # defines the unique name for the spider
    
    start_urls = [ 'https://meteo.ua/150/harkov'] #url for scraping
    
    def parse(self, response):
            
        day_num = response.css('div.wwt_num::text').getall()
        month = response.css('div.wwt_mon::text').getall()
        date = [] 
        
        #loop for correct displaying  month names
        
        for i in range(0, len(month)):
            if month[i].endswith('ь'):
                month[i] = month[i].replace('ь','я')  
            else:
                month[i] = month[i]+'a'
            date.append(str(day_num[i]) +" "+ month[i])
        
        
        # data scraping and conversion to table using pandas:
        
        weather_table = pandas.DataFrame(
            { 
            'Date' : date,
            'Short weather description': response.css('span.vl_child  img::attr(title) ').getall(),
            'Minimum temperature': response.css('div.wwt_tmps > span.wwt_tmp.wwt_min > span:nth-child(2)::text').getall(),
            'Maximum temperature': response.css('div.wwt_tmps > span.wwt_tmp.wwt_max > span:nth-child(2)::text').getall()
        })
    
        #saving data to .csv file:
        
        yield weather_table.to_csv('scrapy_weather_table.csv')
                                        
                                        
        # Use command in terminal : scrapy crawl weather 

        
        


