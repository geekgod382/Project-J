from datetime import datetime
from com import speak

def greetMe():

    '''This function greets the user based on the time of the day'''

    hour  = int(datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morning,sir")
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        print("Good Afternoon ,sir")
        speak("Good Afternoon ,sir")

    else:
        print("Good Evening,sir")
        speak("Good Evening,sir")

    print("How can i assist you?")
    speak("how can i assist you?")

