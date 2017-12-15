import sys
from depot.manager import*
from selenium import webdriver
print "============================Image GRAB CALLED========================"
file_name=sys.argv[1]
#file_name='x.jpg'
if __name__ == "__main__":
	depot=DepotManager.get()
	#driver=webdriver.Firefox()
	driver = webdriver.PhantomJS()
	driver.set_window_size(1024, 768) # set the window size that you need 
	driver.get('./myhtml.html')
	driver.save_screenshot(file_name)
	driver.quit()