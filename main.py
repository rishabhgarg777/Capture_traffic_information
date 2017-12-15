

from sys import*
from datetime import datetime
import os
import time
from subprocess import check_output
time_interval=int(argv[1])
total_time=int(argv[2])


start=datetime.now()
start=str(start)

date=start.split(' ')[0]
date=str(date)
date=date.replace('-','_')
print date

time_=start.split(' ')[1]
print "Now time is:- ",time_
time_=time_.split(":")
time_[2]=time_[2].split('.')[0]

start_time=int(time_[0])*3600+int(time_[1])*60+int(time_[2])
end_time=start_time+(total_time)*60

folder='./'+date+'/'
if not os.path.exists(folder):
	os.makedirs(folder)
i=start_time
while(i<end_time):
	file_time=datetime.now()
	file_time=str(file_time).split(' ')[1]
	file_time=file_time.split(':')
	file_time[2]=file_time[2].split('.')[0]
	file_name=file_time[0]+'_'+file_time[1]+'_'+file_time[2]
	if not os.path.exists(folder+file_name+'/'):
		os.makedirs(folder+file_name+'/')
	os.system('python take_screenshot.py '+file_name+' '+folder+file_name+'/')
	print "Going in sleep mode"
	#time.sleep(3*60)
	time.sleep((time_interval-2)*60)
	i+=time_interval*60

