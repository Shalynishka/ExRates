from item import Item


class Resource(Item):
    """
        Class for Resource. It contains Resource information.
        Child from Item

        Attributes:

        Methods and properties:

            __init__(self, name, s_n, icon, rate, date, s, f)
            __dict__(self) - return all info in dict


        """

    def __init__(self, **kwargs):   # (self, name: str, s_n: str, icon, rate: float, date: datetime.date):
        super().__init__(**kwargs)

    """AKA get info"""
    def __dict__(self) -> dict:
        return {'name': self.name,
                'short': self.short,
                'rate': self.rate,
                'date': self.date,
                'symbol': 'Br'}
