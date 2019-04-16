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

    # для подсчета количества узлов
    def bust(self, node):
        if self.Root is not None:
            yield node
            if node.LeftChild:
                yield from self.bust(node.LeftChild)
            if node.RightChild:
                yield from self.bust(node.RightChild)

    def GetAllNodes(self):
        '''метод возврата всех узлов дерева в виде списка'''
        node_list = []
        for node in self.bust(self.Root):
            node_list.append(node)
        return node_list

    def __iter__(self):
        return self

    def FindNodeByKey(self, key):
        '''
        Метод поиска узла в дереве и сопутствующей информации по нему
        key - ключ
        return BSRFind
        '''
        node = self.Root
        result = BSTFind()
        while node:
            if node.NodeKey == key:
                result.Node = node
                result.NodeHasKey = True
                break
            elif node.NodeKey > key:
                if node.LeftChild is None:
                    result.Node = node
                    result.ToLeft = True
                node = node.LeftChild
            else:
                if node.RightChild is None:
                    result.Node = node
                node = node.RightChild
        return result

    def AddKeyValue(self, key, val):
        '''
        Метод добавления ключа-значения в дерево
        key - ключ
        val - значение
        return False если ключ уже есть, или True если добавление выполнено
        '''
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        else:
            result = self.FindNodeByKey(key)
            if result.NodeHasKey is True:
                return False
            else:
                if result.ToLeft is True:
                    result.Node.LeftChild = BSTNode(key, val, result.Node)
                else:
                    result.Node.RightChild = BSTNode(key, val, result.Node)
                return True

    def FinMinMax(self, FromNode, FindMax):
        '''
        Метод поиска max/min узла в поддереве
        FromNode - указатель на поддерево
        FindMax - параметр поиска (True - max, False - min)
        return узел Node
        '''
        if self.Root is not None and self.FindNodeByKey(FromNode.NodeKey).Node is not None:
            if FindMax is True:
                while FromNode.RightChild is not None:
                    FromNode = FromNode.RightChild
            else:
                while FromNode.LeftChild is not None:
                    FromNode = FromNode.LeftChild
            return FromNode
        else:
            return None

    def DeleteNodeByKey(self, key):
        '''
        Метод удаления узла по ключу
        key - ключ
        return False если ключ не найден, или True если удаление выполнено
        '''
        if self.Root and self.Root.NodeKey != key and self.FindNodeByKey(key).NodeHasKey is True:
            node = self.FindNodeByKey(key).Node
            if node.RightChild:
                receiver = self.FinMinMax(node.RightChild, False)
                if receiver.RightChild is None:
                    self.change_link(node, receiver)

                else:
                    receiver = self.FinMinMax(receiver, True)
                    self.change_link(node, receiver)
                receiver.LeftChild = node.LeftChild
                receiver.Parent.LeftChild = None
            else:
                receiver = node.LeftChild
                self.change_link(node, receiver)

            return True
        else:
            return False

    def change_link(self, node, node_child):
        if node.Parent.LeftChild == node:
            node.Parent.LeftChild = node_child
        else:
            node.Parent.RightChild = node_child

    def Count(self):
        '''
        Метод подсчета узлов в дереве,
        возвращает целочисленное количество узлов
        '''
        return len(self.GetAllNodes())
