from kivy.uix.boxlayout import BoxLayout
import sqlite3
import shutil
from kivy.uix.screenmanager import Screen
from datetime import datetime, timedelta
from kivy.app import App
from kivy.uix.button import Button

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
            self.ids.homeScreenContainer.remove_widget(button)
        self.buttonList.clear()
        self.buildEntryButtons()
    
    def buildEntryButtons(self):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute('SELECT date, mood, gratitude FROM userSaveData') 
        data = cursor.fetchall()
        con.close()
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
            # Entry buttons
            self.entryButton = Button(text = dateNeat, on_press = lambda instance, dateValue = date: self.pressEntryButton(dateValue))
            self.buttonList.append(self.entryButton)
            self.ids.homeScreenContainer.add_widget(self.entryButton)

    def pressEntryButton(self, date):
        self.manager.get_screen('log').date = date
        self.manager.current = 'log'
