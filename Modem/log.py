from kivy.uix.boxlayout import BoxLayout
import sqlite3
from datetime import datetime
import shutil
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty

class Log(Screen):
    date = None
        
    def on_enter(self):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute("SELECT mood, gratitude, rant, action, period FROM userSaveData WHERE date = ?", (self.date,))
        savedEntries = cursor.fetchall()[0]
        con.close()

        self.ids.dateLabel.text = self.date
        self.ids.moodInput.value = savedEntries[0]
        self.ids.gratitudeInput.text = savedEntries[1]
        self.ids.rantInput.text = savedEntries[2]
        self.ids.actionInput.text = savedEntries[3]
        if savedEntries[4] == 1:
            self.ids.periodGraphic.source = 'Graphics/periodTrue.png'
        else:
            self.ids.periodGraphic.source = 'Graphics/periodFalse.png'
        
    def getDateNeat(self, date):
        #if self.date == today or yesterday, write today or yesterday today = datetime.today().strftime('%Y-%m-%d')
        pass
    
    def sliderImage(self):
        print("HIT")
        
    def getData(self):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM userSaveData WHERE date = ?', (datetime.today().strftime('%Y-%m-%d'),))
        result = str(cursor.fetchall())
        con.close()
        print(result)
        return result
        
    def togglePeriod(self):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute("SELECT period FROM userSaveData WHERE date = ?", (self.date,))
        isPeriod = cursor.fetchone()[0]
        isPeriod = 1 - isPeriod
        cursor.execute('UPDATE userSaveData SET period = ? WHERE date = ?', (isPeriod, self.date))
        con.commit()
        con.close()

    def saveData(self, mood, gratitude, rant, action):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        query = ('UPDATE userSaveData SET mood = ?, gratitude = ?, rant = ?, action = ? WHERE date = ?')
        cursor.execute(query, (mood, gratitude, rant, action, self.date))
        con.commit()
        con.close()

'''
def getSuggestions(text):
    when bulb pressed

    sadKeywords = ['sad','groggy','bored','depressed']
    angryKeywords = ['angry','annoyed','irritable']
    selfConciousKeywords = ['conscious','body','face','weight','fat','eating','ate','food','ugly']
    conflictKeywords = ['told','said','hurt','fought','think','want']
    lonelyKeywords = ['lonely','alone','friends']

    sadSuggestions = ['Clean','Listen to music','Pick the easiest thing on your to do list and tick it off','Go for a walk','Shower']
    angrySuggestions = ['You could just be hungry','Punch a pillow','Go somewhere you can scream', 'Listen to really loud music']
    selfConciousSuggestions = ['Go for a run','Do a workout','Plan healthy meals for the rest of the day','Wear something comfortable']
    conflictSuggestions = ['Give them space','Try to see it from their perspective','Talk to them']
    lonelySuggestions = []

    relevantSuggestions = []

    for keyword in sadKeywords:
        print(keyword)
        if keyword in rant.lower():
            relevantSuggestions += sadSuggestions
        break

    for keyword in angryKeywords:
        print(keyword)
        if keyword in rant.lower():
            relevantSuggestions += angrySuggestions
        break

    for keyword in selfConciousKeywords:
        print(keyword)
        if keyword in rant.lower():
            relevantSuggestions += selfConciousSuggestions
        break

    for keyword in conflictKeywords:
        print(keyword)
        if keyword in rant.lower():
            relevantSuggestions += conflictSuggestions
        break

    for keyword in lonelyKeywords:
        print(keyword)
        if keyword in rant.lower():
            relevantSuggestions += lonelySuggestions
        break
	
    if not relevantSuggestions:
        relevantSuggestions += sadSuggestions + angrySuggestions + selfConciousSuggestions + conflictSuggestions + lonelySuggestions

    #print a random one in darkGreen
    #if they don't let them leave or save without writing what they're gonna do
'''    