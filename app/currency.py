from item import Item


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

        """
    __symbol = ''
    __fav_status = False

    # (self, name: str, short: str, icon, rate: float, date: datetime.date, symbol: str, fav: bool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__symbol = kwargs['symbol']
        self.__fav_status = kwargs['fav']

    """AKA get info"""
    def __dict__(self) -> dict:
        return {'name': self.name,
                'short': self.short,
                'rate': self.rate,
                'date': self.date,
                'symbol': self.symbol,
                'fav': self.fav_s}

    """symbol of currency"""
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, s):
        self.__symbol = s

    """favorite status"""
    @property
    def fav_s(self):
        return self.__fav_status

    @fav_s.setter
    def fav_s(self, f):
        self.__fav_status = f
