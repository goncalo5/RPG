# kivy:
from kivy.app import App
# kivy - uix:
from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    pass


class GameApp(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    GameApp().run()