import requests
from bs4 import BeautifulSoup
import json

for i in range(1, 20):
    url = 'http://www.freebuf.com/www.freebuf.com?action=ajax_wenku&year=all&score=all&type=all&tech=0&keyword=&page=' + str(
        i)
    r = requests.get(url)
    data = json.loads(r.text)
    soup = BeautifulSoup(data['cont'])
    for i in soup.select('h3 a'):
        print(i.getText(), i.get('href'))


