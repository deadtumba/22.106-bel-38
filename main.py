from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from datetime import datetime
import time
import os

class MainScreen(Screen):
    def release(self):
        date = ""
        for file in os.listdir("./"):
            if file.endswith(".png"):
                if(date == ""):
                    date = file
                else:
                    if(file>date):
                        date = file
        if(date!=""):
            image = self.ids.image
            image.source = date

class CameraScreen(Screen):
    def screen_shot(self,):
        camera = self.ids.camera
        camera.export_to_png("./" + datetime.now().strftime("%Y%m%d%H%M%S%f") + ".png")

class ScreensManager(ScreenManager):
    def build(self):
        self.current = "Main screen"


class MainApp(App):
    def build(self):
        return ScreensManager.build(self)
        
if __name__=="__main__":
    MainApp().run()