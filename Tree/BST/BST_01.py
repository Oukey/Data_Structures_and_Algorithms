# модель бинарного дерева


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def __repr__(self):
        return 'Node_{}'.format(self.NodeKey)


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
        else:
            return None

    def AddKeyValue(self, key, val):
        '''
        Метод добавления ключа-значения в дерево
        key - кюч
        val - значение
        return False если ключ уже есть, или True если добовление выполнено
        '''
        Node = BSTNode(key, val, None)
        if self.Root is None:  # если дерево пустое
            self.Root = Node
            return True
        else:  # иначе если в дереве есть узлы...
            result = self.FindNodeByKey(key)
            if result.NodeHasKey is True:  # если заданный узел уже есть в дереве
                return False  # указанный узел уже есть в дереве
            else:
                if result.ToLeft is True:  # если заданный ключь меньше текущего
                    result.Node.LeftChild = Node
                    Node.Parent = result.Node.LeftChild
                else:  # если заданный ключь больше текущего
                    result.Node.RightChild = Node
                    Node.Parent = result.Node.RightChild
                return True

    def FinMinMax(self, FromNode, FindMax):
        '''
        Метод поиска max/min узла в поддереве
        FromNode - указатеь на поддерево
        FindMax - параметр поиска (True - max, False - min)
        return узел Node
        '''

        if self.Root is not None:
            node = self.FindNodeByKey(FromNode.NodeKey).Node
            if FindMax is True:
                while True:
                    if node.RightChild is not None:
                        node = node.RightChild
                        continue
                    else:
                        return node
            else:
                while True:
                    if node.LeftChild is not None:
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


tree = BST(None)
# tree.AddKeyValue(5, 50)
# tree.AddKeyValue(3, 30)
# tree.AddKeyValue(8, 80)
# tree.AddKeyValue(7, 77)
# tree.AddKeyValue(10, 101)
# tree.AddKeyValue(4, 44)
# tree.AddKeyValue(1, '01')
find = tree.FindNodeByKey(8)
print(find)
print(find.Node)
# print(find.NodeHasKey)
# print(find.ToLeft)
# print(tree.FinMinMax(tree.Root, True))
