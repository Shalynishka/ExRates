from kivy.uix.boxlayout import BoxLayout
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
        root.size_y = '100dp'
        with root.canvas:
            Color(.88, .88, .88)
            Rectangle(pos=root.pos, size=root.size)

        b = BoxLayout(size_hint=(1, 1))
        ai = BoxLayout()
        i1 = Image(size_hint=(None, None), source=paths.images + 'flags/{}.png'.format(self.item.short))
        ai.add_widget(i1)
        i1.width = '90dp'
        i1.height = '90dp'

        b.add_widget(ai)

        g = BoxLayout(spacing='30dp', orientation='vertical')

        a1 = AnchorLayout()
        l1 = Label(color=(0, 0, 0, 1),
                   font_size='20dp',
                   text=(self.item.short + ' ' + str(self.item.rate[0]) + ' ' +
                         self.item.symbol + ' – ' + '{0:.2f}'.format(self.item.rate[1]) + ' Br'))
        a1.add_widget(l1)

        a2 = AnchorLayout()
        l2 = Label(color=(0, 0, 0, 1), font_size='20dp', text=self.item.name)
        a2.add_widget(l2)

        g.add_widget(a1)
        g.add_widget(a2)
        b.add_widget(g)

        root.star = Button(size_hint=(None, None))
        root.star.width = '80dp'
        root.star.height = '80dp'

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

        a3 = AnchorLayout(anchor_x='center')
        l3 = Label(size_hint=(None, .1), text=str(self.item.date), color=(0, 0, 0, 1))
        a3.add_widget(l3)
        g.add_widget(a3)

        return root

    def fav(self):
        self.change_fav(self.item, self.star)
