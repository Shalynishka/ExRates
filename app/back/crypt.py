from back.item import Item


class Crypt(Item):
    """
        Class for Crypto-currency. It contains Crypto-currency information.
        Child from Item

        Attributes:

        Methods and properties:

            __init__(self, name, s_n, icon, rate, date, s, f)
            __dict__(self) - return all info in dict
    """

    # (self, name: str, s_n: str, icon, rate: float, date: datetime.date, s: str, f: bool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __dict__(self) -> dict:
        """get info"""

        return {'name': self.name,
                'short': self.short,
                'rate': self.rate,
                'date': self.date,
                'symbol': '$'}
