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

#Read data from file to a list
def read_file_to_list(filename):
	with open(filename, "r") as f:
		contents = f.read().splitlines()
	f.close()
	return contents

# adds a number to each line in list of filedata for easy index reference
def read_file_to_numbered_list(filename, data):
	ctr = 0
	with open(filename, "r") as f:
		contents = f.read().splitlines()
		for line in contents:
			mystuff = line
			numberedlist(ctr) = str(ctr) + ". " + mystuff
			ctr = ctr + 1
	f.close()
	return numberedlist

#Create new file
def write_file(filename, data):
	with open(filename, 'w') as f:
		data = str(data) + "\n"
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

#Delete line by matching text
# this would delete all lines containing text
# This solution opens the file in r/w mode ("r+")
# and makes use of seek to reset the f-pointer then truncate to remove everything after the last write
def delete_line_by_matchtext(filename, matchtext):
	f = open(filename,"r+")
	d = f.readlines()
	f.seek(0)
	for i in d:
		if i.find(matchtext) == -1:
			f.write(i)
	f.truncate()
	f.close()

def delete_line_by_index(filename, index):
	del_line = index   #line to be deleted: no. 3 (first line is no. 1)

	with open(filename,"r") as textobj:
	    list = list(textobj)    #puts all lines in a list

	del list[del_line - 1]    #delete regarding element

	    #rewrite the textfile from list contents/elements:
	with open(filename,"w") as textobj:
	    for n in list:
	        textobj.write(n)
	return


#Script directory path
def script_directory_path():
	mypath = os.path.dirname(os.path.realpath(__file__))
	return mypath

# this would find the line index based upon matching text
def find_line_index_by_matchtext(filename, matchtext):
	f = open(filename, "r+")
	d = f.readlines()

	ctr = 0
	for i in d:
		if i.find(matchtext) > -1:
			linenum = ctr
		ctr = ctr + 1
	f.close
	return linenum

#Return a list of all directory files
def all_directory_files(directory):
	filelist = ()
	for filename in os.listdir(directory):
		full_filepath = os.path.join(directory, filename)
		filelist.append(full_filepath)
	return full_filepath
