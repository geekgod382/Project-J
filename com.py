import pyttsx3
import speech_recognition as sr
import json

recognizer = sr.Recognizer()

def get_audio():
    
    '''This function listens to the user's voice and returns the text'''

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_ = recognizer.listen(source)
    try:
        response_text = recognizer.recognize_google(audio_, show_all=True) 
        # print(f"Raw Response: {response_text}")
        
        if "alternative" in response_text and len(response_text["alternative"])>0:
            command = response_text['alternative'][0]['transcript']
            print(f"You said: {command}")
            return command.lower()
        else:
            print("Unexpected response format or empty response")
   
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return get_audio()
    
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
    
    except json.JSONDecodeError as e:
        print(f"json decode error", {e})

# preparing system to speak
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    
    '''This function speaks the text passed to it'''

    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass