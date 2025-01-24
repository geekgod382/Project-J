from googletrans import Translator
from langdetect import detect

translator = Translator()

class trnslte():
    '''This class is used to translate the audio input from user to English'''

    def __init__(self):
        pass

    def detect_language(self, text):
        return detect(text)

    # Function to translate text to a target language
    def translate_text(self, text, target_lang):
        translated = translator.translate(text, dest=target_lang)
        return translated.text

    # Function to process user input and generate response
    def process_input(self, user_input):
        user_lang = self.detect_language(user_input)
        if user_lang != 'en':
            user_input_translated = self.translate_text(user_input, 'en')
        else:
            user_input_translated = user_input
        
        return user_input_translated
