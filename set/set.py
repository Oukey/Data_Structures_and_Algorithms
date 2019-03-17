# модель множества
# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable


class PowerSet:

    def __init__(self):
        # ваша реализация хранилища

    def size(self):
        return 0
        # количество элементов в множестве

    def put(self, value):
        # всегда срабатывает

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        return None 

    def union(self, set2):
        # объединение текущего множества и set2
        return None

    def difference(self, set2):
        # разница текущего множества и set2
        return None

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False
