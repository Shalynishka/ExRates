from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from front.screens.curs_screen_controller import CursScreenController

from back.controllers import CurController, CryptController, ResController

import paths

from front.screens.find.find_screen import Find
from front.screens.menu.menu_screen import Menu
from front.screens.home.home_screen import Home
from front.screens.all_cur.all_cur_screen import AllCur
from front.screens.converter.converter_screen import Convert
from front.screens.crypts.crypt_screen import Crypts
from front.screens.resource.res_screen import Res
from front.screens.settings.settings_screen import Settings
from front.screens.converter_menu.converter_menu import ConvertMenu

from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 600)

cr_controller = CryptController()
cur_controller = CurController()
res_controller = ResController()

Builder.load_file(paths.screens + 'find/find.kv')
Builder.load_file(paths.screens + 'menu/menu.kv')
Builder.load_file(paths.screens + 'home/home.kv')

Builder.load_file(paths.screens + 'all_cur/all_cur.kv')
Builder.load_file(paths.screens + 'converter/converter.kv')
Builder.load_file(paths.screens + 'crypts/crypts.kv')
Builder.load_file(paths.screens + 'resource/res.kv')
Builder.load_file(paths.screens + 'settings/settings.kv')
Builder.load_file(paths.screens + 'converter_menu/converter_menu.kv')

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Menu(name='menu'))


"""CurScreenController"""
h = Home(name='home')
sm.add_widget(h)
a = AllCur(name='all')
sm.add_widget(a)

csc = CursScreenController(h, a, cur_controller)
csc.load()

crypts = Crypts(name='crypt')
crypts.controller = cr_controller
sm.add_widget(crypts)
crypts.load()

res = Res(name='res')
res.controller = res_controller
sm.add_widget(res)
res.load()

cv = Convert(name='convert')
sm.add_widget(cv)
cv.load(cur_controller)

cvm = ConvertMenu(name='converter_menu')
sm.add_widget(cvm)
cvm.load(cv.add)

f = Find(name='find')
f.load(cur_controller, csc.change_fav)
sm.add_widget(f)

sm.add_widget(Settings(name='settings'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()

