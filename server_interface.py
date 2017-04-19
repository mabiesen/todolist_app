import util_files
#Python3 - from tkinter import *
#Python2 - from Tkinter import *
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import platform

myplatform = platform.system()

# Container function
def mainfunc():
	class App(Frame):
		def __init__(self, master):
			Frame.__init__(self, master)
			self.number_of_btns = 4
			self.grid()
			self.grid_columnconfigure(0, weight=1)
			self.make_label()
			self.make_buttons()

		# Create the ToDolist label
		def make_label(self):
			self.list_label = Label(self, text = "To Do List", font=(None, 30), height=3)
			self.list_label.grid(row=0, column=5)

		# Create our buttons initially when program starts
		def make_buttons(self):
			mylist = self.getdata()
			x = 0
			endlist = 4
			listlength = len(mylist)
			if listlength < endlist:
				endlist = listlength
			while x < endlist:
				self.call_button = Button(self, text = mylist[x],width=60, height=2, font=(None, 15))
				self.call_button['command'] = lambda b=self.call_button: self.delete_button(b)
				self.call_button.grid(row=(x+1), column=5, sticky=E+W)
				x = x + 1

		# Retrieve list data from file as required
		def getdata(self):
			print("getdata was called")
			mypath = util_files.script_directory_path()
			myfile = "todolist.txt"
			filename = mypath + "/listfiles/" + myfile
			mylist = util_files.read_file_to_list(filename)
			return mylist

		# Delete data from the list file when a list item button is pressed
		def deletedata(self,buttontext):
			mypath = util_files.script_directory_path()
			myfile = "todolist.txt"
			filename = mypath + "/listfiles/" + myfile
			util_files.delete_line_by_matchtext(filename, buttontext)

		# Delete the button itself when pressed
		def delete_button(self,b):
			mytext = b['text']
			self.deletedata(mytext)
			b.destroy()
			self.append_buttons()

		#If we are displaying less than 4 buttons, and list has more,
		#make new buttons
		def append_buttons(self):
			print(len(self.winfo_children()))
			mylist = self.getdata()
			desired_num_btns = 4
			numbuttons = len(self.winfo_children())-1
			if numbuttons < desired_num_btns:
				firstdifference = desired_num_btns - numbuttons
				seconddifference = len(mylist) - numbuttons
				if firstdifference > seconddifference:
					loopwhile = seconddifference
				else:
					loopwhile = firstdifference

				ctr = 0
				while ctr < loopwhile:
					self.call_button = Button(self, text = mylist[numbuttons],width=60, height=2, font=(None, 15))
					self.call_button['command'] = lambda b=self.call_button: self.delete_button(b)
					self.call_button.grid(column=5)
					numbuttons = numbuttons + 1
					ctr = ctr + 1

			else:
				self.number_of_btns = self.number_of_btns - 1

	#Initialization of the class instance. tkinter loop
	root = Tk()
	#make fullscreen
	#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	#root.overrideredirect(1)
	#root.geometry("%dx%d+0+0" % (w, h))
	app = App(master=root)
	app.mainloop()


#command to destroy a button on click
		#	self.call_button['command'] = lambda b=self.call_button: b.destroy()
