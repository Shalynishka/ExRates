from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle

import paths


class FullItem:
    star = None
    
    def __init__(self, i, fav):
        self.item = i
        self.change_fav = fav

    def build(self):
        root = BoxLayout(orientation='vertical', padding='5dp', size_hint=(1, None))
        # root.id = self.item.short
        root.size_y = '100dp'
        # root.item_property = 'image'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        b = BoxLayout(size_hint=(1, .9))
        i1 = Image(size_hint=(.2, 1), source=paths.images + 'flags/{}.svg'.format(self.item.short))
        i1.width = '40dp'
        i1.height = '40dp'
        # i1.y = b.y + 100
        # i1.x = b.x + 100

        b.add_widget(i1)

        g = GridLayout(spacing='30dp', padding='20dp', rows=2)

        a1 = AnchorLayout()
        l1 = Label(color=(0, 0, 0, 1),
                   font_size='20dp',
                   text=(self.item.short + ' ' + str(self.item.rate[0]) + ' ' +
                         self.item.symbol + ' – ' + str(self.item.rate[1]) + ' Br'))
        a1.add_widget(l1)

        a2 = AnchorLayout()
        l2 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        a2.add_widget(l2)

        g.add_widget(a1)
        g.add_widget(a2)
        b.add_widget(g)

        root.star = Button(size_hint=(None, None))
        root.star.width = '50dp'
        root.star.height = '50dp'

        root.star.on_press = self.fav
        # star.background_down = 'images\\appIcons\\star.png'
        if self.item.fav_s:
            s = paths.images + 'appIcons/starT.png'
        else:
            s = paths.images + 'appIcons/star.png'
        root.star.background_normal = s

        self.star = root.star
        b.add_widget(root.star)
        root.add_widget(b)

        a3 = AnchorLayout(size_hint=(1, .19), anchor_x='right')
        l3 = Label(size_hint=(None, None), text=str(self.item.date), color=(0, 0, 0, 1))
        a3.add_widget(l3)
        root.add_widget(a3)

        # l4 = Label(size_hint=(1, None), height='1dp')
        #
        # with l4.canvas:
        #     Color(0, 0, 0, 1)
        #     Rectangle(pos=root.pos, size=root.size)
        #
        # root.add_widget(l4)

        return root

    def fav(self):
        # if self.item.fav_s:
        #     self.item.fav_s = False
        #     self.star.background_normal = 'images\\appIcons\\star.png'
        # else:
        #     self.item.fav_s = True
        #     self.star.background_normal = 'images\\appIcons\\starT.png'

        self.change_fav(self.item, self.star)
