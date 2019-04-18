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
key_1 = key
print('родитель:', tr.FindNodeByKey(key_1).Node.Parent)
print('левый:', tr.FindNodeByKey(key_1).Node.LeftChild)
print('правый:', tr.FindNodeByKey(key_1).Node.RightChild)

# print(tr.FinMinMax(tr.FindNodeByKey(8).Node, False))
# print('*' * 40)
# node = tr.FindNodeByKey(10).Node
# print(tr.find_receiver(node))

print(tr.FindNodeByKey(1).NodeHasKey)

'''
# модель бинарного дерева


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def __repr__(self):
        return '_{}'.format(self.NodeKey)


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
        # Вариант №1___________________
        # result = BSTFind()
        # node = self.Root
        # if node is not None:
        #     while True:
        #         if node.NodeKey == key:
        #             result.Node = node
        #             result.NodeHasKey = True
        #             break
        #         elif node.NodeKey < key:
        #             if node.RightChild is not None:
        #                 node = node.RightChild
        #                 continue
        #             else:
        #                 result.Node = node
        #                 result.NodeHasKey = False
        #                 result.ToLeft = False
        #                 break
        #         elif node.NodeKey > key:
        #             if node.LeftChild is not None:
        #                 node = node.LeftChild
        #                 continue
        #             else:
        #                 result.Node = node
        #                 result.NodeHasKey = False
        #                 result.ToLeft = True
        #                 break
        #     return result
        # else:
        #     return None

        # Вариант №2___________________
        node = BSTFind()
        node.Node = self.Root
        if self.Root is None:
            return node
        while node.Node.NodeKey != key:
            if key > node.Node.NodeKey:
                if node.Node.RightChild is None:
                    break
                node.Node = node.Node.RightChild
            else:
                if node.Node.LeftChild is None:
                    node.ToLeft = True
                    break
                node.Node = node.Node.LeftChild
        else:
            node.NodeHasKey = True
        return node

    def AddKeyValue(self, key, val):
        '''
        Метод добавления ключа-значения в дерево
        key - кюч
        val - значение
        return False если ключ уже есть, или True если добовление выполнено
        '''

        # Вариант №1___________________
        # Node = BSTNode(key, val, None)
        # if self.Root is None:  # если дерево пустое
        #     self.Root = Node
        #     return True
        # else:  # иначе если в дереве есть узлы...
        #     result = self.FindNodeByKey(key)
        #     if result.NodeHasKey is True:  # если заданный узел уже есть в дереве
        #         return False  # указанный узел уже есть в дереве
        #     else:
        #         if result.ToLeft is True:  # если заданный ключь меньше текущего
        #             result.Node.LeftChild = Node
        #             Node.Parent = result.Node.LeftChild
        #         else:  # если заданный ключь больше текущего
        #             result.Node.RightChild = Node
        #             Node.Parent = result.Node.RightChild
        #         return True

        # Вариант №2___________________
        node = self.FindNodeByKey(key)
        new_node = BSTNode(key, val, None)
        if self.Root is None:
            self.Root = new_node
        elif node.NodeHasKey is False:
            if node.ToLeft:
                node.Node.LeftChild = new_node
            else:
                node.Node.RightChild = new_node
            new_node.Parent = node.Node
            return True
        else:
            return False

    def FinMinMax(self, FromNode, FindMax):
        '''
        Метод поиска max/min узла в поддереве
        FromNode - указатеь на поддерево
        FindMax - параметр поиска (True - max, False - min)
        return узел Node
        '''

        # Вариант №1___________________
        # if self.Root is not None:
        #     node = self.FindNodeByKey(FromNode.NodeKey).Node
        #     if FindMax is True:
        #         while True:
        #             if node.RightChild is not None:
        #                 node = node.RightChild
        #                 continue
        #             else:
        #                 return node
        #     else:
        #         while True:
        #             if node.LeftChild is not None:
        #                 node = node.LeftChild
        #                 continue
        #             else:
        #                 return node
        # else:
        #     return None

        # Вариант с рекурсией___________________
        if self.Root:
            if FindMax:
                if FromNode.RightChild is not None:
                    FromNode = self.FinMinMax(FromNode.RightChild, FindMax)
            else:
                if FromNode.LeftChild is not None:
                    FromNode = self.FinMinMax(FromNode.LeftChild, FindMax)
            return FromNode

    def DeleteNodeByKey(self, key):
        '''
        Метод удаления узла по ключу
        key - ключ
        return False если ключ не найден, или True если удаление выполнено
        '''
        # Вариант №1___________________
        # node_del = self.FindNodeByKey(key)
        # if node_del.NodeHasKey is True:
        #     node = node_del.Node
        #     if node.RightChild and node.LeftChild:
        #         rec = self.FinMinMax(node.RightChild, False)
        #         if rec.RightChild:
        #             rec = rec.RightChild
        #             rec.Parent.RightChild = None
        #         else:
        #             rec.Parent.LeftChild = None
        #     else:
        #         if node.RightChild:
        #             rec = node.RightChild
        #             node.RightChild = rec.RightChild
        #             node.LeftChild = rec.LeftChild
        #         elif node.LeftChild:
        #             rec = node.LeftChild
        #             node.RightChild = rec.RightChild
        #             node.LeftChild = rec.LeftChild
        #         else:
        #             rec = node
        #             if rec.Parent.RightChild == rec:
        #                 rec.Parent.RightChild = None
        #             else:
        #                 rec.Parent.LeftChild = None
        #     rec.Parent = None
        #     node_del.Node.NodeKey = rec.NodeKey
        #     node_del.Node.NodeValue = rec.NodeValue
        #     return True
        # else:
        #     return False

        # Вариант №2_________________
        # if self.Root:
        #     node = self.FindNodeByKey(key).Node
        #     # Если нет потомков
        #     if node.RightChild is None and node.LeftChild is None:
        #         self.change_link(node, None)
        #         node.Parent = None
        #     # если есть только левый потомок
        #     elif node.RightChild is None and node.LeftChild:
        #         self.change_link(node, node.LeftChild)
        #         self.change_link(node, None)
        #         node.RightChild = None
        #         node.LeftChild = None
        #         node.Parent = None
        #     # если есть только правый потомок
        #     elif node.RightChild and node.LeftChild is None:
        #         self.change_link(node, node.RightChild)
        #         self.change_link(node, None)
        #         node.RightChild = None
        #         node.LeftChild = None
        #         node.Parent = None
        #     # если есть и правый и левый потомок
        #     elif node.RightChild and node.LeftChild:
        #         rec = self.find_receiver(node)
        #         self.change_link(rec, None)
        #         rec.Parent = None
        #         rec.RightChild = None
        #         rec.LeftChild = None
        #         node.NodeKey = rec.NodeKey
        #         node.NodeValue = rec.NodeValue
        #     return True
        # else:
        #     return False

        # Вариант №3___________________
        node = self.FindNodeByKey(key).Node
        '''1 если первый и правый потомок'''
        if self.FindNodeByKey(key):
            rec = self.find_receiver(node)
            self.change_link(rec, None)  # step_1
            rec.Parent = node.Parent  # spet_2
            self.change_link(node, rec)  # spet_3
            rec.RightChild = node.RightChild  # spet_4
            rec.LeftChild = node.LeftChild  # spet_5
            node.RightChild = None  # spet_6
            node.LeftChild = None  # spet_7
            node.Parent = None  # spet_8









    def find_receiver(self, node_del):
        rec = node_del
        if node_del.RightChild is not None:
            rec = self.FinMinMax(node_del.RightChild, False)
            if rec.RightChild is not None:
                rec = self.find_receiver(rec.RightChild)
        return rec

    def change_link(self, node_del, node_child):
        if node_del.Parent.LeftChild == node_del:
            node_del.Parent.LeftChild = node_child
        else:
            node_del.Parent.RightChild = node_child

    def Count(self):
        '''
        Метод подсчета узлов в дереве, возвращает
        return целочисленное количество узлов
        '''
        # Вариант №1___________________
        return len(self.GetAllNodes())

        # Вариант №2___________________
        # node = self.Root
        # len_list = [None, self.Root]
        # while node is not None:
        #     if node.LeftChild not in len_list and node.LeftChild is not None:
        #         node = node.LeftChild
        #     elif node.RightChild not in len_list and node.RightChild is not None:
        #         node = node.RightChild
        #     if node not in len_list:
        #         len_list.append(node)
        #     if node.LeftChild is None and node.RightChild is None:
        #         node = node.Parent
        #     elif node.LeftChild in len_list and node.RightChild is len_list:
        #         node = node.Parent
        #     z = 1
        #     for el in len_list:
        #         if el is not None:
        #             z += 1
        #     return z

    def bust(self, node):
        '''Метод перебора всех узлов дерева'''
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


# n1 = BSTNode(8, 8, None)
# n2 = BSTNode(11, 8, None)
# n3 = BSTNode(5, 8, None)
# n4 = BSTNode(14, 8, None)
# n5 = BSTNode(2, 8, None)
# n6 = BSTNode(16, 8, None)
# n7 = BSTNode(0, 8, None)
# n8 = BSTNode(1, 8, None)
# n9 = BSTNode(2, 8, None)
# n10 = BSTNode(10, 8, None)
# n11 = BSTNode(9, 8, None)


tr = BST(None)
tr.AddKeyValue(8, 0)
tr.AddKeyValue(11, 0)
tr.AddKeyValue(5, 0)
tr.AddKeyValue(14, 0)
tr.AddKeyValue(2, 0)
tr.AddKeyValue(16, 0)
tr.AddKeyValue(0, 0)
tr.AddKeyValue(1, 0)
tr.AddKeyValue(3, 0)
tr.AddKeyValue(10, 0)
tr.AddKeyValue(4, 0)
tr.AddKeyValue(40, 0)
key = 8
key_1 = key
print('Список:', tr.GetAllNodes(), end=' / ')
print('Кол-во:', tr.Count())
print('Родитель:', tr.FindNodeByKey(key).Node.Parent, end='/ ')
print('Узел:', tr.FindNodeByKey(key).Node, end='/ ')
print('Левый:', tr.FindNodeByKey(key).Node.LeftChild, end='/ ')
print('Правый:', tr.FindNodeByKey(key).Node.RightChild, end='/ ')
print('Найден: ', tr.FindNodeByKey(key).NodeHasKey)

print('min:', tr.FinMinMax(tr.FindNodeByKey(key).Node, False))
print('max:', tr.FinMinMax(tr.FindNodeByKey(key).Node, True))
# _________del___________
print('У_Д_А_Л_У_Н_И_Е')
# tr.DeleteNodeByKey(8)
tr.DeleteNodeByKey(5)
# tr.DeleteNodeByKey(11)
# tr.DeleteNodeByKey(16)
# tr.DeleteNodeByKey(1)
# tr.DeleteNodeByKey(14)
# tr.DeleteNodeByKey(10)
# tr.DeleteNodeByKey(2)
# tr.DeleteNodeByKey(0)
# tr.DeleteNodeByKey(3)
# tr.DeleteNodeByKey(4)
tr.DeleteNodeByKey(40)
print('Список:', tr.GetAllNodes(), end=' / ')
print('Кол-во:', tr.Count())
print(tr.FindNodeByKey(11).NodeHasKey)

'''
