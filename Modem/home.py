from kivy.uix.boxlayout import BoxLayout
import sqlite3
from datetime import datetime
import shutil

#from log import Log for editing the mood and period straight from home 

class Home(BoxLayout):
    con = sqlite3.connect('modem.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userSaveData(
            date DATE PRIMARY KEY,
            mood FLOAT,
            gratitude TEXT,
            rant TEXT,
            action TEXT,
            period BOOL
        )
    ''')
    con.commit()
    con.close()

    def readData(self):
        #today = datetime.today().strftime('%Y-%m-%d')
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM userSaveData')
        result = str(cursor.fetchone())
        con.close()
        print(result)
        return result
    
    def saveData(self, data, attribute):
        today = datetime.today().strftime('%Y-%m-%d')
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM userSaveData WHERE date = ?", (today,))
        exists = cursor.fetchone()[0]
        if exists:            
            query = f'UPDATE userSaveData SET {attribute} = ? WHERE date = ?'
            cursor.execute(query, (data, today))
        else:
            query = f'INSERT INTO userSaveData (date, {attribute}) VALUES (?, ?)'
            cursor.execute(query, (today, data))
        con.commit()
        con.close()

    def exportFile(self):
            shutil.copyfile('modem.db', '/storage/self/primary/Documents/modemExport.db')
