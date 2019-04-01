# модель дерева


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        # метод добавления нового дочернего узла существующему ParentNode
        if NewChild is not ParentNode:
            ParentNode.Children.append(NewChild)  # добавление в список дочерних узлов
            NewChild.Parent = ParentNode  # ссылка на родительскую ветвь для нового узла

    def DeleteNode(self, NodeToDelete):
        # метод удаления существующего узла NodeToDelete
        # ВОПРОС!!! Удалять ли дочерние узлы уза???
        if NodeToDelete.Parent is not None:
            parent = NodeToDelete  # определение переменной, хранящей ссылку на родительский узел
            parent.Children.remove(NodeToDelete)  # для родительского узла удалить заданный дочерний узел
            NodeToDelete.Parent = None  # удалить ссылку на родительский узел
            NodeToDelete.Children = []  # обнулить список дочерних узлов

    def GetAllNodes(self):
        # метод выдачи всех узлов дерева в определенном порядке
        # возвращает список узлов, какой порядок?
        return []

    def FindNodesByValue(self, val):
        # метод поиска узлов по значению
        # возвращает список узлов?
        return []

    def MoveNode(self, OriginalNode, NewParent):
        # метод перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        # метод посчета всех узлов в дереве
        # возвращает количество узлов
        return 0

    def LeafCount(self):
        # метод подсчета листьев в дереве
        # возвращает количество конечных узлов
        return 0
