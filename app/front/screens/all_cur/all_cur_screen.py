from kivy.uix.screenmanager import Screen


# todo окошко на момент загрузки


class AllCur(Screen):
    controller = None

    def __init__(self, **kw):
        super().__init__(**kw)

    def refresh(self):
        self.controller()
