import requests
from bs4 import BeautifulSoup
for i in range(1,20):
    url='http://www.freebuf.com/www.freebuf.com?action=ajax_wenku&year=all&score=all&type=all&tech=0&keyword=&page='+str(i)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,'lxml')
    for i in soup.select('h3 a'):
        print(i.text.encode('latin-1').decode('unicode_escape'),i.get('href'))