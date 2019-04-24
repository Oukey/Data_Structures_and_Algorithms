# метод двоичного дерева поиска

class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        '''
        Метод поиска ключа в массиве
        Параметр "key" - искомый ключ
        return - индекс с найденным ключем, индекс *(-1) если найден свободный индекс или None если ключ не найден
        '''
        if self.Tree[0] is None:  # если дерево не заполнено
            return 0
        elem = 0
        while elem < len(self.Tree):
            # если найдено свободное мето
            if self.Tree[elem] is None:
                return - elem
            # если ключ найден
            if key == self.Tree[elem]:
                return elem
            # если искомый ключ больше текущего
            if key > self.Tree[elem]:
                elem = 2 * elem + 2
                continue
            # если искомый ключ меньше текущего
            if key < self.Tree[elem]:
                elem = 2 * elem + 1
                continue
        return None  # если свободных узлов и совпадений нет

    def AddKey(self, key):
        '''
        Метод добавления ключа в массив
        Параметр "key" - заданный ключ
        return - индекс добавленного/существующего ключа или -1 если добавление не удалось
        '''
        result = self.FindKeyIndex(key)
        # если не найдено свободных узлов
        if result is None:
            return -1
        else:
            # если найден узел для добавления нового ключа
            if self.Tree[abs(result)] is None:
                self.Tree[abs(result)] = key
            return abs(result)

        
def GenerateBBSTArray(a):
    '''
    Функция сортировки массаива под структуру BST
    Параметр (a) неотсортированный массив
    return - массив, содержащий структуру сбалансированного BST
    '''
    return None
