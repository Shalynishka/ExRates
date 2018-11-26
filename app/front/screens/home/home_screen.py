from kivy.uix.screenmanager import Screen


# todo передавать сюда виджет для удаления. Либо его имя.
class Home(Screen):
    # fav = {}
    controller = None

    def __init__(self, **kw):

        super().__init__(**kw)

    def refresh(self):
        self.controller()
