from kivy.uix.screenmanager import Screen


class Home(Screen):
    controller = None

    def __init__(self, **kw):

        super().__init__(**kw)

    def refresh(self):
        self.controller()
