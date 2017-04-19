#This will launch our program
import server_sockets
import server_interface
import threading
#import server_toggle_display

def start_program():
	#Fire up a thread to detect motion and turn screen on or off
	#motion_thread = threading.Thread(target=server_toggle_display.start_detecting)

	#Fire up our server
	server_thread = threading.Thread(target=server_sockets.start_server)
	server_thread.start()

	#Fire up our user interface
	server_interface.mainfunc()


start_program()
