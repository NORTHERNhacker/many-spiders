import requests
from bs4 import BeautifulSoup
data={'action':"search",'value':"12"}
url= 'http://sed.pwndata.com/api/sed/search'
r=requests.post(url,data=data)
print(r.text)