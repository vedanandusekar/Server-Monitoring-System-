Consider a monitoring system, which monitors 1000 servers. Each server has 2 CPUs. Each server generates a log for CPU usage every minute. 

The format is like this:

timestamp 	IP 		cpu_id usage
1414689783	192.168.1.10	0	87
1414689783	192.168.1.10	1	90
1414689783	192.168.1.11	1	93
	
This simulator generate the logs for one day, say 2014-10-31, just use random numbers between 0% to 100% as CPU usage. 
The generator should write data to files in a directory.  The timestamp is Unix time.
I created command line tool which takes a directory of data files as a parameter and lets you query CPU usage for a 
specific CPU in a given time period. It is an interactive command line tool which reads a user’s commands from stdin. 
The tool may take several minutes to initialize, but the query result returned within 1 second.
The tool support two commands:
One command will print results to stdout. 
Its syntax is QUERY IP cpu_id time_start time_end. Time_start and time_end specified in the format YYYY-MM-DD HH:MM 
The second command to support is EXIT.  It will exit the too.
