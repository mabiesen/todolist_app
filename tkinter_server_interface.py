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
        self.a()

    def a(self):
		x = 0
		while x < 5:
			self.call_button = Button(self, text = "Call")
			self.call_button['command'] = lambda b=self.call_button: b.destroy()
			self.call_button.grid(row=x, column=5) # This is fixing your issue
			x = x + 1

root = Tk()
app = App(master=root)
app.mainloop()
