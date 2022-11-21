from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://3.34.50.139:27017/")
db = client['AD']
pms = db["pms"]

print(datetime.datetime.today().replace(microsecond=0))
mydic = [{"pm10": "1", "pm25": "20", "createdAt": datetime.datetime.today().replace(microsecond=0)}]
pms.insert_many(mydic)

for d, cnt in zip(db['pms'].find(), range(10)):
    print(d['pm25'])
    print(d['pm10'])
    print("-------------------")
