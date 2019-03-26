# универсальное хэширование

import random


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.options_int = random.choice([  # выбор из списока хэш_функций для цифр и пустой строки
            lambda value: int((value * 37 + 29 % 11) % (self.size + 1)),
            lambda value: int(((11 ** value * self.step + self.step) % self.size)),
            lambda value: int((((123 + value + self.step) * self.step) % self.size)),
        ])
        self.options_str = random.choice([  # выбор из списока хэш_функций для строк
            lambda value: (41 + len(value) + ord(value[0]) + ord(value[len(value) - 1]) ** 11) % self.size,
            lambda value: ((len(value) ** 7 + ord(value[0]) ** 7 + ord(value[len(value) - 1]) ** 7) % 11) % self.size,
            lambda value: (17 + len(value) + ord(value[0]) + ord(value[len(value) - 1]) ** 123) % self.size,
        ])

    def hash_fun(self, value):  # функция возвращает хэш функцию по типу вводимых данных
        if type(value) == int or type(value) == float:  # для чисел
            return self.options_int(value)
        else:
            if value == '':  # для пустой строки
                return self.options_int(0)
            else:  # для строк
                return self.options_str(value)

    def seek_slot(self, value):  # находит индекс пустого слота для значения, или None
        slot = self.hash_fun(value)
        buffer = 0
        while buffer < self.size:
            if self.slots[slot] is None:
                return slot
            slot += self.step
            if slot > self.size - 1:
                slot -= self.size
            buffer += 1
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value  # записываем значение по хэш-функции
            return slot  # возвращается индекс слота или None,
        else:  # если из-за коллизий элемент не удаётся разместить
            return None

    def find(self, value):
        # находит индекс слота со значением, или None
        slot = self.hash_fun(value)
        if self.slots[slot] == value:
            return slot
        for slt in range(self.size):
            if self.slots[slt] == value:
                return slt
        return None
