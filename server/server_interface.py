from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

#-----------------------------------------------------------------------

class ItemBoxLayoutExample(App):

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')

		l = Label(text='To Do List', font_size=24)
		layout.add_widget(l)

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1) )
            layout.add_widget(btn)
        return layout

#----------------------------------------------------------------------
if __name__ == "__main__":
    #app = HBoxLayoutExample()
    app = ItemBoxLayoutExample()
    app.run()
