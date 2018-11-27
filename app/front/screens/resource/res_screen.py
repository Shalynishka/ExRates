from front.widgets.res_item.res_item import ResItem
from kivy.uix.screenmanager import Screen


class Res(Screen):
    c = None

    @property
    def controller(self):
        return self.c

    @controller.setter
    def controller(self, c):
        self.c = c

    def load(self):
        for i in self.controller.res.values():
            try:
                self.ids['items'].add_widget(ResItem(i).build())
            except Exception as e:
                print(e)

    def refresh(self):
        while self.ids['items'].children:
            self.ids['items'].remove_widget(self.ids['items'].children[0])
        self.c.update_res()
        self.load()
