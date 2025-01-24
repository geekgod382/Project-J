import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get and print available voices
voices = engine.getProperty('voices')

'''You can change Cypher's voice by changing the index of the voices array'''

for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender}")
    print(f" - Age: {voice.age}")
    print()