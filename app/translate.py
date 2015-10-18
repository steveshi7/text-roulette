import random
import json
from googleapiclient.discovery import build

class Translator:
    def __init__(self):
        self.service = build('translate', 'v2', developerKey='AIzaSyAx-0NBm_CtePnMgvTC5KdZDTnf-C5-i3I')

    def translate(self, text, language):
        translation = self.service.translations().list(target=language, q=text).execute()
        return translation['translations'][0]["translatedText"]

    def randomLanguage(self):
        languages = self.service.languages().list().execute()['languages']
        return random.choice(languages)['language']

    def computeTranslation(self, text):
        amount = random.randint(5, 10)
        for i in range(0, amount):
            text = self.translate(text, self.randomLanguage())
            text = self.translate(text, 'en')
        return text







