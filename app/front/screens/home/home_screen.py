from kivy.uix.screenmanager import Screen


# todo передавать сюда виджет для удаления. Либо его имя.
class Home(Screen):
    # fav = {}

    def __init__(self, **kw):

        super().__init__(**kw)

    # def load(self, *, controller):
    #     self.c = controller
    #     for i in self.c.fav.values():
    #         try:
    #             self.fav[i.short] = FullItem(i, self.change_fav).build()
    #             self.ids['items'].add_widget(self.fav[i.short])
    #         except:
    #             continue
    #
    # def refresh(self):
    #     self.remove_widgets()
    #     self.c.update_cur()
    #     self.load()
    #     print('refresh')
    #
    # def change_fav(self, item):
    #     if item.fav_s:
    #         self.c.cur[item.short].fav_s = True
    #         self.c.fav[item.short] = item
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
    #
    # def remove_widgets(self):
    #     while self.ids['items'].children:
    #         self.ids['items'].remove_widget(self.ids['items'].children[0])


# todo суть идеи: добавление всех виджетов в словарь fav. И потом от туда их дергать и через них удалять с grid-а
