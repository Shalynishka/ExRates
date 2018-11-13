from Item import Item
from datetime import datetime


class Currency(Item):
    """
        Class for Currency. It contains Currency information.
        Child from Item

        Attributes:
            __symbol - symbol of Currency
            __fav    - 'favorite' status

        Methods and properties:

            __init__(self, name, s_n, icon, rate, date, s, f)
            __dict__(self) - return all info in dict

            properties(getter~+setter):
                symbol
                fav

            todo: Load and Store info
        """
    __symbol = ''
    __fav = False

    def __init__(self,  name: str, s_n: str, icon, rate: float, date: datetime.date, s: str, f: bool):
        super().__init__(name, s_n, icon, rate, date)
        self.__symbol = s
        self.__fav = f

    """symbol of currency"""
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, s):
        self.__symbol = s

    """favorite status"""
    @property
    def fav(self):
        return self.__symbol

    @fav.setter
    def fav(self, f):
        self.__fav = f

    """AKA get info"""
    def __dict__(self) -> dict:
        return {'name': self.name,
                'short': self.s_name,
                'rate': self.rate,
                'date': self.date,
                'symbol': self.symbol,
                'fav': self.fav}


c = Currency('name12', 'sn', 'Icon1', .23, datetime.date(datetime.now()), 'A', False)

print(c.__dict__())



