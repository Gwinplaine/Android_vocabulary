from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
from datetime import datetime
from pathlib import Path
import random
from difflib import get_close_matches
Builder.load_file('design.kv')

class WelcomeScreen(Screen):
    def backback(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen_success"


class LoginScreenSuccess(Screen):
    def to_info(self):
        self.manager.transition.direction = "left"
        self.manager.current = "welcome_screen"    

    def get_description(self, word):
        word = word.lower()
        with open ('data.json') as file:
            data = json.load(file)
        if word in data:
            if type(data[word]) == list:
                lst = []
                for item in data[word]:
                    lst.append('- '+item)

                self.ids.match.text = '\n\n'.join(lst)
            else:
                self.ids.match.text= '- ' + data[word].title()
        else:
            self.ids.match.text = "The word doesn't exist. Please double check it."

    def get_russian(self, word2):
        word2 = word2.lower()
        with open ('final_russian_vocabulary.json') as file2:
            data2 = json.load(file2)
            if word2 in data2:
                self.ids.match_in_russian.text= data2[word2].title()
            else:
                self.ids.match_in_russian.text = "The word doesn't exist. Please double check it."

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()