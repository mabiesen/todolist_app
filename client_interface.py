#Command line interface for client application

#OPTIONS
#Receive all list items(list)
#Send list item (list, item)
#delete list item (list, item)
import util_message
import client_sockets
import getopt
import sys

def command_line_arguments():
	print 'ARGV      :', sys.argv[1:]

	options, remainder = getopt.getopt(sys.argv[1:], 'r:s:d', ['requestlist',
	                                                         'send',
	                                                         'delete',
	                                                         ])
	print 'OPTIONS   :', options
	mysend = ""
	for opt, arg in options:
		if opt in ('-r', '--requestlist'):
			#mylist = util_message.get_user_input("Please provide the name of the list you would like to see: ")
			option = "request"
			mysend = option + ":" + arg
		elif opt in ('-s', '--send'):
			#mylist = util_message.get_user_input("Please provide the name of the list you would like to add to: ")
			data = util_message.get_user_input("Please provide some data to send: ")
			option = "send"
			mysend = option + ":" + arg + ":" + data
		elif opt in ('-d', '--delete'):
			#mylist = util_message.get_user_input("Please provide the name of the list you would like to add to: ")
			mymatch = util_message.get_user_input("Please provide some words that distinguish the line you would like to delete")
			option = "delete"
			mysend = option + ":" + arg + ":" + mymatch

	print("The following string will be sent: %s" % mysend)
	client_sockets.send_data(mysend)
command_line_arguments()
