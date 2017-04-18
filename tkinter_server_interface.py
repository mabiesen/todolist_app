import util_files
#Python3 - from tkinter import *
#Python2 - from Tkinter import *
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import platform

myplatform = platform.system()

class App(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.make_label()
		self.make_buttons()

	def make_label(self):
		self.list_label = Label(self, text = "To Do List")
		self.list_label.grid(row=0, column=5)

	def make_buttons(self):
		mylist = self.getdata()
		x = 0
		endlist = 5
		listlength = len(mylist)
		if listlength < endlist:
			endlist = listlength
		while x < endlist:
			self.call_button = Button(self, text = mylist[x])
			self.call_button['command'] = lambda b=self.call_button: self.delete_button(b)
			self.call_button.grid(row=(x+1), column=5) # This is fixing your issue
			x = x + 1

	def getdata(self):
		mypath = util_files.script_directory_path()
		myfile = "todolist.txt"
		filename = mypath + "/listfiles/" + myfile
		mylist = util_files.read_file_to_list(filename)
		return mylist

	def deletedata(self,buttontext):
		mypath = util_files.script_directory_path()
		myfile = "todolist.txt"
		filename = mypath + "/listfiles/" + myfile
		util_files.delete_line_by_matchtext(filename, buttontext)

	def delete_button(self,b):
		mytext = b['text']
		self.deletedata(mytext)
		b.destroy()
		self.append_button()

	def append_button(self):
		mylist = self.getdata()
		if len(mylist) >= 5:
			self.call_button = Button(self, text=mylist[4])
			self.call_button['command'] = lambda b=self.call_button: self.delete_button(b)
			self.call_button.grid(column=5)

	def change_button_text(self, b):
		b['text'] = "hello"

root = Tk()
app = App(master=root)
app.mainloop()


#command to destroy a button on click
		#	self.call_button['command'] = lambda b=self.call_button: b.destroy()