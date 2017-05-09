# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
class DiaosixiashuowangPipeline(object):
    #def __init__(self):
     #   self.file = open('books.txt',mode='w+')
    #def process_item(self, item, spider):
    #    self.file.write(str(item['books_title']))
     #   self.file.write('\n')
      #  self.file.write(str(item['books_author']))
       # self.file.write('\n')
      #  self.file.write(str(item['books_info']))
      #  self.file.write('\n')
       # self.file.write(str(item['books_url']))
       # self.file.write('\n')
       # self.file.write(str(item['books_cheaper']))
        #self.file.write('\n')
       # return item
    

    def process_item(self, item, spider):
        cheaper = str(item['books_cheaper'])
        f= open(cheaper+'.txt','w')
        f.write(str(item['books_text']).replace(u'\xa0', u' '))
        f.close()
        #self.file.write(str(item['books_title']))
        #self.file.write('\n')
        #self.file.write(str(item['books_author']))
        #self.file.write('\n')s
        #self.file.write(str(item['books_info']))
        #self.file.write('\n')
        #self.file.write(str(item['books_url']))
        #self.file.write('\n')   
        return item


