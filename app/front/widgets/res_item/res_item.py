from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle

import paths


class ResItem:

    def __init__(self, i):
        self.item = i

    def build(self):
        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None))
        root.size_y = '100dp'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        b = BoxLayout(size_hint=(1, .9))
        i1 = Image(size_hint=(None, None), source=paths.images + 'res/{}.svg'.format(self.item.name))   # todo crypt icons
        i1.width = '55dp'
        i1.height = '55dp'

        b.add_widget(i1)

        # полное имя и цена
        a1 = AnchorLayout()
        l1 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        a1.add_widget(l1)

        # короткое имя
        a2 = AnchorLayout()
        l2 = Label(color=(0, 0, 0, 1), font_size='20dp', text='{0:.2f}'.format(self.item.rate) + '$')
        a2.add_widget(l2)

        b1 = BoxLayout(spacing='30dp', padding='20dp')
        b1.add_widget(a1)
        b1.add_widget(a2)

        a3 = AnchorLayout()
        l3 = Label(color=(0, 0, 0, 1), font_size='20dp', text='price for 100 gr')
        a3.add_widget(l3)

        a4 = AnchorLayout(size_hint=(1, .19), anchor_x='right')
        l4 = Label(size_hint=(None, None), text=str(self.item.date), color=(0, 0, 0, 1))
        a4.add_widget(l4)

        b2 = BoxLayout(spacing='30dp', padding='20dp')
        b2.add_widget(a3)
        b2.add_widget(a4)

        g0 = GridLayout(spacing='30dp', padding='20dp', rows=2)
        g0.add_widget(b1)
        g0.add_widget(b2)
        ####

        b.add_widget(g0)
        root.add_widget(b)

        return root
