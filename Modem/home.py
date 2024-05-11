from kivy.uix.boxlayout import BoxLayout
import sqlite3
import shutil
from kivy.uix.screenmanager import Screen
from datetime import datetime, timedelta
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

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
                
            mood = line[1]
            if mood < 1:
               moodImage = 'Graphics/0.5'
            elif mood < 2:
               moodImage = 'Graphics/1.5'
            elif mood < 3:
               moodImage = 'Graphics/2.5'
            elif mood < 4:
               moodImage = 'Graphics/3.5'
            else:
               moodImage = 'Graphics/4.5'
               
            gratitude = line[2]
            
            # Entry buttons
            self.entryButton = Button(
                text = dateNeat,
                on_press = lambda instance,
                dateValue = date: self.pressEntryButton(dateValue),
                size_hint_y=None,
                #height = 75 #this is the one that you wanna change
                )

            #big button
                #add a box layout verical
                    #add a box layout horizontal to vertical set the height to something static
                        #put image in horiz set width 
                        #put date in horiz
                    #add gratit to vertical the height should be variable
            
            ''' 
            entry_layout = BoxLayout(orientation='vertical')
            mood_label = Label(text=f"Mood: {mood}")
            date_label = Label(text=f"Date: {dateNeat}")
            gratitude_label = Label(text=gratitude)

            entry_layout.add_widget(mood_label)
            entry_layout.add_widget(date_label)
            entry_layout.add_widget(gratitude_label)

            self.entryButton = Button(
                size_hint_y=None,
                height=entry_layout.minimum_height,
                on_press=lambda instance, dateValue=date: self.pressEntryButton(dateValue)
            )
            
            self.entryButton.add_widget(entry_layout)
            '''
            self.buttonList.append(self.entryButton)
            self.ids.entryContainer.add_widget(self.entryButton)
            
    def pressEntryButton(self, date):
        self.manager.get_screen('log').date = date
        self.manager.current = 'log'
        