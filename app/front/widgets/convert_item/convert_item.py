from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

import paths


# todo дергать здесь конвертер
class LimInput(TextInput):
    def __init__(self, **kw):
        super().__init__(**kw)

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
        root.size_y = '100dp'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        # содержит картинку
        b0 = BoxLayout(id='box_root', padding='30dp', spacing='10dp')  # size_hint=(1, 1),
        ai = AnchorLayout(size_hint=(.3, 1))
        i1 = Image(size_hint=(None, None), source=paths.images + 'flags/{}.png'.format(self.item.short))
        i1.width = '60dp'
        i1.height = '60dp'

        ai.add_widget(i1)
        b0.add_widget(ai)

        # содержит ввод и корткое имя
        # короткое имя
        a1 = AnchorLayout(size_hint=(.1, 1))
        l1 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.short)
        a1.add_widget(l1)

        b0.add_widget(a1)

        # ввод
        a_inp = AnchorLayout(size_hint=(1, .8), id='anchor_input')
        inp = LimInput(size_hint=(1, None), id=self.item.short, write_tab=False, multiline=False)
        inp.height = '30dp'
        inp.make_convert = convert
        a_inp.add_widget(inp)
        b0.add_widget(a_inp)

        root.add_widget(b0)

        a2 = AnchorLayout(anchor_x='center', padding='30dp')

        l2 = Label(size_hint=(None, None), color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        a2.add_widget(l2)

        root.add_widget(a2)

        root.input = inp

        return root




















