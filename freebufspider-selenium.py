from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from bs4 import BeautifulSoup



browser = webdriver.Chrome()
browser.get('http://www.freebuf.com/wenku')
soup=BeautifulSoup(browser.page_source,"lxml")
s=0
while (len(soup.select('#pagination a'))>0)&(s<=4):
#902页
	try:
		browser.find_element_by_link_text(u"查看更多").click()#点击下一页
		sleep(2)#休眠时间设置为2秒，否则请求过快会导致异常
		soup=BeautifulSoup(browser.page_source,"lxml")
		s=s+1
		#browser.implicitly_wait(15)#休眠时间设置为15秒，否则js未加载完毕不可点击
	except:
		break
for elem in soup.select('h3 a'):
	print(elem.text,elem.get('href'))
browser.quit()