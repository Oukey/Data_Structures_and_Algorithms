'''bazoon'''
class TreeNode:
    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree:
    def __init__(self):
        self.root = None

    def print_all(self):
        def aux(node):
            if node != None:
                aux(node.left_child)
                print(node.key)
                aux(node.right_child)

        aux(self.root)

    def add(self, key):

        def aux(root):
            if (root == None):
                root = TreeNode(self.root, key)
                if self.root == None:
                    self.root = root
            else:
                if (root.key <= key):
                    if root.right_child == None:
                        root.right_child = TreeNode(root, key)
                    else:
                        aux(root.right_child)
                else:
                    if root.left_child == None:
                        root.left_child = TreeNode(root, key)
                    else:
                        root.left_child = aux(root.left_child)

            return root

        aux(self.root)

    def find(self, key):
        def aux(node):
            if node is None:
                return None
            if node.key == key:
                return node

            if node.key < key:
                return aux(node.right_child)
            else:
                return aux(node.left_child)

        return aux(self.root)

    def find_max_from(self, node):
        if node is None or node.right_child is None:
            return node
        return self.find_max_from(node.right_child)

    def find_min_from(self, node):
        if node is None or node.left_child is None:
            return node
        return self.find_min_from(node.left_child)

    def remove_node(self, node):

        # no children
        if node.left_child is None and node.right_child is None:
            if node.parent != None:
                if node.parent.left_child == node:
                    node.parent.left_child = None
                else:
                    node.parent.right_child = None
        # have left child
        # Copy the child to the node and delete the child
        elif node.left_child != None and node.right_child is None:
            if node.parent != None:
                if node.parent.left_child == node:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child
        elif node.left_child is None and node.right_child != None:
            if node.parent != None:
                if node.parent.left_child == node:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child
        else:
            # two children
            successor = self.find_min_from(node.right_child)

            if successor.right_child != None:
                right_child = self.find_max_from(successor.right_child)
                right_child.right_child = node.right_child
                successor.parent.left_child = None
                if node.parent is None:
                    self.root = successor
            else:
                node.key = successor.key
                node.right_child = None

            successor.left_child = node.left_child


t = Tree()
# t.add(120)
# t.add(140)
# t.add(115)


t.add(40)
t.add(70)
t.add(60)
t.add(80)
t.add(65)
t.add(66)

a = t.find(80)
t.remove_node(a)
t.print_all()
# print(t.root.left_child.right_child.key)

# t.inorder(t.root)

# print(t.find_min_from(t.root))


