from kivy.uix.boxlayout import BoxLayout
import sqlite3

#from log import Log for editing the mood and period straight from home 

class Home(BoxLayout):
    def __init__(self):
        super(Home, self).__init__()  # Ensures kivy is set up before dealing with SQL
        con = sqlite3.connect('test.db')
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS userSaveData(
                date DATE PRIMARY KEY,
                mood FLOAT,
                gratitude TEXT,
                rant TEXT,
                action TEXT,
                period BOOL NOT NULL
            )
        ''')
        con.commit()
        con.close()

    def readData(self):
        return 'temp test'
    
    def saveData(self, data, dataType):
        print(data)
        # Write the text to a file