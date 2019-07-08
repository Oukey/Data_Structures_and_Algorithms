# модель множества


class PowerSet:

    def __init__(self):  # ваша реализация хранилища
        self.slots = []

    def size(self):  # количество элементов в множестве
        return len(self.slots)

    def put(self, value):  # метод добавления
        if self.get(value) is False:
            self.slots.append(value)

    def get(self, value):  # метод возврата
        if value in self.slots:  # возвращает True если value имеется в множестве,
            return True
        else:  # иначе False
            return False

    def remove(self, value):  # метод удаления
        if self.get(value) is True:
            self.slots.remove(value)
            return True  # возвращает True если value удалено
        else:
            return False  # иначе False

    def intersection(self, set2):  # пересечение текущего множества и set2
        set_3 = PowerSet()
        if self.size() >= set2.size():
            set_max = self
            set_min = set2
        else:
            set_max = set2
            set_min = self
        for i in set_min.slots:
            if set_max.get(i):
                set_3.put(i)
        return set_3

    def union(self, set2):  # объединение текущего множества и set2
        set_3 = PowerSet()
        for i in self.slots:
            set_3.put(i)
        for i in set2.slots:
            set_3.put(i)
        return set_3

    def difference(self, set2):  # разница текущего множества и set2
        set_3 = PowerSet()
        for i in self.slots:
            if set2.get(i) is False:
                set_3.put(i)
        return set_3

    def issubset(self, set2):
        for i in set2.slots:
            if self.get(i) is False:
                return False
        return True
