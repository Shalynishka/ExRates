import pickle
from back.currency import Currency
from back.crypt import Crypt
from back.resource import Resource
from datetime import datetime
import requests
import os

# good = [23, 27, 68, 72, 74, 77, 119, 130, 143, 145, 170, 184, 191, 232, 286, 290, 291, 292, 293, 294, 295, 296, 297,
#         298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319,
#         320, 321,323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342,
#         343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353]
NAMES = 'CAD', 'SGD', 'CHF', 'GBP', 'USD', 'AUD', 'BGN', 'UAH', 'DKK', 'EUR', 'PLN', 'RUB', 'KZT', 'TRY', 'CZK', 'SEK'
CRYPTS = {'BTC': 'Bitcoin', 'ETH': 'Ethereum', 'LTC': 'Litecoin', 'BCH': 'Bitcoin Cash', 'EOS': 'EOS'}


class Controller:
    """
    Class Controller
    It contains general methods to work with currencies and resources
    Methods:
        staticmethod:
            show_info(i)        - return dict with information about i
            clear(file)         - clear file, that contains stores info about Items
            store(file, items)  - store info about items in file
            load(file)          - return list of info of items from file
    """

    """return info about item"""
    @staticmethod
    def show_info(i) -> dict:
        return i.__dict__()

    """clear required file"""
    @staticmethod
    def clear(file: str):
        try:
            os.remove(file)
        except FileNotFoundError:
            return
        # f.truncate()
        # f.close()

    """store list of items in required file"""
    @staticmethod
    def store(file: str, items: list):
        with open(file, 'wb') as f:
            for i in items:
                pickle.dump(i.__dict__(), f)

    """load and return list of info of items in required file"""
    @staticmethod
    def load(file: str):
        lt = []
        try:
            with open(file, 'rb') as f:
                    while True:
                        try:
                            lt.append(pickle.load(f))
                        except EOFError:
                            break
        except FileNotFoundError:
            return []
        else:
            return lt


class CurController(Controller):
    """
    Class CurController, child of Controller
    It contains methods to work with currencies
    Attributes:
        __cur       - list of Currency
        __fav_cur   - list of favorites Currency
    Methods:
        __init__ - load info
        find_cur(name) - find currencies withs required name and return list of currencies
        update_cur()   - update and store cur
        del_fav(f)     - delete f from favorites
    Properties:
        cur -> __cur - setter and getter~
        fav -> __fav - setter and getter~
    """

    __cur = []
    __fav_cur = []

    def __init__(self):
        for i in self.load('cur.txt'):
            self.cur = Currency(**i)
            if i['fav']:
                self.fav = self.cur[-1]

    """list of currency"""
    @property
    def cur(self):
        return self.__cur

    @cur.setter
    def cur(self, c):
        self.__cur.append(c)

    """list of favorite currencies"""
    @property
    def fav(self):
        return self.__fav_cur

    @fav.setter
    def fav(self, f):
        self.__fav_cur.append(f)

    """delete from favorites"""
    def del_fav(self, short):   # todo возможно добавить обработку исключения отсутствия индекса. Возможно.
        shorts = [r.short for r in self.fav]
        self.__fav_cur.pop(shorts.index(short))

    """
    update all currency + create file with them
    fresh file!
    """
    def update_cur(self):
        cr = []
        fv = []
        date = datetime.date(datetime.now())
        i = -1
        for c in NAMES:
            i += 1
            try:
                r = requests.get('http://www.nbrb.by/API/ExRates/Rates/{}?ParamMode=2'.format(c)).json()
                rate = [r['Cur_Scale'], r['Cur_OfficialRate']]
                d = requests.get('http://www.nbrb.by/API/ExRates/Currencies/' + str(r['Cur_ID'])).json()
                # функция для замены файла курсов. Все данные берутся из кортежа. (на случай, если файл затеряется)
                # именно поэтому тут такое шаманство
                cr.append(Currency(name=d['Cur_Name_Eng'], short=d['Cur_Abbreviation'], rate=rate,
                                   date=date, symbol=chr(164), fav=self.cur[i].fav_s if self.fav else False))
                if self.cur and self.cur[i].fav_s:
                    fv.append(cr[-1])
            except:
                continue
        self.__cur = cr
        self.__fav_cur = fv
        self.clear('cur.txt')
        self.store('cur.txt', self.cur)

    """find currency"""
    @staticmethod
    def find_cur(name: str) -> list:
        cur = []
        date = datetime.date(datetime.now())
        for line in open('cur_names.txt', 'r'):
            if name in line:
                try:
                    r = requests.get('http://www.nbrb.by/API/ExRates/Rates/{}?ParamMode=2'.format(line[-4:-1])).json()
                    rate = [r['Cur_Scale'], r['Cur_OfficialRate']]
                    d = requests.get('http://www.nbrb.by/API/ExRates/Currencies/' + str(r['Cur_ID'])).json()

                    cur.append(Currency(name=d['Cur_Name_Eng'], short=d['Cur_Abbreviation'], rate=rate,
                                        date=date, symbol=chr(164), fav=False))
                except:
                    continue
        return cur


class ResController(Controller):
    """
    Class ResController, child of Controller
    It contains methods to work with resources
    Attributes:
        __res       - list of Resource
    Methods:
        __init__ - load info                    # todo add update?
        update_res()   - пусть берет всех и обновляет, перезаписывает файл и обновляет внутренние списки #todo
    Properties:
        res -> __res - setter and getter~
        """
    __res = []

    def __init__(self):
        for i in self.load('res.txt'):
            self.res = Resource(**i)

    @property
    def res(self):
        return self.__res

    @res.setter
    def res(self, r):
        self.__res.append(r)

    def update_res(self):
        try:
            r = []
            date = datetime.date(datetime.today())
            names = requests.get('http://www.nbrb.by/API/Metals').json()
            data = requests.get('http://www.nbrb.by/API/Ingots/Prices/?onDate=' + str(date)).json()
            for i in range(3):
                for d in data:
                    if d['MetalID'] == i and d['Nominal'] == 100.0:
                        rate = d['CertificateRubles']
                r.append(Resource(name=names[i]['NameEng'], short=str(i), date=date, rate=rate))
        except:
            return
        self.__res = r
        self.clear('res.txt')
        self.store('res.txt', self.res)


class CryptController(Controller):
    """
    Class CryptController, child of Controller
    It contains methods to work with crypts
    Attributes:
        __crypt - list of Crypt
    Methods:
        __init__ - load info                    # todo add update?
        update_crypt() - пусть берет всех и обновляет, перезаписывает файл и обновляет внутренние списки #todo
    Properties:
        crypt -> __crypt - setter and getter~
    """
    __crypt = []

    def __init__(self):
        for i in self.load('crypt.txt'):
            self.crypt = Crypt(**i)

    @property
    def crypt(self):
        return self.__crypt

    @crypt.setter
    def crypt(self, cr):
        self.__crypt.append(cr)

    def update_crypt(self):
        try:
            crypts = []
            date = datetime.date(datetime.today())
            for d in CRYPTS:
                cr = requests.get('https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD'.format(d)).json()
                crypts.append(Resource(name=CRYPTS[d], short=d, date=date, rate=cr['USD']))
        except:
            return
        self.__crypt = crypts
        self.clear('crypt.txt')
        self.store('crypt.txt', self.crypt)
