import random
import json
from googleapiclient.discovery import build

class Translator:
    def __init__(self):
        self.service = build('translate', 'v2', developerKey='AIzaSyDGab9TFvh6-bY059FkuLxjGLKn8IkOQXw')

    def translate(self, text, language):
        return json.loads(self.service.translations().list(target=language, q=text))['data']['translations'][0]["translatedText"]

    def randomLanguage(self):
        return random.choice(list(self.service.languages().list()['data']['languages'].keys()))

    def computeTranslation(self, text):
        amount = 1
        newtext = ''
        for i in range(0, amount):
            newtext = self.translate(self.translate(text, self.randomLanguage()), 'en')

        return newtext







