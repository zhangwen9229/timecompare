#!/usr/bin/python
#coding:utf-8
import datetime
import time

print(time.time())


today = datetime.date.today() 
ttt=time.mktime(today.timetuple())
print(today)
print(str(today))

format="%Y-%m-%d %H:%M:%S"

startTime = str(today) + " 09:00:00"
endTime = str(today) + " 21:00:00"
print(startTime)
sTime = time.strptime(startTime,format)
print(time.mktime(sTime))

eTime = time.strptime(endTime,format)
print(time.mktime(eTime))

print(time.time()>time.mktime(sTime))


print("--------------------------------------------------")

t1=time.strptime("2008-01-31 00:11:23",format)
t2=datetime.datetime(t1[0],t1[1],t1[2],t1[3],t1[4],t1[5],t1[6])
t3=t2-datetime.timedelta(minutes=30)
t3=str(t3)

b1=t3[0:4]
b2=t3[5:7]
b3=t3[8:10]
b4=t3[11:13]
b5=t3[14:16]
b6=t3[-2:]

print b1
print b2
print b3
print b4
print b5
print b6