#import util_general
from util import util_general
testcolonstring = "Hello:World"
testarray = [1,2,3,4,5,6,7,8,9]


#########
#split a string by its colons
mylist = colon_string_to_list(testcolonstring)
print(mylist)
#########

#########
#redimension a one dimensional array as two dimensional
newarray = one_to_twod_array(testarray, 3,3)
print(newarray)
#########

############################################
# import util_files
from ..util_files import *

testfile = "testfile.txt"
testfilestring = "Hel"
fullfilepath = script_directory_path() + "/listfiles/" + testfile

#############
#Append to file, or create file if file does not exist
append_file(fullfilepath, testfilestring)
############

##########
# Deletes all lines in file that contain the given text
delete_line_by_matchtext(fullfilepath, "Hello Wor")
###########

##########
#reads file contents to a list and prints list
filearray = read_file_to_list(fullfilepath)
print(filearray)
##########

#########
# read whole file contents and print as is
wholefile = read_file_whole(fullfilepath)
print(wholefile)
#########

########
# delete line by its indexed number
delete_line_by_index(fullfilepath, 0)
########

######
#Find the index value of the line for given text
indexnumber = find_line_index_by_matchtext(fullfilepath, "friend")
print(indexnumber)
######

#####
#Returns a list of files from the selected directory
directorylist = all_directory_files(util_files.script_directory_path())
print(directorylist)
#####
