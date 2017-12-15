import gmplot
from sys import*
file_name="myhtml.html"
lat=float(argv[1])
longi=float(argv[2])
latitudes=[]
latitudes.append(lat)
print "----------------------MAP PLOTTER CALLED==================================="
longitudes=[]
longitudes.append(longi)
'''
lat=23.549220 
longi=87.289278
lat2=23.548895 
long2=87.284085 
latitudes=[23.5599646939]
longitudes=[87.2766435074]
more_lats=[lat]
more_lngs=[longi]
marker_lats=[lat]
marker_lngs=[longi]
heat_lats=[lat]
heat_lngs=[longi]
'''
gmap = gmplot.GoogleMapPlotter(lat,longi, 17)

gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=0)
gmap.scatter(latitudes, longitudes, '#3B0B39', size=0, marker=False)
gmap.scatter(latitudes, longitudes, 'k', marker=True)
gmap.heatmap(latitudes, longitudes)
#file_name='mymap.html'
gmap.draw('myhtml.html')
#os.system('firefox myhtml.html &')
quit()
