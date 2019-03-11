# Модель словаря


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots_key = [None] * self.size  # массив для ключей
        self.slots_value = [None] * self.size  # массив для значений

    def hash_fun(self, key):  # резерв
        return self.slots_key.index(None)

    def seek_slot(self, key):  # функция определения свободного слота
        if self.is_key(key) is False:
            if self.slots_key.count(None) != 0:
                return self.slots_key.index(None)
            else:
                return None  # если массив заполнен
        else:
            return True

    def put(self, key, value):  # сохранение внутри класса ассоциативного массива пары ключ-значение
        slot = self.seek_slot(key)
        if slot is True:
            self.slots_value[self.slots_key.index(key)] = value
        elif slot is not None:
            self.slots_key[slot] = key
            self.slots_value[slot] = value
            return slot
        else:
            return None

    def is_key(self, key):  # проверка, имеется ли в слотах такой ключ
        if key in self.slots_key:
            return True
        else:
            return False

    def get(self, key):  # поиск и извлечение значения по ключу или отсутствие значения если ключ не найден
        if self.is_key(key) is True:
            return self.slots_value[self.slots_key.index(key)]
        else:
            return None
