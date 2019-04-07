# модель дерева

class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = 0

    def get_level(self):  # метод определения уровня
        if self.Parent is None:
            self.level = 0
        else:
            self.level = self.Parent.level + 1
        return self.level

    # метод формального обозначения объектов
    def __repr__(self):
        return 'Node {}'.format(self.NodeValue)


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    # метод добавления нового дочернего узла существующему ParentNode
    def AddChild(self, ParentNode, NewChild):
        if self.Root == NewChild:
            raise Exception('Попытка удаления корневого узла!')
        if self.Root is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    # метод удаления существующего узла NodeToDelete
    def DeleteNode(self, NodeToDelete):
        if self.Root == NodeToDelete:
            raise Exception('Попытка удаления корневого узла!')
        if NodeToDelete.Parent is None:
            raise Exception('Отсутствует указатель на родительский узел!')
        if self.Root != NodeToDelete:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

            # генератор

    def search_nodes(self, node):
        if self.Root is not None:
            yield node
            for child in node.Children:
                yield from self.search_nodes(child)

    def __iter__(self):
        return self

    # метод выдачи всех узлов дерева в определенном порядке
    def GetAllNodes(self):
        Node_list = []
        for node in self.search_nodes(self.Root):
            Node_list.append(node)
        return Node_list

    def FindNodesByValue(self, val):
        Value_list = []
        for node in self.search_nodes(self.Root):
            if node.NodeValue == val:
                Value_list.append(node)
        return Value_list

    # метод перемещения узла вместе с его поддеревом --
    # в качестве дочернего для узла NewParent
    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode is not self.Root:
            OriginalNode.Parent.Children.remove(OriginalNode)
            OriginalNode.Parent = NewParent
            NewParent.Children.append(OriginalNode)
            return True
        return False

    # метод подсчета всех узлов в дереве
    def Count(self):
        count = 0
        if len(self.Root.Children) == 0 and len(self.GetAllNodes()) == 1:
            count = 1
            return count
        for node in self.GetAllNodes():
            # if len(node.Children) >= 1:
            if node.Children:
                count += 1
        return count

    # метод подсчета листьев в дереве
    def LeafCount(self):
        count_leaf = 0
        if len(self.Root.Children) == 0 and len(self.GetAllNodes()) == 1:
            return count_leaf

        for node in self.GetAllNodes():
            if len(node.Children) == 0:
                count_leaf += 1
        return count_leaf
