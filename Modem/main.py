import kivy

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
import home, log

class MyScreenManager(ScreenManager):
    def switch_screen(self, screen_name):
        self.current = screen_name

class ModemApp(App):
    def build(self):
        sm =  MyScreenManager(transition = NoTransition())
        sm.add_widget(home.Home(name="home"))
        sm.add_widget(log.Log(name="log"))
        return sm

if __name__ == '__main__':
    ModemApp().run()
