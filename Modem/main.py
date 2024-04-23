# Please bear with while I figure out how this shit works
import kivy

kivy.require('2.3.0')


from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='Buildozer Test')
        # if no mood yet, just open log straight away

if __name__ == '__main__':
    MyApp().run()