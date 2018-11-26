from kivy.uix.screenmanager import Screen
from front.widgets.reduce_item.reduce_item import ReduceItem
from back.controllers import NAMES


# добавление
class ConvertMenu(Screen):

    def load(self, add):
        for name in NAMES.keys():
            self.ids['items'].add_widget(ReduceItem(name).build(add))

    # def add(self, *arg):
    #     print('hello', arg[0].id)

