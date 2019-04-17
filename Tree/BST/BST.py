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

    def find_receiver(self, node_del):
        rec = node_del
        if node_del.RightChild is not None:
            rec = self.FinMinMax(node_del.RightChild, False)
            if rec.RightChild is not None:
                rec = self.find_receiver(rec.RightChild)
        return rec

    def DeleteNodeByKey(self, key):
        '''
        Метод удаления узла по ключу
        key - ключ
        return False если ключ не найден, или True если удаление выполнено
        '''
        if self.Root and self.Root.NodeKey != key and self.FindNodeByKey(key).NodeHasKey is True:
        # if self.Root and self.Root.NodeKey != key:
            node = self.FindNodeByKey(key).Node
            # Если нет потомков
            if node.RightChild is None and node.LeftChild is None:
                self.change_link(node, None)
                node.Parent = None
            # если есть только левый потомок
            elif node.RightChild is None and node.LeftChild:
                self.change_link(node, node.LeftChild)
                node.RightChild = None
                node.LeftChild = None
                node.Parent = None
            # если есть только правый потомок
            elif node.RightChild and node.LeftChild is None:
                self.change_link(node, node.RightChild)
                node.RightChild = None
                node.LeftChild = None
                node.Parent = None
            # если есть и правый и левый потомок
            elif node.RightChild and node.LeftChild:
                rec = self.find_receiver(node)
                self.change_link(rec, None)
                rec.Parent = None
                rec.RightChild = None
                rec.LeftChild = None
                node.NodeKey = rec.NodeKey
                node.NodeValue = rec.NodeValue


            return True
        else:
            return False

    def change_link(self, node_del, node_child):
        if node_del.Parent.LeftChild == node_del:
            node_del.Parent.LeftChild = node_child
        else:
            node_del.Parent.RightChild = node_child

    def Count(self):
        '''
        Метод подсчета узлов в дереве,
        возвращает целочисленное количество узлов
        '''
        return len(self.GetAllNodes())


'''логи'''
tr = BST(None)
tr.AddKeyValue(5, 5)  # 0
tr.AddKeyValue(3, 3)  # 1
tr.AddKeyValue(8, 8)  # 2 !!!
tr.AddKeyValue(2, 2)  # 3
tr.AddKeyValue(4, 4)  # 4
tr.AddKeyValue(1, 1)  # 5
tr.AddKeyValue(7, 7)  # 6
tr.AddKeyValue(10, 10)  # 7 !!!
tr.AddKeyValue(9, 9)  # 8
tr.AddKeyValue(6, 6)  # 9
tr.AddKeyValue(0, 0)  # 10
tr.AddKeyValue(11, 0)  # 11
tr.AddKeyValue(12, 0)  # 12

print('Количество узлов:', tr.Count())
print('Список:', tr.GetAllNodes())
key = 1
tr.DeleteNodeByKey(8)
tr.DeleteNodeByKey(3)
tr.DeleteNodeByKey(0)
tr.DeleteNodeByKey(10)
tr.DeleteNodeByKey(9)
tr.DeleteNodeByKey(2)
tr.DeleteNodeByKey(4)
tr.DeleteNodeByKey(1)
tr.DeleteNodeByKey(6)
tr.DeleteNodeByKey(7)
tr.DeleteNodeByKey(11)
tr.DeleteNodeByKey(12)
tr.DeleteNodeByKey(11)
# tr.DeleteNodeByKey(key)
# print('Удаление:', tr.DeleteNodeByKey(key))
print('Количество узлов:', tr.Count())
print('Список:', tr.GetAllNodes())

print('_' * 40)
key_1 = 5
print('родитель:', tr.FindNodeByKey(key_1).Node.Parent)
print('левый:', tr.FindNodeByKey(key_1).Node.LeftChild)
print('правый:', tr.FindNodeByKey(key_1).Node.RightChild)

# print(tr.FinMinMax(tr.FindNodeByKey(8).Node, False))
# print('*' * 40)
# node = tr.FindNodeByKey(10).Node
# print(tr.find_receiver(node))

print(tr.FindNodeByKey(1).NodeHasKey)
