# Модель дерева


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = 0

    def get_level(self):
        ''' метод определения и возврата уровня узла в дереве '''
        if self.Parent is None:
            self.level = 0
        else:
            self.level = self.Parent.level + 1
        return self.level

    def __repr__(self):
        ''' метод формального обозначения объекта '''
        return 'Node_{}'.format(self.NodeValue)


class SimpleTree:

    def __init__(self, root):
        '''Root - корень дерева, может быть None'''
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        '''
        метод добавления нового дочернего узла существующему
        ParentNode - существующий узел
        NewChild - новый дочерний узел
        return True если добавление выполнено, иначе return False
        '''
        if self.Root != NewChild:
            # if self.Root != NewChild and ParentNode in self.GetAllNodes():
            if self.Root is None:
                self.Root = NewChild
            else:
                ParentNode.Children.append(NewChild)
                NewChild.Parent = ParentNode
            return True
        return False

    def DeleteNode(self, NodeToDelete):
        '''
        метод удаления существующего узла NodeToDelete
        return True если удаление выполнено, иначе return False
        '''
        if self.Root != NodeToDelete and NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
            return True
        return False

    def search_nodes(self, node):
        ''' генератор '''
        if node is not None:
            yield node
            for child in node.Children:
                yield from self.search_nodes(child)

    def __iter__(self):
        return self

    def GetAllNodes(self):
        ''' метод возврата всех узлов дерева в виде списка '''
        node_list = []
        for node in self.search_nodes(self.Root):
            node_list.append(node)
        return node_list

    def FindNodesByValue(self, val):
        ''' Метод поиска узлов по значению val. Возвращает список найденных узов '''
        node_val = []
        for node in self.search_nodes(self.Root):
            if node.NodeValue == val:
                node_val.append(node)
        return node_val

    def MoveNode(self, OriginalNode, NewParent):
        '''
        метод перемещения узла вместе с поддеревом
        OriginalNode - переносимый узел
        NewParent - узел привязки
        return True если перемещение выполнено, иначе return False
        '''
        if OriginalNode != self.Root and NewParent not in self.search_nodes(OriginalNode):
            OriginalNode.Parent.Children.remove(OriginalNode)
            OriginalNode.Parent = NewParent
            NewParent.Children.append(OriginalNode)
            return True
        return False

    def Count(self):
        ''' метод возвращает целочисленное количество узлов в дереве '''
        return int(len(self.GetAllNodes()))

    def LeafCount(self):
        ''' метод возвращает целочисленное количество листьев в дереве '''
        count_leaf = int(0)
        for node in self.GetAllNodes():
            if len(node.Children) == 0:
                count_leaf += 1
        return count_leaf
