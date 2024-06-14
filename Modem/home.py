from kivy.uix.floatlayout import FloatLayout
import sqlite3
from kivy.uix.screenmanager import Screen
from datetime import datetime, timedelta
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp

class CustomButton(FloatLayout):

    def __init__(self, dateNeat, moodImage, gratitude, **kwargs):
        super(CustomButton, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.145, 0.125, 0.11, 1)
            self.background = RoundedRectangle(radius=[dp(10)])

        self.entryMoodImage = Image(source = moodImage, width = dp(20), height = dp(20), size_hint = (None, None))
        self.entryDate = Label(text=dateNeat, font_name = 'Fonts/bold.ttf', font_size = 18, size_hint=(None, None), valign = 'top')
        self.entryGratitude = Label(text=gratitude, font_name = 'Fonts/medium.ttf', font_size = 16, size_hint=(None, None), valign = 'top')
        self.entryButtonness = Button(background_normal='', background_color=(0, 0, 0, 0))
        
        self.add_widget(self.entryMoodImage)
        self.add_widget(self.entryDate)
        self.add_widget(self.entryGratitude)
        self.add_widget(self.entryButtonness)

        self.entryGratitude.bind(texture_size=self.centerWidgets)
        self.bind(size=self.centerWidgets)

        self.centerWidgets()

    def centerWidgets(self, *args): # I'm sorry
       padding = dp(10)
       
       self.size = self.size[0], self.entryGratitude.texture_size[1] + self.entryMoodImage.height + padding*3

       self.background.size = self.size
       self.background.pos = self.pos
       
       self.entryMoodImage.pos = self.pos[0] + padding, self.pos[1] + self.height - self.entryMoodImage.height - padding
       
       self.entryDate.size = self.size[0] - (padding*2), self.entryDate.texture_size[1]
       self.entryDate.text_size = self.entryDate.width, None
       self.entryDate.pos = self.entryMoodImage.pos[0] + self.entryMoodImage.width + padding, self.pos[1] + self.height - (self.entryDate.height+self.entryMoodImage.height)/2 - padding
       
       self.entryGratitude.size = self.size[0] - (padding*2), self.entryGratitude.texture_size[1]
       self.entryGratitude.text_size = self.entryGratitude.width, None
       self.entryGratitude.pos = self.pos[0] + padding, self.pos[1] + self.height - self.entryGratitude.height - self.entryMoodImage.height - padding*2
       
       self.entryButtonness.pos = self.pos
       self.entryButtonness.size = self.size

class Home(Screen):
    buttonList = []
    def on_enter(self):
        
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS userSaveData(
                date DATE PRIMARY KEY,
                mood FLOAT DEFAULT 2.5,
                gratitude TEXT DEFAULT '',
                rant TEXT DEFAULT '',
                action TEXT DEFAULT '',
                period INTEGER DEFAULT 0
            )
        ''')
        cursor.execute("SELECT COUNT(*) FROM userSaveData WHERE date = ?", (datetime.today().strftime('%d/%m/%Y'),))
        exists = cursor.fetchone()[0]
        if not exists:
            cursor.execute('INSERT INTO userSaveData (date) VALUES (?)', (datetime.today().strftime('%d/%m/%Y'),))
        con.commit()
        con.close()
        for button in self.buttonList: # Clears existing list
            self.ids.entryContainer.remove_widget(button)
        self.buttonList.clear()
        self.buildEntryButtons()
    
    def buildEntryButtons(self):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute('SELECT date, mood, gratitude FROM userSaveData') 
        data = cursor.fetchall()
        con.close() 
        data.reverse()
        
        for line in data:
            date = line[0]
            # Neatening dates
            if date == datetime.today().strftime('%d/%m/%Y'):
                dateNeat = 'Today'
            elif date == (datetime.today() - timedelta(days=1)).strftime('%d/%m/%Y'):
                dateNeat = 'Yesterday'
            else:
                dateObj = datetime.strptime(date, '%d/%m/%Y')
                dateNeat = dateObj.strftime('%d %b')
            # Getting mood
            mood = line[1]
            if mood < 1:
               moodImage = 'Graphics/0.5.png'
            elif mood < 2:
               moodImage = 'Graphics/1.5.png'
            elif mood < 3:
               moodImage = 'Graphics/2.5.png'
            elif mood < 4:
               moodImage = 'Graphics/3.5.png'
            else:
               moodImage = 'Graphics/4.5.png'
            # Getting gratitude 
            gratitude = line[2]
            
            # Entry buttons                     
            self.entryButton = CustomButton(dateNeat, moodImage, gratitude, size_hint_y=None)
            self.entryButton.entryButtonness.bind(on_press = lambda instance, dateValue=date: self.pressEntryButton(dateValue))
           

            
            self.buttonList.append(self.entryButton)
            self.ids.entryContainer.add_widget(self.entryButton)
            
    def pressEntryButton(self, date):
        self.manager.get_screen('log').date = date
        self.manager.current = 'log'
        