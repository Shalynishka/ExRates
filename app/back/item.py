
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
    """

    name = ''
    short = ''
    icon = 'Some'   # по имени подгружать иконку? Тогда не нужен конструктор
    rate = .0
    date = ''

    def __init__(self, **kwargs):   # (name: str, s_n: str, icon, rate: float, date: datetime.date)
        self.__name = kwargs['name']
        self.__short = kwargs['short']
        self.__icon = kwargs['short'] + '.png'
        self.__rate = kwargs['rate']
        self.__date = str(kwargs['date'])
