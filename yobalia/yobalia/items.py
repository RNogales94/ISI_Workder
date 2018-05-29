# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YobaliaItem(scrapy.Item):

    title = scrapy.Field()
    summary = scrapy.Field()
    location = scrapy.Field()
    postDate = scrapy.Field()
    jornada = scrapy.Field()
