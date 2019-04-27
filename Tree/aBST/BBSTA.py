# модель преобразования массива под структуру BST


def depth_calc(a):
    '''
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
    if type(a) == list:
        a.sort()
        array_BST = [None] * depth_calc(a)[1]
        binary_sort(array_BST, a, 0)
        return array_BST
