from datetime import datetime


class Item:
    """
    Class for Item. It contains general characteristics for Currencies and Resources
    Attributes:
        __name   - name of Item
        __s_name - short name of Item
        __icon   - mini image of Item
        __rate   - rate of Item
        __date   - date of last update of Item

    Methods and properties:

        __init__(self, name, s_n, icon, rate, date)

        properties(getter~+setter):
            name
            s_name
            rate
            date

        todo: Icon and work with it
    """
    __name = ''
    __s_name = ''
    __icon = 'Some'   # по имени подгружать иконку? Тогда не нужен конструктор
    __rate = .0
    __date = ''

    def __init__(self, name: str, s_n: str, icon, rate: float, date: datetime.date):
        self.__name = name
        self.__s_name = s_n
        self.__icon = icon
        self.__rate = rate
        self.__date = date

    """name of item"""
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    """short name of item"""
    @property
    def s_name(self):
        return self.__s_name

    @s_name.setter
    def s_name(self, sn):
        self.__s_name = sn

    """rate of item"""
    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, r):
        self.__rate = r

    """date of last update"""
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, d):
        self.__date = d


s = Item('name', 's_n', 'icon', .5, datetime.today())

print(s.name)
s.name = 'hello'
print(s.name)


dd = datetime.date(datetime.today())
print(dd)
