from kivy.uix.screenmanager import Screen
import shutil
import sqlite3

try:
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_INTERNAL_STORAGE, Permission.WRITE_INTERNAL_STORAGE])
except:
    print('Couldnt import request_permissions')

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
            #if it exists:
                #remove it
            shutil.copyfile('modem.db', '/storage/self/primary/Documents/modemExport.db')
        except Exception as e:
            print(f'Could not export file: {e}')

    def importFile(self):
        try:
            shutil.move('/storage/self/primary/Documents/modemExport.db', 'modem.db')
        except Exception as e:
            print(f'Could not import file: {e}')
    

