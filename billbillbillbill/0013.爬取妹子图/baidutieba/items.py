# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidutiebaItem(scrapy.Item):
    Img_name = scrapy.Field()
    Img_url = scrapy.Field()
    File_path = scrapy.Field()
    pass
