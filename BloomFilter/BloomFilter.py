# модель фильтра Блума


class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bitmap = [int(0) for i in range(self.filter_len)]

    def hash1(self, str1):  # 17
        code = 0
        for c in str1:
            code = code * 17 + ord(c)
        return code % self.filter_len

    def hash2(self, str1):  # 223
        code = 0
        for c in str1:
            code = code * 223 + ord(c)
        return code % self.filter_len

    def add(self, str1):  # добавляем строку str1 в фильтр
        self.bitmap[self.hash1(str1)] = int(1)
        self.bitmap[self.hash2(str1)] = int(1)

    def is_value(self, str1):  # проверка, имеется ли строка str1 в фильтре
        if self.bitmap[self.hash1(str1)] == 1 and self.bitmap[self.hash2(str1)] == 1:
            return True
        else:
            return False
