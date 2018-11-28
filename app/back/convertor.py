class Converter:
    """
        Class for Crypto-currency. It contains Crypto-currency information.
        Child from Item

        Attributes:
            __rates - list of currency to convert
        Methods and properties:
            properties:
                rates - getter + setter

            del_rate(self, short)         - delete currency from __rates
            convert(self, rate_name, num) - return dict of convert values
    """

    __rates = {}

    @property
    def rates(self):
        return self.__rates

    @rates.setter
    def rates(self, cur):
        self.rates[cur.short] = cur

    def del_rate(self, short):                       # отправить только имя
        self.__rates.pop(short)

    def convert(self, rate_name: str, num: float) -> dict:
        """zero-тот, кого надо конвертировать(ему ввели число)"""

        answer = {}
        if rate_name == 'BYN':
            answer['BYN'] = num
            zero_rate = None
        else:
            zero_rate = self.rates[rate_name]              # через нулевую(введенную) валюту вычислим Br
            answer['BYN'] = num * zero_rate.rate[1]/zero_rate.rate[0]

        for r in self.rates.values():
            if r is zero_rate:
                answer[r.short] = num
            else:
                answer[r.short] = answer['BYN']/r.rate[1]/r.rate[0]

        answer.pop(rate_name)
        return answer
