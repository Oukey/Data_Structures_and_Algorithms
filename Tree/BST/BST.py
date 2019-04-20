# модель бинарного дерева


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    '''метод формального обозначения объекта'''

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
        result = BSTFind()
        node = self.Root
        if node is None:
            return result
        else:
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
                        result.ToLeft = False
                    node = node.RightChild
        return result

    def AddKeyValue(self, key, val):
        '''
        Метод добавления ключа-значения в дерево
        key - кюч
        val - значение
        return False если ключ уже есть, или True если добовление выполнено
        '''
        node = self.FindNodeByKey(key)
        new_node = BSTNode(key, val, None)
        if self.Root is None:
            self.Root = new_node
            return True
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
        if FindMax:  # Если идет поиск узла с максимальным ключем
            while FromNode.RightChild:
                FromNode = FromNode.RightChild
        else:  # Если идет поиск узла с минимальным ключем
            while FromNode.LeftChild:
                FromNode = FromNode.LeftChild
        return FromNode

    def DeleteNodeByKey(self, key):
        '''
        Метод удаления узла по ключу
        key - ключ
        return False если ключ не найден, или True если удаление выполнено
        '''

        if self.FindNodeByKey(key).NodeHasKey is True:  # если в дереве найден узел с заданным ключем
            node = self.FindNodeByKey(key).Node
            # 0 если узел это корень дерева
            if node == self.Root:
                # 0.1 если у корня нет потомков
                if node.RightChild is None and node.LeftChild is None:
                    self.__init__(None)
                # 0.2 если есть оба узла: и левый, и правый
                elif node.RightChild and node.LeftChild:
                    rec = self.Find_receiver(node)
                    self.change_link(rec, None)
                    rec.Parent = None
                    node.NodeKey = rec.NodeKey
                    node.NodeValue = rec.NodeValue
                    if rec.RightChild:
                        node.RightChild = rec.RightChild
                else:  # 0.3 если есть один из двух потомков(левый или правый)
                    if node.RightChild:  # 0.3.1 если только правый
                        self.Root = node.RightChild
                        node.RightChild.Parent = None
                        node.RightChild = None
                    else:  # 0.3.2 если только левый
                        self.Root = node.LeftChild
                        node.LeftChild.Parent = None
                        node.LeftChild = None
            # 1 если есть первый и правый потомок
            elif node.RightChild and node.LeftChild:
                rec = self.Find_receiver(node)
                self.change_link(rec, None)
                rec.Parent = None
                node.NodeValue = rec.NodeValue
                node.NodeKey = rec.NodeKey
                if rec.RightChild:
                    node.RightChild = rec.RightChild
            # 2 если нет потомков
            elif node.RightChild is None and node.LeftChild is None:
                self.change_link(node, None)
                node.Parent = None
            # 3 если есть один потомок: или правый, или левый
            else:
                # 3.1 если только правый потомок
                if node.RightChild:  # если есть только правый наследник
                    self.change_link(node, node.RightChild)
                    node.RightChild.Parent = node.Parent
                    node.Parent = None
                    node.RightChild = None
                # 3.2 если есть только левый потомок
                else:
                    self.change_link(node, node.LeftChild)
                    node.LeftChild.Parent = node.Parent
                    node.Parent = None
                    node.LeftChild = None
        else:
            return False

    def Find_receiver(self, node_del):
        '''Метод определения приемника для метода удаления'''
        rec = node_del.RightChild
        while rec.LeftChild:
            if rec.LeftChild:
                rec = rec.LeftChild
                continue
            if rec.RightChild:
                rec = rec.RightChild
        return rec

    def change_link(self, node_del, node_child):
        '''метод изменения привязок узлов родителя и потомка'''
        if node_del.Parent.LeftChild == node_del:
            node_del.Parent.LeftChild = node_child
        else:
            node_del.Parent.RightChild = node_child

    def Count(self):
        '''
        Метод подсчета узлов в дереве, возвращает
        return целочисленное количество узлов
        '''
        return len(self.GetAllNodes())

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
