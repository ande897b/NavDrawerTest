from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.garden.navigationdrawer import NavigationDrawer as ND


class NavDemoWindow(ND):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NavDemoApp(App):
    def build(self):

        return NavDemoWindow()


if __name__ == '__main__':
    NavDemoApp().run()
