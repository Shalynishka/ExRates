
class Item:
    """
    Class for Item. It contains general characteristics for Currencies and Resources
    Attributes:
        __name   - name of Item
        __short - short name of Item
        __icon   - mini image of Item
        __rate   - rate of Item [1 $ to 2.1431 by]
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
    __short = ''
    __icon = 'Some'   # по имени подгружать иконку? Тогда не нужен конструктор
    __rate = .0
    __date = ''

    def __init__(self, **kwargs):   # (name: str, s_n: str, icon, rate: float, date: datetime.date)
        self.__name = kwargs['name']
        self.__short = kwargs['short']
        self.__icon = kwargs['short'] + '.png'
        self.__rate = kwargs['rate']
        self.__date = str(kwargs['date'])

    """name of item"""
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    """short name of item"""
    @property
    def short(self):
        return self.__short

    @short.setter
    def short(self, sn):
        self.__short = sn

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

    """icon"""
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, i):
        self.__icon = i
