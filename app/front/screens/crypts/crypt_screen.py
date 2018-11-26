from front.widgets.crypr_item.crypt_item import CryptItem
from kivy.uix.screenmanager import Screen


class Crypts(Screen):
    c = None

    @property
    def controller(self):
        return self.c

    @controller.setter
    def controller(self, c):
        self.c = c

    def load(self):
        for i in self.controller.crypt.values():
            try:
                self.ids['items'].add_widget(CryptItem(i).build())
            except Exception as e:
                print(e)

    def refresh(self):
        while self.ids['items'].children:
            self.ids['items'].remove_widget(self.ids['items'].children[0])
        self.c.update_crypt()
        self.load()
        print('what')
