from Item import Item
from datetime import datetime


class Crypt(Item):
    """
        Class for Crypto-currency. It contains Crypto-currency information.
        Child from Item

        Attributes:

        Methods and properties:

            __init__(self, name, s_n, icon, rate, date, s, f)
            __dict__(self) - return all info in dict

            todo: Load and Store info
        """

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

    """AKA get info"""
    def __dict__(self) -> dict:
        return {'name': self.name,
                'short': self.s_name,
                'rate': self.rate,
                'date': self.date}


c = Crypt('name12', 'sn', 'Icon1', .23, datetime.date(datetime.now()), 'A', False)

print(c.__dict__())



