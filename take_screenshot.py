from sys import*
import os
#taking the groud truth point of UKHRA route 
#3,8,13,16,18,22,23,28,30,32,38

time_=argv[1]
folder=argv[2]
lats=[23.5629794762,23.55356333,23.5638339616,23.5734398686,23.5803901374,23.5899426124,23.5905404266,23.617015,23.62591833,23.6407509281,23.6527257855]
longs=[87.2797557939,87.27244333,87.2498826079,87.2369699101,87.2274964561,87.2055189182,87.2060461896,87.21726833,87.22094667,87.2265615539,87.23317195]
latlong=zip(lats,longs)
i=0
for x in latlong:
	out_file=folder+str(time_)+'_'+str(i)+'.png'
	os.system('python map_plotter.py '+str(x[0])+' '+str(x[1]))
	os.system('python image_grab.py '+out_file)
	i+=1