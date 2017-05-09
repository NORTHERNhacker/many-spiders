import scrapy
#from scrapy.selector import Selector
from bs4 import BeautifulSoup
from diaosixiashuowang.items import DiaosixiashuowangItem
import logging
import os
class diaosispider(scrapy.Spider):
	"""docstring for diaosispider"""
	name = 'diaosixiashuowang'
	allowed_domains = ["1766bbs.com"]
	start_urls = ['http://www.1766bbs.com/book/9/default-0-0-0-0-1.html'] 

	def parse(self,response):
		if response.status == 200:
			#for i in range(2,29):
			for x in range(1,30):
				item=DiaosixiashuowangItem()
				item['books_title'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[1]/h3/a/text()').extract()[0]
				#item['books_author'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[2]/span/text()').extract()
				#item['books_info'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[3]/text()').extract()
				item['books_url'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[1]/h3/a/@href').extract()[0]
					#item['books_title'],item['books_author'],item['books_info'],item['books_url'] = response.xpath("//*[@id="main"]/div[3]/div[2]/div["str(x)+"]/dl[2]/dd[1]/h3/a""|//*[@id="main"]/div[3]/div[2]/div[2]/dl["str(x)+"]/dd[2]/span""|//*[@id="main"]/div[3]/div[2]/div[2]/dl["+str(x)+"]/dd[3]/text()""|//*[@id="main"]/div[3]/div[2]/div[2]/dl["+str(x)+"]/dd[1]/h3/a").extract()
				path = str(item['books_title'])
				os.makedirs(os.path.join("j:\小说",path))
				next_url = 'http://www.1766bbs.com'+str(item['books_url'])
					#next_url = 'http://www.1766bbs.com/book/9/default-0-0-0-0-'+str(i)+'.html'
				yield scrapy.Request(next_url,callback=self.parsecheaper)
		
	#def parse_books(self,response):
	#	if response.status == 200:
	#		for x in range(1,30):
	#			item=DiaosixiashuowangItem()
	#			item['books_title'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[1]/h3/a/text()').extract()
	#			item['books_author'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[2]/span/text()').extract()
	#			item['books_info'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[3]/text()').extract()
	#			item['books_url'] = response.selector.xpath('//*[@id="main"]/div[3]/div[2]/div[2]/dl['+str(x)+']/dd[1]/h3/a/@href').extract()[0]
	#			#item['books_title'],item['books_author'],item['books_info'],item['books_url'] = response.xpath("//*[@id="main"]/div[3]/div[2]/div[2]/dl[2]/dd[1]/h3/a""|//*[@id="main"]/div[3]/div[2]/div[2]/dl[2]/dd[2]/span""|//*[@id="main"]/div[3]/div[2]/div[2]/dl[2]/dd[3]/text()""|//*[@id="main"]/div[3]/div[2]/div[2]/dl["+str(x)+"]/dd[1]/h3/a").extract()
	#			next_url = 'http://www.1766bbs.com/book/9/default-0-0-0-0-'+str(i)+'.html'
	#			yield scrapy.Request(next_url, callback=self.parseall)
	#			#yield scrapy.Request(next_url, callback=self.parseall)
	def parsecheaper(self,response):
		if response.status == 200:
			for x in range(1,2000):
				item = DiaosixiashuowangItem()
				#item['books_cheaper'] = response.xpath('//*[@id="main"]/div[3]/div[2]/ul/li['+str(x)+']/a/text()').extract()[0]
				item['cheapers_url'] = response.xpath('//*[@id="main"]/div[3]/div[2]/ul/li['+str(x)+']/a/@href').extract()[0]
				next_url = response.url+str(item['cheapers_url'])
				yield scrapy.Request(next_url,callback=self.parseall)
	def parseall(self,response):
		if response.status == 200:
			item = DiaosixiashuowangItem()
			item['books_title'] = response.selector.xpath('//*[@id="content"]/div[1]/b/a[4]/strong/text()').extract()[0]
			#item['books_text'] = response.xpath('//*[@id="htmlContent"]/text()').all().extract()[0]
			item['books_cheaper'] = response.xpath('//*[@id="jsnc_l"]/div/div[1]/h1/text()').extract()[0]
			alltxt=response.xpath('//*[@id="htmlContent"]')
			info = alltxt.xpath('string(.)').extract()[0]
			item['books_text'] = info
			path = str(item['books_title'])
			os.chdir("j:\小说\\"+path)
			yield item

