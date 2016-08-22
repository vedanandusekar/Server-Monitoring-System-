import random 
import time
import datetime
import sys

date = "2014-10-31"
timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
dataPath = sys.argv[1] + '/'
val1=192
val2=168
val3=1
val4=10
for i in range (0,1000):
	if (val4 < 255):
	   val4 +=1
	elif (val3 < 255):
	   val4=0        
	   val3 +=1
	elif(val2 < 255):
	   val4=0 
	   val3=0
	   val2 +=1
	elif(val1 < 255):
	   val4=0
	   val3=0
	   val2=0
	   val1 +=1
	else:
	  break 
	IP_Address = str(val1) + '.'+ str(val2) + '.' + str(val3) + '.' + str(val4)
         
	#timestamp = 1414689783
	day  = 24*60
	minute = 60
	path = dataPath+str(IP_Address)+".txt"
        fo = open(path,"w")
	for minute in range(0,day):
		timestamp += 60
		minute + 60

		fo.write(str(timestamp)+' '+str(IP_Address)+' '+'0 '+str(random.randint(0,100))+'\n')
		fo.write(str(timestamp)+' '+str(IP_Address)+' '+'1 '+str(random.randint(0,100))+'\n')
	fo.close()
        print fo
