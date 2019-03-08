# Проект модели хзш-таблицы с применением
# универсального хэширования

import random


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.options_int = lambda value: ((value * random.randrange(1, 17, 2) + random.randint(0,
                                                                                               17)) % 17) % self.size
        self.options_str = lambda value: hash(value) % self.size

    def hash_fun(self, value):
        fun = None
        if type(value) == int:
            fun = self.options_int(value)
        elif type(value) == str:
            fun = self.options_str(value)
        return fun

    def see_slot(self, value):
        pass

    def put(self, value):
        pass

    def find(self, value):
        pass
    
