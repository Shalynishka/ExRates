from back.item import Item


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

    """

    symbol = ''     # currency symbol
    fav_s = False   # favorite status

    # (self, name: str, short: str, icon, rate: float, date: datetime.date, symbol: str, fav: bool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__symbol = kwargs['symbol']
        self.__fav_status = kwargs['fav']

    def __dict__(self) -> dict:
        """get info"""

        return {'name': self.name,
                'short': self.short,
                'rate': self.rate,
                'date': self.date,
                'symbol': self.symbol,
                'fav': self.fav_s}

    def __str__(self):
        return self.short + ' 1 ' + self.symbol + ' ' + str(self.rate) + ' Br'
