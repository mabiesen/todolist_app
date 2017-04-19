#host a tcp server to receive data and return response

import socket
import threading
import server_manage_client_input

def start_server():
	bind_ip = "0.0.0.0"
	bind_port = 9999

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((bind_ip, bind_port))
	server.listen(5)

	print("[*] Listening on %s:%d" % (bind_ip, bind_port))

	#send back strings to client
	#server_manage_client_input determines what to do with a request.
	def reply_to_client(client_socket, request):
		success = server_manage_client_input.redirect_user_input(request)
		client_socket.send(success)
		client_socket.close()


	#this function called as new thread
	#receives information, then works on a reply
	def handle_client(client_socket):

	    #print out what the client sends
		request = client_socket.recv(1024)
		print("[*] Received %s" % request)
		reply_to_client(client_socket, request)


#Constantly scans for connections to clients.
#spins off a new thread when contact is made with client
	while True:
	    client, addr = server.accept()

	    print ("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

	    #spin up our client thread to handle incoming data
	    #the thread is declared in the first line and started in the second line
	    client_handler = threading.Thread(target=handle_client, args=(client,))
	    client_handler.start()
