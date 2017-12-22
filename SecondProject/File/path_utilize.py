import os
from os import path
import datetime
from datetime import date,time,timedelta
import time
def main():
	print(os.name)
	print("Item exists: " + str(path.exists("newfile.txt")))
	print("Item exists: " + str(path.isfile("newfile.txt")))
	print("Item exists: " + str(path.isdir("hello.txt")))
	print("Using path and split")
	print("Item's path " +str(path.realpath("hello.txt")))
	
	print("Item's path and name " + str(path.split(path.realpath("hello.txt"))))
if __name__ == '__main__':
	main()

def function():
	print("Get modified time")
	t = time.ctime(path.getmtime("newfile.txt"))
	print(t)
	print(datetime.datetime.fromtimestamp(path.getmtime("newfile.txt")))

	print("Minute has modified")
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("newfile.txt"))
	print("This file has been modifed for " + str(td))
	print("Or " + str(td.total_seconds()) + " seconds")

function()