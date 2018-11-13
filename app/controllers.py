class Controller:
    @staticmethod
    def show_info(i):
        return i.__dict__()


class CurController(Controller):
    __cur = []
    __fav_cur = []

    @property
    def cur(self):
        return self.__cur

    @cur.setter
    def cur(self, c):
        self.__cur.append(c)

    def find_cur(self, *names):
        answer = []
        if names:
            for n in names:
                answer.append(self.__cur[self.__cur.index(n)])
        return answer

    @property
    def fav(self):
        return self.__fav_cur

    @fav.setter
    def fav(self, f):
        self.__fav_cur.append(f)

    # todo возможно добавить обработку исключения отсутствия индекса. Возможно.
    def del_fav(self, f):
        self.__fav_cur.pop(self.__fav_cur.index(f))

    def update_cur(self):
        for c in self.__cur:
            # todo сделать обновление информации по ресурсам
            print(c)


class ResController(Controller):
    __res = []

    @property
    def res(self):
        return self.__res

    @res.setter
    def res(self, r):
        self.__res.append(r)

    def update_res(self):
        for r in self.__res:
            # todo сделать обновление информации по ресурсам
            print(r)


class CryptController(Controller):
    __crypt = []

    @property
    def crypt(self):
        return self.__crypt

    @crypt.setter
    def res(self, cr):
        self.__crypt.append(cr)

    def update_crypt(self):
        for cr in self.__crypt:
            # todo сделать обновление информации по ресурсам
            print(cr)


r = CurController()

for c in 'spam':
    r.cur = c

print(r.find_cur('s', 'a'))
print(r.fav)

