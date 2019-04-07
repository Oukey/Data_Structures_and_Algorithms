# модель бинарного дерева


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если не найден узел
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        '''
        Метод поиска узла в дереве и сопутсвующей информации по нему
        key - ключ
        return BSRFind
        '''
        return None

    def AddKeyValue(self, key, val):
        '''
        Метод добавления ключа-значения в дерево
        key - кюч
        val - значение
        return False если ключ уже есть, или True если добовление выполнено
        '''
        return False

    def FinMinMax(self, FromNode, FindMax):
        '''
        Метод поиска max/min узе в поддереве
        FromNode - указатеь на поддерево
        FindMax - параметр поиска
        return узел Node
        '''
        return None

    def DeleteNodeByKey(self, key):
        '''
        Метод удаления узла по ключу
        key - ключ
        return False если ключ не найден, или True если удаление выполнено 
        '''
        return False

    def Count(self):
        '''
        Метод подсчета узлов в дереве, возвращает 
        return целочисленное количество узлов
        '''
        return 0  # количество узлов в дереве
