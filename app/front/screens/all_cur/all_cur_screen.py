from kivy.uix.screenmanager import Screen


# todo окошко на момент загрузки


class AllCur(Screen):
    # c = None
    # h = None
    # fav = {}

    def __init__(self, **kw):
        super().__init__(**kw)

    # def load(self, *, controller, home):
    #     self.c = controller
    #     self.h = home
    #     for i in self.c.cur.values():
    #         try:
    #             fi = FullItem(i, self.change_fav).build()
    #             if i.fav_s:
    #                 self.fav[i.short] = fi
    #             self.ids['items'].add_widget(FullItem(i, self.h).build())
    #         except:
    #             continue
    #
    # def refresh(self):
    #     while self.ids['items'].children:
    #         self.ids['items'].remove_widget(self.ids['items'].children[0])
    #     self.c.update_cur()
    #     self.load()
    #     print('refresh')
    #
    # def change_fav(self, item):
    #     if item.fav_s:
    #         self.controller.cur[item.short].fav_s = True
    #         self.controller.fav[item.short] = item
    #         self.add_fav(item)
    #
    #     else:
    #         self.c.cur[item.short].fav_s = False
    #         self.c.fav.pop(item.short)
    #         self.del_fav(item.short)
    #
    # def del_fav(self, short):
    #     self.ids['items'].remove_widget(self.fav[short])
    #
    # def add_fav(self, item):
    #     self.fav[item.short] = FullItem(item, self.change_fav).build()
    #     self.ids['items'].add_widget(self.fav[item.short])
