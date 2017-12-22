import os
import shutil
from shutil import make_archive
from os import path
from zipfile import ZipFile
def main():
	if path.exists("newfile.txt"):
		#get the path to the file in the current directory
		src = path.realpath("newfile.txt")
		# separate the path from the file name
		head,tail = path.split(src)
		print(head)
		print(tail)
		# let's make copy by appending .bak to the name
		dest = src + ".bak"
		# not use the shell to make a copy of the file
		shutil.copy(src,dest)
		shutil.copystat(src,dest)
		# rename the original file
		#os.rename("newfile.txt","hello.txt")
		# root_dir,tail= path.split(src)
		# shutil.make_archive("archive","zip",root_dir)
		with ZipFile("testzip.zip","w") as newzip:
			newzip.write("newfile.txt")
			newzip.write("newfile.txt.bak")
if __name__ == '__main__':
	main()

