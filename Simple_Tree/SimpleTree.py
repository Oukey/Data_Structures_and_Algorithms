# модель дерева - необходимо тестировать и отлаживать!!!


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    # метод добавления нового дочернего узла существующему ParentNode
    def AddChild(self, ParentNode, NewChild):
        if self.Root is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)  # добавление нового узла в список дочерних узлов
            NewChild.Parent = ParentNode  # ссылка на родительский узел для нового узла

    # метод удаления существующего узла NodeToDelete
    def DeleteNode(self, NodeToDelete):
        if self.Root != NodeToDelete:
            NodeToDelete.Parent.Children.remove(NodeToDelete)  # почистить список детей в родительском узле
            NodeToDelete.Parent = None  # для удаляемого узла удалить ссылку на ролительский узел
            # NodeToDelete.Children = []  # обнулить список дочерних узлов

    # def traverse_tree(self, node):
    #     if node is not None:
    #         yield self
    #     else:
    #         yield node
    #     for child in self.Root:
    #         yield from self.traverse_tree(child)

    # def __iter__(self):
    #     return self

    # метод выдачи всех узлов дерева в определенном порядке
    # возвращает список узлов
    def GetAllNodes(self):
        Node_list = []
        if self.Root is not None:
            Node = self.Root
            Node_list.append(Node)
            for n in Node.Children:
                Node_list.append(n)
                for child in n.Children:
                    Node_list.append(child)
        return Node_list

    def FindNodesByValue(self, val):
        Node_value = []
        for node in self.GetAllNodes():
            if node.NodeValue == val:
                Node_value.append(node)
        return Node_value

    # Запасной вариант
    # def FindNodesByValue(self, val):
    #     Node_value = []
    #     for node in self.traverse_tree(self.Root):
    #         if node.NodeValue == val:
    #             Node_value.append(node)
    #     return Node_value

    # метод перемещения узла вместе с его поддеревом --
    # в качестве дочернего для узла NewParent
    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Childrem.append(OriginalNode)

    # метод посчета всех узлов в дереве
    # возвращает количество узлов
    def Count(self):
        count = 0
        for node in self.GetAllNodes():
            if len(node.Children) > 0:
                count += 1
        return count

    # метод подсчета листьев в дереве
    # возвращает количество конечных узлов
    def LeafCount(self):
        count_leaf = 0
        for node in self.GetAllNodes():
            if len(node.Children) == 0:
                count_leaf += 1
        return count_leaf
