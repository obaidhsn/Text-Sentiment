from googletrans import Translator, LANGUAGES

class SentenceTranslator():
    def __init__(self) -> None:
        self.translator = Translator()

    def detect_and_translate(self, text):
        # Detect the language of the text
        try:
            detected_language = self.translator.detect(text).lang

            # Translate the text to English
            if detected_language != 'en':
                translation = self.translator.translate(text, src=detected_language, dest='en').text
            else:
                translation = text  # Text is already in English

            return translation
        except:
            return True, "Connection to Google API Failed. Please try again!"