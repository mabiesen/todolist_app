#Given program size, save data to
#designated files as easy solution

import os

#Write data to file

#Read data from file as one chunk
def read_file_whole(filename):
	with open(filename, "r") as f:
		contents = f.read()
	f.close()
	return contents

#Read data from file to tuple
def read_file_tuple():
	with open(filename, "r") as f:
		contents = f.read().splitlines()
	f.close()
	return contents

#Create new file
def write_file(filename, data):
	with open(filename, 'w') as f:
		f.write(data)
	f.close()

#Append to file
def append_file(filename,data):
	with open(filename, 'a+') as f:
		data = str(data) + "\n"
		f.write(data)
	f.close()

#Destroy file
def destroy_file(filename):
	os.remove(filename)

#Delete line
# This solution opens the file in r/w mode ("r+")
# and makes use of seek to reset the f-pointer then truncate to remove everything after the last write
def delete_line(filename, matchtext):
	f = open(filename,"r+")
	d = f.readlines()
	f.seek(0)
	for i in d:
		if i.find(matchtext) == -1:
			f.write(i)
	f.truncate()
	f.close()

#Script directory path
def script_directory_path():
	mypath = os.path.dirname(os.path.realpath(__file__))
	return mypath

#Return a list of all directory files
def all_directory_files(directory):
	filelist = ()
	for filename in os.listdir(directory):
		full_filepath = os.path.join(directory, filename)
		filelist.append(full_filepath)
	return full_filepath
