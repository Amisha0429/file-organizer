# Import modules
import PySimpleGUI as sg
import pathlib
import sys


# Class for GUI
class GUI:
    def __init__(self):
        self.event = None
        self.values = None
        self.path = pathlib.Path().absolute()
        self.get_folder()

    def get_folder(self):
        layout = [
            [sg.InputText("./"), sg.FolderBrowse('Browse', initial_folder=self.path)],
            
            [sg.Submit('Organize Files'), sg.Cancel()],
            ]
        window = sg.Window('File Organizer', layout)
        
        while True:
            self.event, self.values = window.Read()
            self.path = self.values[0]
            print(self.event)
            if self.event in ('Cancel', None):
                window.close()
                sys.exit("Script exit")
            elif self.event == 'Organize Files':
                break
        window.close()
    
if __name__ == "__main__":
    gui = GUI()
