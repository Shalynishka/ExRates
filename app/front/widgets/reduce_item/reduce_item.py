from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

import paths


class ReduceItem:

    def __init__(self, short):
        self.short = short

    def build(self, func):

        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None))
        # root.id = self.item.short
        root.size_y = '100dp'
        # root.item_property = 'image'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)
        b0 = BoxLayout()
        a1 = AnchorLayout(size_hint=(.7, 1), anchor_x='left', anchor_y='center')
        # короткое имя
        l1 = Label(size_hint=(None, None), color=(0, 0, 0, 1), font_size='20dp', text=self.short)
        a1.add_widget(l1)

        # содержит картинку
        a2 = AnchorLayout(anchor_x='right', anchor_y='center')
        i1 = Image(size_hint=(None, None), source=paths.images + 'flags/{}.svg'.format(self.short))
        # i1.width = '60dp'
        # i1.height = '60dp'
        a2.add_widget(i1)
        b0.add_widget(a1)
        b0.add_widget(a2)

        btn = Button(text='Add', on_press=func, color=(0, 0, 0, 1), background_color=(0, 0, 0, 0), id=self.short)
        root.add_widget(b0)
        root.add_widget(btn)

        return root
