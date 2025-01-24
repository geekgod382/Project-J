# stone paper scissor game

import random
from com import speak, get_audio

s=["stone", "paper", "scissor"]
y=random.choice(s)

def stone_paper_scissor():
    '''A game for timepass'''
    
    while(1):
        speak("What would you choose? ")
        c=get_audio()
        print("Your choice: ", c)

        if "paper" in c or "scissor" in c or "stone" in c:
            print("My choice: ", y)
            speak("My choice:")
            speak(y)
            if (y=="stone" and ("paper" in c)) or (y=="paper" and ("scissor" in c)) or (y=="scissor" and ("stone" in c)):
                print("You won!")
                speak("You won!")
            elif y==c:
                print("It's a draw!")
                speak("It's a draw!")
            else:
                print("Oh, You lost!")
                speak("Oh, You lost!")
        else:
            speak("Please enter a valid choice")
            continue

        speak("Want to play more?")
        q = get_audio()
        if q=="yes":
            continue
        else:
            print("Ok")
            break

# stone_paper_scissor()