'''Alviner'''
class TreeNode:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.value = value
        self.level = 1

    def __repr__(self):
        return f'Node({self.value})'


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self, node=None):
        if node is None:
            node = self.root
        yield node
        if node.left_child:
            for item in self.__iter__(node.left_child):
                yield item
        if node.right_child:
            for item in self.__iter__(node.right_child):
                yield item

    def __repr__(self, node=None):
        if node is None:
            node = self.root
        ret = ''
        if node.left_child:
            ret += self.__repr__(node.left_child)
        ret += node.__repr__()
        if node.right_child:
            ret += self.__repr__(node.right_child)
        return ret

    def reload(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.parent is None:
            node.level = 1
        else:
            node.level = node.parent.level + 1
        if node.left_child is not None:
            self.reload(node.left_child)
        if node.right_child is not None:
            self.reload(node.right_child)

    def add(self, node: TreeNode, parent=None):
        if parent is not None:
            is_exist, pos = False, 'right' if parent.right_child is None else 'left'
        else:
            parent, is_exist, pos = self.find(value=node.value)
        if not is_exist:
            if pos == 'right':
                node.parent = parent
                parent.right_child = node
                self.reload(parent.right_child)
                return parent.right_child
            elif pos == 'left':
                node.parent = parent
                parent.left_child = node
                self.reload(parent.left_child)
                return parent.left_child
            else:
                node.parent = None
                self.root = node
                return self.root

    def find(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node, False, '-'
        if value < node.value:
            if node.left_child is None:
                return node, False, 'left'
            return self.find(value, node.left_child)
        else:
            if node.value == value:
                return node, True, '-'

            if node.right_child is None:
                return node, False, 'right'
            return self.find(value, node.right_child)

    def remove(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.value > value:
            successor = self.remove(value, node.left_child)
            if successor is not None:
                successor.parent = node
            node.left_child = successor
        elif node.value < value:
            successor = self.remove(value, node.right_child)
            if successor is not None:
                successor.parent = node
            node.right_child = successor
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            temp = self.find_minimum(node.right_child)
            node.value = temp.value
            successor = self.remove(temp.value, node.right_child)
            successor.parent = node
            node.right_child = successor
        return node

    def find_minimum(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node
        if node.left_child is not None:
            return self.find_minimum(node.left_child)
        else:
            return node

    def find_maximum(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node
        if node.right_child is not None:
            return self.find_maximum(node.right_child)
        else:
            return node


def test_find():
    tree = BinaryTree()
    tree.add(TreeNode(8))
    tree.add(TreeNode(4))
    tree.add(TreeNode(12))
    tree.add(TreeNode(2))
    tree.add(TreeNode(6))
    tree.add(TreeNode(10))
    tree.add(TreeNode(14))

    node, is_exist, pos = tree.find(8)
    assert node == tree.root and is_exist and pos == '-'

    node, is_exist, pos = tree.find(2)
    assert node == tree.root.left_child.left_child and is_exist and pos == '-'

    node, is_exist, pos = tree.find(3)
    assert node == tree.root.left_child.left_child and not is_exist and pos == 'right'


def test_add():
    tree = BinaryTree()
    tree.add(TreeNode(8))
    tree.add(TreeNode(4))
    tree.add(TreeNode(12))
    tree.add(TreeNode(2))
    tree.add(TreeNode(6))
    tree.add(TreeNode(10))
    tree.add(TreeNode(14))

    assert tree.root.value == 8
    assert tree.root.left_child.value == 4
    assert tree.root.right_child.value == 12
    assert tree.root.left_child.left_child.value == 2
    assert tree.root.left_child.right_child.value == 6


def test_minmax():
    tree = BinaryTree()
    tree.add(TreeNode(8))
    tree.add(TreeNode(4))
    tree.add(TreeNode(12))
    tree.add(TreeNode(2))
    tree.add(TreeNode(6))
    tree.add(TreeNode(10))
    tree.add(TreeNode(14))

    assert tree.find_minimum().value == 2
    assert tree.find_maximum().value == 14
    assert tree.find_minimum(tree.root.right_child).value == 10
    assert tree.find_maximum(tree.root.left_child).value == 6


def test_remove():
    tree = BinaryTree()
    tree.add(TreeNode(8))
    tree.add(TreeNode(4))
    tree.add(TreeNode(12))
    tree.add(TreeNode(2))
    tree.add(TreeNode(6))
    tree.add(TreeNode(10))
    tree.add(TreeNode(14))
    tree.add(TreeNode(1))
    tree.add(TreeNode(3))
    tree.add(TreeNode(5))
    tree.add(TreeNode(7))
    tree.add(TreeNode(9))
    tree.add(TreeNode(11))
    tree.add(TreeNode(13))
    tree.add(TreeNode(15))

    tree.remove(8)
    assert tree.root.value == 9
    tree.remove(12)
    assert tree.root.right_child.value == 13
    tree.remove(1)
    assert tree.root.left_child.left_child.left_child is None
    assert tree.root.left_child.parent is tree.root
    assert tree.root.right_child.parent is tree.root


if __name__ == '__main__':
    test_find()
    test_add()
    test_minmax()
    test_remove()

'''Gexeg'''
import unittest


class Tree2Node:
    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree2:
    def __init__(self, key):
        self.root = Tree2Node(None, key)

    def find_node(self, value):
        """Поиск узла по значению"""
        current_node = self.root
        finded = False
        lr_child = None
        while True:
            if current_node.key == value:
                finded = True
                return current_node, finded, lr_child
            elif current_node.key < value:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    lr_child = 'right'
                    return current_node, finded, lr_child
            elif current_node.key > value:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    lr_child = 'left'
                    return current_node, finded, lr_child

    def add_node(self, key):
        """Добавление нового узла все, что больше - направо, все, что меньше - налево"""
        find_result = self.find_node(key)
        if find_result[1]:
            print('No duplicates allowed')
            return False
        if find_result[1] is False:
            if find_result[2] == 'right':
                find_result[0].right_child = Tree2Node(find_result[0], key)
                return
            elif find_result[2] == 'left':
                find_result[0].left_child = Tree2Node(find_result[0], key)
                return

    def min_max_node(self, mm, start_node):
        """Метод поиска максимального/минимального значения в дереве"""
        node = self.find_node(start_node)[0]
        if mm == 'min':
            while True:
                if node.left_child:
                    node = node.left_child
                else:
                    return node
        if mm == 'max':
            while True:
                if node.right_child:
                    node = node.right_child
                else:
                    return node

    def delete_node(self, key):
        """Удаление узла"""
        if self.root.key == key:
            print('Cannot delete root-node')
            return False
        elif self.find_node(key)[1]:
            node = self.find_node(key)[0]
        else:
            return False
        if node.right_child is None and node.left_child is None:
            if node.parent.right_child and node.parent.right_child.key == key:
                node.parent.right_child = None
                return
            if node.parent.left_child and node.parent.left_child.key == key:
                node.parent.left_child = None
                return
        elif node.right_child is None:
            if node.parent.right_child and node.parent.right_child.key == key:
                node.parent.right_child = node.left_child
                node.left_child.parent = node.parent
                return
            if node.parent.left_child and node.parent.left_child.key == key:
                node.parent.left_child = node.left_child
                node.left_child.parent = node.parent
                return
        else:
            new_node = node.right_child
            while True:
                if new_node.right_child is None and new_node.left_child is None:
                    if node.parent.right_child and node.parent.right_child.key == key:
                        node.parent.right_child = new_node
                        new_node.parent = node.parent
                        return
                    if node.parent.left_child and node.parent.left_child.key == key:
                        node.parent.left_child = None
                        new_node.parent = node.parent
                        return
                new_node = new_node.left_child


a_tree2 = Tree2(14)
a_tree2.add_node(15)
a_tree2.add_node(12)
a_tree2.add_node(18)
a_tree2.add_node(17)
a_tree2.add_node(5464)
a_tree2.add_node(22)
a_tree2.add_node(23)
a_tree2.add_node(21)
a_tree2.add_node(13)


class Ls13Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_min_max_node(self):
        self.assertEqual(a_tree2.min_max_node('min', 14).key, 12)
        self.assertEqual(a_tree2.min_max_node('max', 14).key, 5464)

    def test_delete_node(self):
        a_tree2.delete_node(23)
        self.assertEqual(a_tree2.find_node(23)[1], False)

    def tearDown(self):
        pass


unittest.main()

'''Safintim'''
from collections import namedtuple


class TreeNode2:

    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree2:

    def __init__(self):
        self.root = None
        self.current = self.root
        self.result_find = namedtuple('result_find', ['node', 'is_key', 'direct'])

    def preoder(self, root):
        yield root
        if root.left_child:
            yield from self.preoder(root.left_child)
        if root.right_child:
            yield from self.preoder(root.right_child)

    def __iter__(self):
        return self

    def find(self, key):
        # по сути это проверка только, когда дерево пусто
        if self.current is None:
            return self.result_find(self.current, False, None)
            # return [self.current, False, None]
        # если нашлась нода с таким же ключом
        elif self.current.key == key:
            return self.result_find(self.current, True, None)
            # return [self.current, True, None]
        elif key < self.current.key:
            '''если справа или слева пусто, то нужно запомнить родителя, чтобы после добавить к нему ноду'''
            if self.current.left_child is None:
                return self.result_find(self.current, False, 'left')
                # return [self.current, False, 'left']
            self.current = self.current.left_child
            return self.find(key)
        else:
            # key > self.current.key:
            if self.current.right_child is None:
                return self.result_find(self.current, False, 'right')
                # return [self.current, False, 'right']
            self.current = self.current.right_child
            return self.find(key)

    def add_node(self, n):
        f = self.find(n.key)
        # с индексами работать не особо удобно
        # node = f[0]
        # is_key = f[1]
        # direct = f[2]

        if f.node is None:
            self.root = n
        elif f.is_key:
            print('Такой ключ уже есть')
        else:
            if f.direct == 'right':
                f.node.right_child = n
                n.parent = f.node
            else:
                f.node.left_child = n
                n.parent = f.node
        self.current = self.root

    def max(self, node):
        f = self.find(node.key)
        self.current = self.root
        if f.is_key:
            temp = f.node.right_child
            while True:
                if temp.right_child is None:
                    return temp
                temp = temp.right_child
        else:
            print('Такой ноды нет')

    def min(self, node):
        f = self.find(node.key)
        self.current = self.root
        if f.is_key:
            temp = f.node.left_child
            while True:
                if temp.left_child is None:
                    return temp
                temp = temp.left_child
        else:
            print('Такой ноды нет')

    def remove_node(self, node):
        f = self.find(node.key)
        self.current = self.root
        if f.is_key:
            # минимальный "справа"
            min_node = self.min(f.node.right_child)
            # родителю минимального приемника левому ребру None
            min_node.parent.left_child = None
            # установить новому узлу "лево и право"
            min_node.left_child = f.node.left_child
            min_node.right_child = f.node.right_child
            # родителю удаляемого узла задать нового приемника
            f.node.parent.right_child = min_node
        else:
            print('Такой ноды нет')
