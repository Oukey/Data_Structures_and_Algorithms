# метод двоичного дерева поиска


class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1  # рассчет количество узлов по заданной глубине
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        '''
        Метод поиска ключа в массиве
        Параметр "key" - искомый ключ
        return - индекс с найденным ключем или None если ключ не найден
        '''
        if self.Tree[0] is None:
            return 0
        elem = 0
        while elem < len(self.Tree):
            # если ключ найден
            if key == self.Tree[elem]:
                return elem
            # если найден свободный узел
            elif self.Tree[elem] is None:
                return - elem
            # если заданный ключ меньше текущего - переход к левому потомку
            elif key < self.Tree[elem]:
                elem = 2 * elem + 1
                continue
            # если заданный ключ больше текущего - переход к правому потомку
            elif key > self.Tree[elem]:
                elem = 2 * elem + 2
                continue
        return None

    def AddKey(self, key):
        '''
        Метод добавления ключа в массив
        Параметр "key" - заданный ключ
        return - индекс добавленного/существующего ключа или -1 если добавление не удалось
        '''
        result = self.FindKeyIndex(key)
        if result is None or result > 0:
            return -1
        elif result <= 0:
            self.Tree[abs(result)] = key
            return abs(result)
