# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# A class that allows you to represent the data you scrape from the web, any way you like
class PdfUrlsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # These are the only two things we care about scraping (according to client specifications)
    url         = scrapy.Field()
    filename    = scrapy.Field()

