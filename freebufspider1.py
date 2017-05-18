import requests
from bs4 import BeautifulSoup
for i in range(1,20):#先爬取20个页面，数字可以改
    url='http://www.freebuf.com/www.freebuf.com?action=ajax_wenku&year=all&score=all&type=all&tech=0&keyword=&page='+str(i)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,'lxml')#直接把json数据传递给BeautifulSoup解析
    for i in soup.select('h3 a'):
        #print(i.text,)
        print(i.text.encode('latin-1').decode('unicode_escape'),i.get('href'))#解析出的数据是unicode形式，所以要对unicode码进行转码操作
