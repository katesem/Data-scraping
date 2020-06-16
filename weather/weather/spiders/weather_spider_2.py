

# Data scrapping using xpath

import scrapy
import pandas

class SpiderWeather(scrapy.Spider):
    
    name = 'weather_2'  # defines the unique name for the spider
    
    start_urls = [ 'https://meteo.ua/150/harkov']
    
    def parse(self, response):
            
        day_num = response.xpath('//div[@class="wwt_num"]/text()').getall()
        
        month = response.xpath('//div[@class="wwt_mon"]/text()').getall()
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
            'Short weather description': response.xpath('//span[@class="vl_child"]/span/img/@title').extract(),
            'Minimum temperature': response.xpath('//span[@class="wwt_tmp wwt_min"]/span[2]/text()').getall(),
            'Maximum temperature': response.xpath('//span[@class="wwt_tmp wwt_max"]/span[2]/text()').getall()
        })
    
        #saving data to .csv file:
        
        yield weather_table.to_csv('scrapy_weather_table_xpath.csv')
                                        
        # Use command : scrapy crawl weather_2