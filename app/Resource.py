from Item import Item
from datetime import datetime


class Resource(Item):
    """
        Class for Resource. It contains Resource information.
        Child from Item

        Attributes:

        Methods and properties:

            __init__(self, name, s_n, icon, rate, date, s, f)
            __dict__(self) - return all info in dict

            properties(getter~+setter):
                price

            todo: Load and Store info
        """

    def __init__(self,  name: str, s_n: str, icon, rate: float, date: datetime.date):
        super().__init__(name, s_n, icon, rate, date)

    """AKA get info"""
    def __dict__(self) -> dict:
        return {'name': self.name,
                'short': self.s_name,
                'rate': self.rate,
                'date': self.date}


c = Resource('name12', 'sn', 'Icon1', .23, datetime.date(datetime.now()))

print(c.__dict__())



