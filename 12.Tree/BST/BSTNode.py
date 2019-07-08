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

    def CreateFromArray(self, a):
        pass

    # создаём массив дерева BSTArray из заданного a
    # ...

    def GenerateTree(self):
        pass

    # создаём дерево с нуля из массива BSTArray
    # ...      

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node
