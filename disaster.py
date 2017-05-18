import requests
import json
import pymongo

key = ""#api的authkey
def get_disaster():
	try:
		client = pymongo.MongoClient('localhost', 27017)
		tianqi = client['tianqi']
		item_list = tianqi['tianqi_list']
	except:
		print('数据库连接失败')
	try:
		url = "https://api.seniverse.com/v3/weather/alarm.json?key="+key
		r = requests.get(url)
		data = json.loads(r.text)
		information = data['results']
	except:
		print('调用API失败')
	try:
		for i in range(len(information)):
			timezone = information[i]["location"]["timezone"]
			path = information[i]["location"]["path"]
			location = information[i]["location"]["name"]
			type1 = information[i]["alarms"][0]["type"]
			date = information[i]["alarms"][0]["pub_date"]
			description = information[i]["alarms"][0]["description"]
			level = information[i]["alarms"][0]["level"]
			title = information[i]["alarms"][0]["title"]
			item_list.insert_one({'灾难名':title,'灾难类型':type1,'灾难级别':level,'城市':location,'详细坐标':path,'时区':timezone,'时间':date,'具体情况':description})
	except:
		print('数据库插入失败')


if __name__ == '__main__':
	get_disaster()
