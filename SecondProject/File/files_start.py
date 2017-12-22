def main():
#write if not exist will be created
#	f = open("hello.txt","w+")
#	f = open("hello.txt","a+")
	# for i in range(10):
	# 	f.write("This is line %d\r\n " % (i+1))
	f = open("hello.txt","r")
	if f.mode == 'r':
	#	contents = f.read()
	#	print(contents)
		fl = f.readlines()
		for x in fl:
			print(x)
	
	f.close()


if __name__ == '__main__':
	main()