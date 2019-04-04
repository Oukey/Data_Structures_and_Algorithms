# модель дерева

class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    # для тестов!!!
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
            ParentNode.Children.append(NewChild)  # добавление нового узла в список дочерних узлов
            NewChild.Parent = ParentNode  # ссылка на родительский узел для нового узла

    # метод удаления существующего узла NodeToDelete
    def DeleteNode(self, NodeToDelete):
        if self.Root == NodeToDelete:
            raise Exception('Попытка удаления корневого узла!')
        if NodeToDelete.Parent is None:
            raise Exception('Отсутствует указатель на родительский узел!')
        if self.Root != NodeToDelete:
            NodeToDelete.Parent.Children.remove(NodeToDelete)  # почистить список детей в родительском узле
            NodeToDelete.Parent = None  # для удаляемого узла удалить ссылку на ролительский узел
            # NodeToDelete.Children = []  # обнулить список дочерних узлов

    # генератор
    def search_nodes(self, node):
        yield node
        for child in node.Children:
            yield from self.search_nodes(child)

    # def __iter__(self):
    #     return self

    # метод выдачи всех узлов дерева в определенном порядке
    # возвращает список узлов
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
        if OriginalNode is not NewParent:
            OriginalNode.Parent.Children.remove(OriginalNode)
            OriginalNode.Parent = NewParent
            NewParent.Children.append(OriginalNode)

    # метод посчета всех узлов в дереве
    # возвращает количество узлов
    def Count(self):
        count = 0
        for node in self.GetAllNodes():
            # if len(node.Children) >= 1:
            if node.Children:
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


rt = SimpleTreeNode(0, None)

ch1 = SimpleTreeNode(1, None)
ch2 = SimpleTreeNode(2, None)
ch3 = SimpleTreeNode(3, None)
ch4 = SimpleTreeNode(4, None)
ch5 = SimpleTreeNode(5, None)
ch6 = SimpleTreeNode(6, None)
ch7 = SimpleTreeNode(7, None)
ch8 = SimpleTreeNode(8, None)
ch9 = SimpleTreeNode(9, None)
ch10 = SimpleTreeNode(10, None)
ch11 = SimpleTreeNode(11, None)
ch12 = SimpleTreeNode(12, None)

tree = SimpleTree(rt)

tree.AddChild(rt, ch1)
tree.AddChild(rt, ch2)
tree.AddChild(ch1, ch3)
tree.AddChild(ch1, ch4)
tree.AddChild(ch2, ch5)
tree.AddChild(ch2, ch6)
tree.AddChild(ch3, ch7)
tree.AddChild(ch3, ch8)
tree.AddChild(ch5, ch9)
tree.AddChild(ch5, ch10)
tree.AddChild(ch6, ch11)
# tree.DeleteNode(ch11)
for i in tree.Root.Children:
    print(i.NodeValue)
tree.MoveNode(ch10, ch4)

print(tree.GetAllNodes())
print('узлы', tree.Count())
print('листья', tree.LeafCount())



'''
0 --                 rt(0)
                   /       \
1 --           ch1          ch2
              /   \       /    \
2 --       ch3    ch4   ch5    ch6
         /   \        /  \      \
3 --   ch7    ch8   ch9   ch10    ch11
'''
