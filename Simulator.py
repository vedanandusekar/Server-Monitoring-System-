# -*- coding: utf-8 -*-
import os, sys
IP_Dict = {}

def initialize():
	
	if len(sys.argv) != 2:
		print "Invalid command. Command usage: python file_name.py DATA_PATH"
		exit()

	path = sys.argv[1] + '/'                # path should be in format - /home/veda/Code
	try: 
		dirs = os.listdir( path )
	except OSError, e:
		if e.errno == 2:
			print "Invalid path. Please enter a valid path. Example: /home/User/Files"
		else:
			print e.errno
			print e
		exit()

	# This would print all the files and directories
	for file in dirs:
		filepath = os.path.abspath(path+file)
		#print filepath
		f = open(filepath, "r")
		fileName = str(file)
		ID_Dict = {}
		Value_Dict_0 = {}
		Value_Dict_1 = {}
		hh = 0;
		mm = 0;
		for lines in f:
			line = lines.split(' ')
			#print line[1]
			if hh < 10:
				ts_hh = '0'+str(hh)
			else:
				ts_hh = str(hh)
			if mm < 10:
				ts_mm = '0'+str(mm)
			else:
				ts_mm = str(mm)

			if line[2] == '0':
				Value_Dict_0[str(ts_hh+':'+ts_mm)] = line[3]
			else :
				Value_Dict_1[str(ts_hh+':'+ts_mm)] = line[3]
				if mm < 59:
					mm += 1
				else:
					hh += 1
					mm = 0
				
		ID_Dict['0'] = Value_Dict_0
		ID_Dict['1'] = Value_Dict_1
	
		IP_Dict[fileName] = ID_Dict

	return


def CPU_Calculation():
	input = raw_input("QUERY ")

	while(input!="EXIT"):

		output = input.split(' ')
		if len(output) != 6:
			print "Invalid query. Query Usage Example:IP cpu_id time_start time_end Time_start time_end "
		else:
			varIP,varID,startDate,start,endDate,end = output[0],output[1],output[2],output[3],output[4],output[5]

			output1 = output[0] +'.txt'
	
			tempDictID = IP_Dict[output1]
			tempDictValue = tempDictID[varID]
	
			points_small = dict(filter(lambda (k,b): k >= start and k <= end,tempDictValue.items()))

			print "CPU"+varID+" usage on "+varIP+":"

			for j in sorted(points_small):
			 #      print j+"-->"+points_small[j]
				usage = points_small[j].strip('\n')
				print "("+startDate+" "+j.strip('\n')+ ", "+usage+"%)"

		input = raw_input("QUERY ")
	return

initialize()
CPU_Calculation()


