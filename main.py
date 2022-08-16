import kivymd
kivymd.require("1.9.1")
from kivymd.app import App
from kivymd.uix.button import Button
class ButtonApp(App):
     
    def build(self):
         
        btn = Button(text ="Push Me !")
        return btn
 

root = ButtonApp()
 

root.run()