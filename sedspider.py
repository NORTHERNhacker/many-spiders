import requests
import json
data={'action':"search",'value':"12"}
url= 'http://sed.pwndata.com/api/sed/search'
r=requests.post(url,data=data)
data=json.loads(r.text)
#print(data)
i= data['data']['result']['开房数据']
