from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

import paths


class ReduceItem:

    def __init__(self, short):
        self.short = short

    def build(self, func):

        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None))
        root.size_y = '100dp'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)
        b0 = BoxLayout()
        a1 = AnchorLayout(size_hint=(1, 1))
        # короткое имя
        btn = Button(size_hint=(1, 1), text='Add ' + self.short, on_press=func, id=self.short)
        a1.add_widget(btn)

        # содержит картинку
        a2 = AnchorLayout(anchor_x='right', anchor_y='center')
        i1 = Image(size_hint=(None, None), source=paths.images + 'flags/{}.png'.format(self.short))
        i1.width = '60dp'
        i1.height = '60dp'
        a2.add_widget(i1)
        b0.add_widget(a1)
        b0.add_widget(a2)

        root.add_widget(b0)

        return root
