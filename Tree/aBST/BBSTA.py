# Модель сбалансированного двоичного дерева поиска


class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray = []  # временный массив для ключей дерева

    def depth_calc(self, array):
        '''
        Метод расчета глубины
        парамет array - исходный массив
        возвращает кортеж с параметрами: 0 - глубина дерева, 1 - длина массива
        '''
        if array:
            len_array = 0
            depth_tree = 0
            while len_array < len(array):
                depth_tree += 1
                len_array = 2 ** (depth_tree + 1) - 1
            return depth_tree, len_array
        else:
            return 0, 0

    def binary_sort(self, array_BST, array, ind):
        '''Метод сортировки массива под структуру BST'''
        if array:
            array_BST[ind] = array[len(array) // 2]
            self.binary_sort(array_BST, array[:len(array) // 2], 2 * ind + 1)
            self.binary_sort(array_BST, array[len(array) // 2 + 1:], 2 * ind + 2)
        else:
            return None

    def CreateFromArray(self, a):
        ''' Метод создания массива дерева BSTArray из заданного массива a'''
        if type(a) == list:
            a.sort()
            self.BSTArray = [None] * self.depth_calc(a)[1]
            self.binary_sort(self.BSTArray, a, 0)

    def GenerateTree(self):
        '''Метод создания дерева с нуля из массива BSTArray'''
        self.Root = self.tree_builder(0)
    
        def tree_builder(self, ind, parent=None):
        '''Метод рекурсивного построения дерева из массива с '''
        if len(self.BSTArray) > ind:
            node = BSTNode(self.BSTArray[ind], parent)
            if parent is None:
                node.Level = 1
            else:
                node.Level = parent.Level + 1
            node.LeftChild = self.tree_builder(ind * 2 + 1, node)
            node.RightChild = self.tree_builder(ind * 2 + 2, node)
            return node

    def IsBalanced(self, root_node):
        '''
        Метод проверки баланса дерева с корнем root_node
        return True если сбалансировано, иначе возвращает False
        '''
        return False  # сбалансировано ли дерево с корнем root_node
