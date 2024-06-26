from kivy.uix.boxlayout import BoxLayout
import sqlite3
from datetime import datetime, timedelta
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
        #dateLabel
        if self.date == datetime.today().strftime('%d/%m/%Y'):
            self.ids.dateLabel.text = 'Today'
        elif self.date == (datetime.today() - timedelta(days=1)).strftime('%d/%m/%Y'):
            self.ids.dateLabel.text = 'Yesterday'
        else:
            dateObj = datetime.strptime(self.date, '%d/%m/%Y')
            self.ids.dateLabel.text = dateObj.strftime('%d %b')
        #moodInput
        self.ids.moodInput.value = savedEntries[0]
        #gratitudeInput
        self.ids.gratitudeInput.text = savedEntries[1]
        #rantInput
        self.ids.rantInput.text = savedEntries[2]
        #actionInput
        self.ids.actionInput.text = savedEntries[3]
        #periodGraphic
        if savedEntries[4] == 1:
            self.ids.periodGraphic.source = 'Graphics/periodTrue.png'
        else:
            self.ids.periodGraphic.source = 'Graphics/periodFalse.png'
    
    def sliderImage(self):
        pass
        
    def getData(self):
        con = sqlite3.connect('modem.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM userSaveData WHERE date = ?', (datetime.today().strftime('%d/%m/%Y'),))
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
        if isPeriod == 1:
            self.ids.periodGraphic.source = 'Graphics/periodTrue.png'
        else:
            self.ids.periodGraphic.source = 'Graphics/periodFalse.png'

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

    boredKeywords = ['groggy', 'bored', 'eh']
    sadKeywords = ['sad', 'depressed']
    angryKeywords = ['angry','annoyed','irritable']
    selfConciousKeywords = ['conscious','body','face','weight','fat','eating','ate','food','ugly']
    conflictKeywords = ['told', 'said', 'hurt', 'fought', 'think', 'argu']
    lonelyKeywords = ['lonely','alone','friends']

    boredSuggestions = ['Clean', 'Pick the easiest thing on your to do list and tick it off', 'Go for a walk', 'Bake']
    sadSuggestions = ['Cry it out', 'Listen to gentle music', 'Have a full shower']
    angrySuggestions = ['You could just be hungry', 'Punch a pillow', 'Go somewhere you can scream', 'Listen to really loud music']
    selfConciousSuggestions = ['Do a workout', 'Plan healthy meals for the rest of the day', 'Wear something comfortable']
    conflictSuggestions = ['How long do your conflicts normally last?\nTime will heal this', 'Give them space', 'Try to see it from their perspective', 'Let them know how you feel']
    lonelySuggestions = ['Message a group chat', 'Call a friend or family member']

    relevantSuggestions = []

    for keyword in boredKeywords:
        print(keyword)
        if keyword in rant.lower():
            relevantSuggestions += sadSuggestions
        break
    
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