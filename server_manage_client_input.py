# Client input must be interpreted and directed appropriately
import util_files
import util_general
# Main function to determine user input
def redirect_user_input(myinput):
	input_split = util_general.colon_string_to_list(myinput)
	if input_split(0) == "request":
		returnval = handle_get_list(input_split)
	elif input_split(0) == "send":
		returnval = handle_sent_list_item(input_split)
	elif input_split(0) == "delete":
		returnval = handle_delete(input_split)
	return returnval

# Handle socket request for entire list
def handle_get_list(myinput):
	myfile = myinput(1)
	filename = myfile + ".txt"
	mypath = util_files.script_directory_path()
	fullfilepath = mypath + "/listfiles/" + filename
	filecontents = util_files.read_file_whole(fullfilepath)
	return filecontents

# Handle socket request for entering new todo information
def handle_sent_list_item(myinput):
	myfile = myinput(1)
	filename = myfile + ".txt"
	mypath = util_files.script_directory_path()
	fullfilepath = mypath + "/listfiles/" + filename
	listitem = myinput(2)
	util_files.append_file(fullfilepath,listitem)
	return "Successfully added item to list!"

# Handle request to delete an item from a list
def handle_delete_item(myinput):
	myfile = myinput(1)
	filename = myfile + ".txt"
	mypath = util_files.script_directory_path()
	fullfilepath = mypath + "/listfiles/" + filename
	listitem = myinput(2)
	delete_line_by_matchtext(listitem)
	return "Successfully deleted list item"
