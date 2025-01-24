# Cypher, an AI assistant

# initializing libraries
import subprocess
import time
import webbrowser
import random
import google.generativeai as ai
from datetime import datetime
import pyautogui
import threading
import re
import pywhatkit
from com import speak, get_audio
from battery import battery_reminder
from fraud import check_fraudulent
from greet import greetMe
from netspeed import speed_test
from sps import stone_paper_scissor
from file import fileop
from translate import trnslte

bat = battery_reminder()
tr = trnslte()
fileopener = fileop()

# function for setting an alarm
def alarm(alarm_time):
        current_time = datetime.now().strftime("%H:%M")
        while current_time != alarm_time:
            current_time = datetime.now().strftime("%H:%M")
            time.sleep(1)
        speak("Sir, Time's up!!")

def save_to_notepad(text):
    pyautogui.typewrite(text)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)

def alarm_thread(alarm_time): 
    alarm_thread = threading.Thread(target=alarm, args=(alarm_time,))
    alarm_thread.start()

# Set up Gemini API key
api= 'YOUR API KEY'
ai.configure(api_key=api)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def main():

    while(True):

        x = get_audio()
        x.replace("cypher", "")
        x.replace("hey cypher", "")

        print("")
        # performing tasks based on user inputs    
        if "open files" in x or "open file" in x or "open a file" in x :
            print("Enter file name with extension: ")
            speak("Enter file name with extension: ")
            c1=str(input())
            speak("Sure!")
            fileopener.open_file(c1)

        elif "open websites" in x or "open website" in x or "open a website" in x:
            print("Enter URL: ")
            speak("Enter URL: ")
            url=str(input())
            speak("Sure!")
            webbrowser.open(url)
        
        elif "open" in x:
            speak("Sure!")
            pyautogui.hotkey('win')
            time.sleep(0.5)
            pyautogui.typewrite(x[4:])
            time.sleep(0.5)
            pyautogui.press('enter')

        elif "how is the weather" in x or "what is the weather today" in x or "what's the weather" in x:
            subprocess.Popen("start ms-windows-weather:", shell=True)

        elif x=="what is the time":
            speak(time.strftime("It's %H:%M %p", time.localtime()))

        elif x=="what is the date":
            speak(time.strftime("It's %A, %d %B %Y", time.localtime()))

        elif "activate barn door protocol" in x or "activate protocol" in x:
            print("Barn door protocol activated")
            speak("Barn door protocol activated")
            print("Activation code: ", random.randint(100000, 999999))

        elif "set an alarm" in x:
            speak("For what time?")
            alarm_time = input("(HH:MM, in 24 hour format) ")
            alarm_thread(alarm_time)

        elif "store some data" in x or "store" in x:
            rw=r'Stored_data.txt'
            
            pyautogui.hotkey('win', 'r')
            pyautogui.typewrite(rw)
            pyautogui.press('enter')
            time.sleep(4)
            speak("Speak now")
            pyautogui.press('enter')
            text = get_audio()
            save_to_notepad(text)

        elif "close the system" in x or "close system" in x:
            print("Ok, Closing the system.")
            speak("Ok, Closing the system.")
            break

        elif "close" in x:
            pyautogui.hotkey('alt', 'fn', 'f4')

        elif "check a website for fraud" in x or "check website" in x:
            url = input('Enter the website URL to check: ')
            fraudulent = check_fraudulent(url)

            if fraudulent:
                speak('The website is fraudulent.')
            else:
                speak('The website is not fraudulent.')

        elif "check network speed" in x or "check internet speed" in x:
            print("Checking Network speed...")
            speak("Checking Network speed")
            time.sleep(2)
            print("This may take a while...")
            speed_test()

        elif "let's play stone paper scissor" in x or "play stone paper scissor" in x:
            s=["stone", "paper", "scissor"]
            y=random.choice(s)
            stone_paper_scissor()

        elif "play" in x:
            song = x.replace('play', '')
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif "send a whatsapp message" in x or "send message" in x or "send whatsapp message" in x:
            x=str(input("Enter the name of the person: "))
            pyautogui.hotkey('win')
            pyautogui.typewrite('whatsapp')
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.typewrite(x)
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(1)
            pyautogui.press('enter')
            speak("What do you want to send?")
            msg = get_audio()
            pyautogui.typewrite(msg)
            time.sleep(1)
            pyautogui.press('enter')
            speak("Message sent")

        elif "summarize text for me" in x or "summarize text" in x:
            print("Enter the text to summarize: ")
            speak("Enter the text to summarize: ")
            text = str(input())
            response = chat.send_message("Summarize this text: " + text)
            cleaned_data = re.sub(r'\* ', '', response.text)
            print(cleaned_data)
            speak(cleaned_data)

        else:
            r = tr.process_input(x)
            response = chat.send_message(r)
            cleaned_data = re.sub(r'\* ', '', response.text)
            print(cleaned_data)
            if len(cleaned_data) < 500:
                speak(cleaned_data)

        print("------------------------------------------------------------------------")

        print("Press enter to speak")
        t=input()
        if t=='':
            continue

if __name__ == '__main__':

    greetMe()

    battery_thread = threading.Thread(target = bat.battery)
    battery_thread.start()

    bat.check_battery()

    main()

#code ends!

