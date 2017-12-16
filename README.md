# Capture_traffic_information
This set of code captures the real time information of road traffic . It uses google map api to do this. Information is stored in form of image . To run this code you need to define the Latitude's and longituted's of location.

Instruction to run the code 


Requirements :-
	1. gmplot (sudo pip install gmplot)
	2. selenium
	3. PhantomJS


Step 1. Goto "/usr/local/lib/python2.7/dist-packages/gmplot"

Step 2. open file gmplot.py 

Step 3. 

		Copy these lines after  275th line  
			
			f.write(',styles: [{"stylers": [{"visibility": "off"}] }]') 


		Copy these two lines at the end of function write_points
		 
			f.write('\t\tvar trafficLayer = new google.maps.TrafficLayer();\n')
        
        	f.write('\t\ttrafficLayer.setMap(map);')
Step 4. Save gmplot.py

step 5. Run main.py
