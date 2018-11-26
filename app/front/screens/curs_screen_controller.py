from front.widgets.full_item.full_item import FullItem

import paths


class CursScreenController:
    fav = {}
    cur = {}
    controller = None

    def __init__(self, h, a, c):
        self.home = h   # экраны с виджетами валют
        self.all = a
        self.controller = c

    def load(self):
        for i in self.controller.cur.values():
            try:
                fi0 = FullItem(i, self.change_fav).build()
                self.cur[i.short] = fi0
                self.all.ids['items'].add_widget(fi0)
                if i.fav_s:
                    fi1 = FullItem(i, self.change_fav).build()
                    self.fav[i.short] = fi1
                    self.home.ids['items'].add_widget(fi1)
            except:
                continue

    """refresh"""
    def refresh(self):
        while self.home.ids['items'].children:
            self.home.ids['items'].remove_widget(self.home.ids['items'].children[0])

        while self.all.ids['items'].children:
            self.all.ids['items'].remove_widget(self.all.ids['items'].children[0])

        self.controller.update_cur()
        self.load()

    def change_fav(self, item, widget):
        if not item.fav_s:
            self.controller.cur[item.short].fav_s = True
            self.controller.fav[item.short] = item          # todo в общем листе данный item должен изменить свой статус. А потом это сохранять
            widget.background_normal = paths.images + 'appIcons/starT.png'
            self.cur[item.short].star.background_normal = paths.images + 'appIcons/starT.png'
            self.add_fav(item)
        else:
            self.controller.cur[item.short].fav_s = False
            self.controller.fav.pop(item.short)
            self.del_fav(item.short)
            widget.background_normal = paths.images + 'appIcons/star.png'
            self.cur[item.short].star.background_normal = paths.images + 'appIcons/star.png'
            # widget.background_normal = 'images\\appIcons\\star.png'

    def del_fav(self, short):
        self.home.ids['items'].remove_widget(self.fav[short])
        self.fav[short].star.background_normal = paths.images + 'appIcons/star.png'

        self.fav.pop(short)

    def add_fav(self, item):
        fi1 = FullItem(item, self.change_fav).build()
        self.home.ids['items'].add_widget(fi1)
        self.fav[item.short] = fi1
        # widget.background_normal = 'images\\appIcons\\starT.png'
