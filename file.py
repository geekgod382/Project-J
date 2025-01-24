import os
from com import speak

class fileop:

    '''This class is used to open files from the system'''

    def __init__(self):
        pass

    def find_file(self, filename, search_path):
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                return os.path.join(root, filename)
        return None

    def open_file(self,filename):
        search_path = "C:\\"
        file_path = self.find_file(filename, search_path)

        if file_path:
            os.startfile(file_path)
        else:
            speak("File not found.")