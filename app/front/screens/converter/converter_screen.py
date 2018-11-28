from kivy.uix.screenmanager import Screen

from front.widgets.convert_item.convert_item import ConvertItem

from back.currency import Currency
from back.convertor import Converter

br = Currency(name='Belarusian ruble', short='BYN', rate=1, date=0, symbol='Br', fav=True)


class Convert(Screen):
    cv = Converter()
    c = None    # контроллер валют. Через него будем получать по короткому имени валюты
    curs = {}   # содержит виджеты, в них input, в которых менять текст

    def load(self, controller):
        self.c = controller
        item = ConvertItem(br).build(self.convert)
        self.curs['BYN'] = item
        self.ids['items'].add_widget(item)

    def add(self, short):
        if short.id not in self.curs.keys():
            item = ConvertItem(self.c.cur[short.id]).build(self.convert)
            self.curs[short.id] = item
            self.cv.rates = self.c.cur[short.id]
            self.ids['items'].add_widget(item)

    def convert(self, zero_name, addition):
        num = self.curs[zero_name].input.text + addition
        if num:
            for (name, value) in self.cv.convert(zero_name, float(num)).items():
                self.curs[name].input.text = '{0:.2f}'.format(value)
