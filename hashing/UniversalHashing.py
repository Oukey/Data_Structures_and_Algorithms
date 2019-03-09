# Проект модели хзш-таблицы с применением
# универсального хэширования

import random


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.num = random.choice((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53))
        self.options_int = lambda value: ((value * random.randrange(1, self.num, 2) + random.randint(0,
                                                                                                     self.num)) % self.num) % self.size
        self.options_str = {0: lambda value: hash(value) % self.size,
                            1: lambda value: ((len(value) * self.num + self.step) % self.num) % self.size,
                            2: lambda value: (len(value) * self.num + self.step - 1) % self.size
                            }

    def hash_fun(self, value):
        fun = None
        if type(value) == int:
            fun = self.options_int(value)
        elif type(value) == str:
            fun = random.choice(self.options_str)(value)
        return fun

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        buffer = 0
        while buffer < self.size:
            if self.slots[slot] is None:
                return slot
            slot += self.step
            if slot > self.size - 1:
                slot -= self.size
            buffer += 1

    def put(self, value):
        ind = self.seek_slot(value)
        if ind is not None:
            self.slots[ind] = value
            return ind
        else:
            return None

    def find(self, value):
        if value in self.slots:
            return self.slots.index(value)
        else:
            return None
