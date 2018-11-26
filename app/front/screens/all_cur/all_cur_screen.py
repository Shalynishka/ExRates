from kivy.uix.screenmanager import Screen


# todo окошко на момент загрузки


class AllCur(Screen):
    # c = None
    # h = None
    # fav = {}
    controller = None

    def __init__(self, **kw):
        super().__init__(**kw)

    def refresh(self):
        self.controller()
