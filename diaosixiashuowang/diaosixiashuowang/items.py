# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiaosixiashuowangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    books_title = scrapy.Field() #小说名
    books_author = scrapy.Field()     #作者
    books_info = scrapy.Field()  #小说简介
    books_url = scrapy.Field()	#小说全章节链接
    books_latest = scrapy.Field()    		#最新章节
    books_cheaper = scrapy.Field()  #小说章节名
    books_text = scrapy.Field()  #小说正文
    cheapers_url = scrapy.Field()  #章节链接
    books_text = scrapy.Field()  #章节链接
    
