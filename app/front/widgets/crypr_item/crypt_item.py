from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

import paths


class CryptItem:

    def __init__(self, i):
        self.item = i

    def build(self):
        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None))
        root.size_y = '100dp'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        b = BoxLayout(size_hint=(1, 1))
        ai = BoxLayout(size_hint=(.3, 1))
        i1 = Image(size_hint=(None, None), source=paths.images + 'crypts/{}.svg'.format(self.item.short))
        i1.width = '60dp'
        i1.height = '60dp'
        ai.add_widget(i1)

        b.add_widget(ai)

        g1 = BoxLayout(spacing='40dp', padding='40dp')

        # полное имя
        a1 = AnchorLayout(anchor_x='left', anchor_y='center', padding='10dp')
        l1 = Label(size_hint=(None, None), color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        l1.valign = 'middle'
        l1.halign = 'left'
        a1.add_widget(l1)
        # цена
        a3 = AnchorLayout(anchor_x='right', anchor_y='center', padding='10dp')
        l3 = Label(size_hint=(None, None), color=(0, 0, 0, 1), font_size='20dp',
                   text='{0:.2f}'.format(self.item.rate) + '$')
        l3.valign = 'middle'
        l3.halign = 'right'
        a3.add_widget(l3)

        g1.add_widget(a1)
        g1.add_widget(a3)

        g2 = BoxLayout(spacing='40dp', padding='40dp')
        # короткое имя
        a2 = AnchorLayout(anchor_x='left', anchor_y='center', padding='10dp')
        l2 = Label(size_hint=(None, None), color=(0, 0, 0, 1), font_size='20dp', text=self.item.short)
        l2.valign = 'middle'
        l2.halign = 'left'
        a2.add_widget(l2)
        g2.add_widget(a2)

        a4 = AnchorLayout(anchor_x='right', anchor_y='center', padding='10dp')
        l4 = Label(size_hint=(None, None), text=str(self.item.date), color=(0, 0, 0, 1))
        l4.valign = 'middle'
        l4.halign = 'left'
        a4.add_widget(l4)
        g2.add_widget(a4)

        b0 = BoxLayout(spacing='40dp', orientation='vertical')

        b0.add_widget(g1)
        b0.add_widget(g2)
        b.add_widget(b0)
        root.add_widget(b)

        return root




















