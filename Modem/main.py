import kivy

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import sqlite3

class ModemApp(App):
    def build(self):
        return ModemScreen()

class ModemScreen(BoxLayout):
    con = sqlite3.connect('test.db')
    
    def readData(self):
        return 'temp test'
    
    def saveData(self, data, type):
        print(data)
        # Write the text to a file
    

        
#search 
#log
#graphs

if __name__ == '__main__':
    ModemApp().run()
