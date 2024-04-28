import kivy

kivy.require('2.3.0')

from kivy.app import App
from home import Home

class ModemApp(App):
    def build(self):
        return Home()

if __name__ == '__main__':
    ModemApp().run()
