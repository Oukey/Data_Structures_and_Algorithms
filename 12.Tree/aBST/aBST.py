# модель преобразования массива под структуру BST


def depth_calc(a):
    '''# модель двоичного дерева поиска

class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.12.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        '''
        Метод поиска ключа в массиве
        Параметр "key" - искомый ключ
        return - индекс с найденным ключем, индекс *(-1) если найден свободный индекс или None если ключ не найден
        '''
        if self.12.Tree[0] is None:  # если дерево не заполнено
            return 0
        elem = 0
        while elem < len(self.12.Tree):
            # если найдено свободное мето
            if self.12.Tree[elem] is None:
                return - elem
            # если ключ найден
            if key == self.12.Tree[elem]:
                return elem
            # если искомый ключ больше текущего
            if key > self.12.Tree[elem]:
                elem = 2 * elem + 2
                continue
            # если искомый ключ меньше текущего
            if key < self.12.Tree[elem]:
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
            if self.12.Tree[abs(result)] is None:
                self.12.Tree[abs(result)] = key
            return abs(result)



    модуль расчета глубины
    параметр a - исходный массив
    возвращает кортеж с параметрами: 0 - глубина дерева, 1 - длина массива
    '''
    if a:
        len_array = 0
        depth_tree = 0
        while len_array < len(a):
            depth_tree += 1
            len_array = 2 ** (depth_tree + 1) - 1
        return depth_tree, len_array


def binary_sort(array_BST, a, ind):
    if a:
        array_BST[ind] = a[len(a) // 2]
        binary_sort(array_BST, a[:len(a) // 2], 2 * ind + 1)
        binary_sort(array_BST, a[len(a) // 2 + 1:], 2 * ind + 2)
    else:
        return None


def GenerateBBSTArray(a):
    '''
    Функция сортировки массива под структуру BST
    Параметр (a) неотсортированный массив
    return - массив со структурой сбалансированного BST
    '''
    a.sort()
    array_BST = [None] * depth_calc(a)[1]
    binary_sort(array_BST, a, 0)
    return array_BST
