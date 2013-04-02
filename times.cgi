#!/bin/python
import datetime, pickle
hour = datetime.datetime.now().hour
try: 
    times = pickle.load(open("times.p","rb"))
except:
    times = {}
if hour in times: 
    times[hour] = times[hour] + 1 
else:
    times[hour] = 1
pickle.dump(times, open("times.p","wb"))

for k in times:
    print "hour"
    print k 
    print ":"
    print times[k]
    print "visits |||"
    
