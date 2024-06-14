from kivy.uix.screenmanager import Screen
import shutil
import sqlite3

class Stonks(Screen):
    def on_enter(self):
        self.warning = False
        self.ids.importButton.text = 'Import file'
        self.ids.importButton.buttonColor = 0.145, 0.125, 0.11, 1
        
# Export and Import
# You should let them choose where from 
   
    def toggleWarning(self):
        if self.warning == False:
            self.ids.importButton.text = 'Warning: this will overwrite all existing entries'
            self.ids.importButton.buttonColor = 1, 0, 0, 1    
            self.warning = True
        else:
            self.importFile()
            self.ids.importButton.text = 'Import file'
            self.ids.importButton.buttonColor = 0.145, 0.125, 0.11, 1
            self.warning = False

    def exportFile(self):
        try:
            shutil.copyfile('modem.db', '/storage/self/primary/Documents/modemExport.db')
        except:
            print('Could not export file')

    def importFile(self):
        try:
            shutil.move('/storage/self/primary/Documents/modemExport.db', 'modem.db')
        except:
            print('Could not import file')
    

