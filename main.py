import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from  kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.lang import Builder
from  kivy.core.image import Image, Texture
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.factory import Factory

class MyFloat(FloatLayout):
    count1 = 40
    count2 = 40
    count3 = 40
    count4 = 40
    my_text1 = StringProperty("40")
    my_text2 = StringProperty("40")
    my_text3 = StringProperty("40")
    my_text4 = StringProperty("40")
    
    def on_button_click1(self):
        self.count1 += 1
        self.my_text1 = str(self.count1)
    
    def on_button_click2(self):
        self.count1 -= 1
        self.my_text1 = str(self.count1)

    def on_button_click3(self):
        self.count2 += 1
        self.my_text2 = str(self.count2)
    
    def on_button_click4(self):
        self.count2 -= 1
        self.my_text2 = str(self.count2)
    
    def on_button_click5(self):
        self.count3 += 1
        self.my_text3 = str(self.count3)
    
    def on_button_click6(self):
        self.count3 -= 1
        self.my_text3 = str(self.count3)
    
    def on_button_click7(self):
        self.count4 += 1
        self.my_text4 = str(self.count4)
    
    def on_button_click8(self):
        self.count4 -= 1
        self.my_text4 = str(self.count4)

    def reset(self):
        self.count1 = 40
        self.my_text1 = str(self.count1)
        self.count2 = 40
        self.my_text2 = str(self.count2)
        self.count3 = 40
        self.my_text3 = str(self.count3)
        self.count4 = 40
        self.my_text4 = str(self.count4)

    
class My1App(App):
    def build(self):
        return MyFloat()

if __name__== "__main__":
    My1App().run()
    
"""    player1 = ObjectProperty(None)
player2 = ObjectProperty(None)
player3 = ObjectProperty(None)
player4 = ObjectProperty(None)

def btn(self):
    print("Name:" , self.name.text , "email: ", self.email.text)"""
