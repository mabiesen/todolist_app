#CLI MESSAGES FOR CLIENT
#Server error could not add to list
NO_LIST = "The program could not find a list with the specified name.  Please try again"
ITEM_RECEIVED = "Item was successfully received by the server."

#Client did or did not connect to server
NO_SERVER = "The program could not detct the server.  Is the server operational?"
DATA_SENT = "Data was sent successfully. You should see a message from the server soon."

#Client error, selection is not an option
NOT_AN_OPTION = "The command line option provided is not one of the specified commands."


#RELATED FUNCTIONS
def new_error(err):
	print("Error: %s" % err)

def new_success(success):
	print("Success! %s" % success)

def print_dictionary(mydict):
	for key,value in mydict.iteritems:
		print("%s, %s" % (key, value))

# prompt function
def get_user_input(prompt):
	answer = raw_input(prompt)
	return answer
