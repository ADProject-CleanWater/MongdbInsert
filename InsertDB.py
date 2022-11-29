import csv
import pymongo
from pymongo import MongoClient

# myclient = pymongo.MongoClient("mongodb://3.34.50.139:27017/")
myclient = MongoClient("mongodb://3.34.50.139:27017/", 27017)  # mongoDB는 27017 포트로 돌아갑니다.

# db =myclient.MONGODB
db = myclient["pmsbme"]
pms = db["pms"]
bme = db["bme"]

# '2008_2021_pms.csv' 미세먼지데이터
# '2008_2021_bme.csv' 온도,습도데이터
jsonList_pms=[]

with open("2008_2021_pms.csv", 'r', encoding='utf-8-sig') as file_pms:
    csvReader = csv.DictReader(file_pms)

    for rows in csvReader:
        jsonData_pms = {}
        jsonData_pms['date'] = rows['date'].strip()
        jsonData_pms['pm1'] = rows['pm1'].strip()
        jsonData_pms['pm10'] = int(rows['pm10'].strip())
        jsonData_pms['pm25'] = int(rows['pm25'].strip())

        jsonList_pms.append(jsonData_pms)

    db.pms.insert_many(jsonList_pms)

jsonList_bme=[]

with open("2008_2021_bme.csv", 'r', encoding='utf-8-sig') as file_bme:
    csvReader = csv.DictReader(file_bme)

    for rows in csvReader:
        jsonData_bme = {}
        jsonData_bme['date'] = rows['date'].strip()
        jsonData_bme['temp'] = rows['temp'].strip()
        jsonData_bme['humi'] = rows['humi'].strip()
        jsonData_bme['alti'] = rows['alti'].strip()
        jsonData_bme['press'] = rows['press'].strip()

        jsonList_bme.append(jsonData_bme)

    db.bme.insert_many(jsonList_bme)
