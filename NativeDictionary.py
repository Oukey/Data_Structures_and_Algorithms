class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size

    def put(self, key, value):
        # сохранение внутри класса ассоциативного массива пары ключ-значение
        pass

    def is_key(self, key):
        # проверка, имеется ли в слотах такой ключ
        pass

    def get(self, key):
        # поиск и извлечение значения по ключу или отсутствие значения если ключ не найден
        pass
