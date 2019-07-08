# Кэш


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        code = 0
        for symbol in str(key):
            code = ord(symbol) + code * 11
        return code % self.size

    def seek_slot(self, key):  # метод поиска свободного слота.
        # циклом перебираются все слоты на предмет поиска пустого места или того-же ключа
        slot = self.hash_fun(key)
        mark = slot
        while self.slots[slot] is not None and self.slots[slot] != key:
            slot = (slot + 1) % self.size
            if slot == mark:
                return None
        return slot

    def put(self, key, value):  # метод вставки ключа и значения
        # если нет свободных слотов и ключ ранее не встречался -
        # перезаписываются элементы самого непопулярного слота
        slot = self.seek_slot(key)
        if slot is None:
            slot = self.min_hits()
        self.slots[slot] = key
        self.values[slot] = value
        self.hits[slot] = 1

    def get(self, key):  # метод получения значения по запросу ключа
        # фиксируется количество запросов по текущему ключу
        slot = self.seek_slot(key)
        if slot is not None:
            self.hits[slot] += 1
            return self.values[slot]
        else:
            return None

    def is_key(self, key):  # метод определения наличия заданного ключа
        # предусмотрел условие, т.к. метод seek_slot может вернуть None
        slot = self.seek_slot(key)
        if slot is not None:
            return self.slots[slot] == key
        else:
            return False

    def min_hits(self):  # метод определения наименее популярного слота
        return self.hits.index(min(self.hits))

    def find(self, key):  # метод поиска слота по ключу (для тестирования)
        if self.is_key(key) is True:
            return self.slots.index(key)
        else:
            return None

'''
# логи
nc = NativeCache(3)
nc.put('1', 1)
nc.put('2', 2)
nc.put('3', 3)
nc.put('4', 4)
nc.put('5', 5)
nc.get('5')
nc.put('6', 6)
nc.get('6')
nc.put('7', 70)
nc.get('8')
print('+++', nc.get('8'))

print('nc.slots', nc.slots)
print('nc.values', nc.values)
print('nc.hits', nc.hits)
print('nc.is_key', nc.is_key('10'))
print('nc.fun', nc.hash_fun('10'))
print('nc.slot', nc.seek_slot('10'))
print('min', nc.min_hits())
print(nc.find('1'))
'''
