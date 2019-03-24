# Кэш


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def put(self, key, value):  # метод вставки ключа и значения.
        # O(1) в лучшем и O(n) в худшем случае
        # если нет свободных слотов определяется индекс самого непопулярного ключа за O(n)
        slot = self.seek_fun(key)
        # if slot is None:  # запасной вариант
        #     slot = self.min_hits()  # запасной вариант
        self.slots[slot] = key
        self.values[slot] = value
        self.hits[slot] = 1

    def hash_fun(self, key):
        code = 0
        for c in str(key):
            code = code * 11 + ord(c)
        return code % self.size

    def seek_fun(self, key):  # метод поиска свободного слота.
        # циклом выполняется перебор всех эементов на поиск свободного мета:
        # в лучшем случае поиск свободного слота обходится за O(1),
        # в худшем случае сложность O(n).
        # если нет свободных слотов возвращается None!
        # если уже есть такой кюч вернется номер его слота.
        slot = self.hash_fun(key)
        counter = 0
        while counter < self.size:
            if self.slots[slot] is None:
                return slot
            elif self.slots[slot] == key:
                return slot
            slot += 1
            if slot + 1 > self.size:
                slot = 0
            counter += 1
        # return None  # запасной вариант
        return self.min_hits()

    def min_hits(self):  # метод определения наименее популярного элемента
        return self.hits.index(min(self.hits))  # O(n)

    def get(self, key):  # метод получения значения по ключу.
        # в лучшем случае поиск индекса обходится за O(1), в худшем за O(n);
        # количество запросов запрашиваемого ключа увеличивается на 1.
        # если ключ не найден - возвращается None!
        slot = self.seek_fun(key)
        if slot is not None:
            self.hits[slot] += 1
            return self.values[slot]
        else:
            for el in range(self.size):
                if self.slots[el] == key:
                    self.hits[el] += 1
                    return self.values[el]
                return None


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
nc.put('7', 7)
nc.get('8')
print('+++', nc.get('8'))

print('nc.slots', nc.slots)
print('nc.values', nc.values)
print('nc.hits', nc.hits)
