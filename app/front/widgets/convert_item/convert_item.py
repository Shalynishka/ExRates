from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

import paths


# todo дергать здесь конвертер
class LimInput(TextInput):
    def keyboard_on_key_down(self, window, key, text, modifiers):
        TextInput.keyboard_on_key_down(self, window, key, text, modifiers)
        if key[1] == "backspace":
            self.make_convert(self.id, '')

    def insert_text(self, substring, from_undo=False):
        if substring.isdigit():
            self.make_convert(self.id, substring)
        else:
            if substring != '.':
                substring = ''
        return super(LimInput, self).insert_text(substring, from_undo=from_undo)


class ConvertItem:

    def __init__(self, i):
        self.item = i

    def build(self, convert):
        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None), id='root')
        # root.id = self.item.short
        root.size_y = '100dp'
        # root.item_property = 'image'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        # содержит картинку
        b0 = BoxLayout(size_hint=(1, 1), id='box_root')
        i1 = Image(size_hint=(.3, 1), source=paths.images + 'flags/{}.svg'.format(self.item.short))
        i1.width = '60dp'
        i1.height = '60dp'

        b0.add_widget(i1)

        # содержит ввод и корткое имя
        b1 = BoxLayout(id='box_input')
        # короткое имя
        a1 = AnchorLayout()
        l1 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.short)
        a1.add_widget(l1)

        b1.add_widget(a1)

        # ввод
        a_inp = AnchorLayout(id='anchor_input')
        inp = LimInput(id=self.item.short)
        inp.make_convert = convert
        a_inp.add_widget(inp)
        b1.add_widget(a_inp)

        b0.add_widget(b1)
        root.add_widget(b0)
        # # содержит b1 и полное имя
        # b2 = BoxLayout(orientation='vertical')

        # полное имя
        a2 = AnchorLayout(size_hint=(1, 1), anchor_x='center')

        l2 = Label(size_hint=(None, None), color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        a2.add_widget(l2)

        # b2.add_widget(b1)
        # b2.add_widget(a2)

        root.add_widget(a2)
        # root.add_widget(b2)

        root.input = inp

        return root




















