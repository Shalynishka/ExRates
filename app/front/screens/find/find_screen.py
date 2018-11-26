from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from front.widgets.full_item.full_item import FullItem


class Find(Screen):
    search = ObjectProperty()

    c = None
    change_fav = None
    r = None

    def load(self, controller, change_fav, refresh):
        self.c = controller
        self.change_fav = change_fav
        self.r = refresh

    def find(self):
        self.remove_w()
        for value in self.c.find_cur(self.search.text).values():
            self.add_w(self.c.cur[value.short])

    def remove_w(self):
        while self.ids['items'].children:
            self.ids['items'].remove_widget(self.ids['items'].children[0])

    def add_w(self, item):
        fi1 = FullItem(item, self.change_fav).build()
        self.ids['items'].add_widget(fi1)

    def refresh(self):
        self.r()
        self.find()
