from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle

import paths


class CryptItem:

    def __init__(self, i):
        self.item = i

    def build(self):
        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None))
        # root.id = self.item.short
        root.size_y = '100dp'
        # root.item_property = 'image'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        b = BoxLayout(size_hint=(1, .9))
        i1 = Image(size_hint=(.3, 1), source=paths.images + 'crypts/{}.svg'.format(self.item.short))
        i1.width = '60dp'
        i1.height = '60dp'

        b.add_widget(i1)

        g1 = GridLayout(spacing='30dp', padding='20dp', rows=2)

        # полное имя
        a1 = AnchorLayout()
        l1 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        a1.add_widget(l1)

        # короткое имя
        a2 = AnchorLayout()
        l2 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.short)
        a2.add_widget(l2)

        g1.add_widget(a1)
        g1.add_widget(a2)
        b.add_widget(g1)

        ####
        g2 = GridLayout(spacing='30dp', padding='20dp', rows=2)

        a3 = AnchorLayout()
        l3 = Label(color=(0, 0, 0, 1), font_size='20dp', text=str(self.item.rate) + '$')
        a3.add_widget(l3)

        g2.add_widget(a3)

        a4 = AnchorLayout(size_hint=(1, .19), anchor_x='right')
        l4 = Label(size_hint=(None, None), text=str(self.item.date), color=(0, 0, 0, 1))
        a4.add_widget(l4)
        g2.add_widget(a4)
        b.add_widget(g2)
        # root.add_widget(a4)

        root.add_widget(b)
        # l4 = Label(size_hint=(1, None), height='1dp')
        #
        # with l4.canvas:
        #     Color(0, 0, 0, 1)
        #     Rectangle(pos=root.pos, size=root.size)
        #
        # root.add_widget(l4)

        return root




















