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
        # набросок!
        key = int(key)
        result = BSTFind()
        node = self.Root
        if node is not None:
            while True:
                if node.NodeKey == key:
                    result.Node = node
                    result.NodeHasKey = True
                    break
                elif node.NodeKey < key:
                    if node.RightChild is not None:
                        node = node.RightChild
                        continue
                    else:
                        result.Node = node
                        result.NodeHasKey = False
                        result.ToLeft = False
                        break
                elif node.NodeKey > key:
                    if node.LeftChild is not None:
                        node = node.LeftChild
                        continue
                    else:
                        result.Node = node
                        result.NodeHasKey = False
                        result.ToLeft = True
                        break
            return result

    # def compare_keys(self, key, node):
    #     ''' Метод сравнения ключей '''
    #     if node is not None:
    #         if node.NodeKey == key:
    #             return True
    #         if node.NodeKey < key:
    #             if node.RightChild is not None:
    #                 return node.RightChild
    #             else:
    #                 return None
    #         if node.NodeKey >= key:
    #             if node.LeftChild is not None:
    #                 return node.LeftChild
    #             else:
    #                 return None
    #     pass

    def AddKeyValue(self, key, val):
        '''
        Метод добавления ключа-значения в дерево
        key - кюч
        val - значение
        return False если ключ уже есть, или True если добовление выполнено
        '''
        key = int(key)

        if self.Root is None:
            self.Root.NodeKey = key
            self.Root.NodeValue = val
            return True
        else:
            result = self.FindNodeByKey(key)
            if result.NodeHasKey is True:
                return False  # указанный узел уже есть в дереве
            else:
                if result.ToLeft is True:
                    result.Node.LeftChild.NodeKey = key
                    result.Node.LeftChild.NodeValue = val
                else:
                    result.Node.RightChild.NodeKey = key
                    result.Node.RightChild.NodeValue = val
                return True

    def FinMinMax(self, FromNode, FindMax):
        '''
        Метод поиска max/min узла в поддереве
        FromNode - указатеь на поддерево
        FindMax - параметр поиска (True - max, False - min)
        return узел Node
        '''
        node = self.FromNode
        if self.Root is not None:
            if FindMax is True:
                while True:
                    if self.Node.RightChild is not None:
                        node = node.RightChild
                        continue
                    else:
                        return node
            else:
                while True:
                    if self.Node.LeftChild is not None:
                        node = node.LeftChild
                        continue
                    else:
                        return node
        else:
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
