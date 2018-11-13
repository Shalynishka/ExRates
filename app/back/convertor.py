class Converter:
    __rates = []

    @property
    def rates(self):
        return self.__rates

    @rates.setter
    def rates(self, cur):
        self.rates.append(cur)

    def del_rate(self, short):                       # в такие методы надо будет объект отсылать
        shorts = [r.short for r in self.rates]
        self.__rates.pop(shorts.index(short))

    """zero-тот, кого надо конвертировать(ему ввели число)"""
    def convert(self, rate_name, num):
        answer = {}
        if rate_name == 'Br':
            answer['Br'] = num
            zero_rate = None
        else:
            shorts = [r.short for r in self.rates]
            zero_rate = self.rates[shorts.index(rate_name)]              # через нулевую(введенную) валюту вычислим Br
            answer['Br'] = num * zero_rate.rate[1]/zero_rate.rate[0]

        for r in self.rates:
            if r is zero_rate:
                answer[r.short] = num
            else:
                answer[r.short] = answer['Br']/r.rate[1]/r.rate[0]

        return answer
