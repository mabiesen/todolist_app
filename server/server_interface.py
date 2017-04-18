import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class VBoxLayoutExample(App):
    """
    Vertical oriented BoxLayout example class
    """

    #----------------------------------------------------------------------
    def setOrientation(self, orient):
        """"""
        self.orient = orient

    #----------------------------------------------------------------------
    def build(self):
        """"""
        layout = BoxLayout(padding=10, orientation='vertical')
		l = Label(text='To Do List', font_size=24)

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1) )
            layout.add_widget(btn)
        return layout

#----------------------------------------------------------------------
if __name__ == "__main__":
    #app = HBoxLayoutExample()
    app = VBoxLayoutExample()
    app.setOrientation('vertical')
    app.run()
