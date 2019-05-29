import unittest
import Even_Trees as Tree


class EvenTest(unittest.TestCase):

    @staticmethod
    def Creat_tree():
        rt = Tree.SimpleTreeNode(1, None)
        ch2 = Tree.SimpleTreeNode(2, None)
        ch3 = Tree.SimpleTreeNode(3, None)
        ch4 = Tree.SimpleTreeNode(4, None)
        ch5 = Tree.SimpleTreeNode(5, None)
        ch6 = Tree.SimpleTreeNode(6, None)
        ch7 = Tree.SimpleTreeNode(7, None)
        ch8 = Tree.SimpleTreeNode(8, None)
        ch9 = Tree.SimpleTreeNode(9, None)
        ch10 = Tree.SimpleTreeNode(10, None)
        tree = Tree.SimpleTree(rt)
        tree.AddChild(tree.Root, ch2)
        tree.AddChild(tree.Root, ch3)
        tree.AddChild(tree.Root, ch6)
        tree.AddChild(ch2, ch5)
        tree.AddChild(ch2, ch7)
        tree.AddChild(ch3, ch4)
        tree.AddChild(ch6, ch8)
        tree.AddChild(ch8, ch9)
        tree.AddChild(ch8, ch10)
        return tree

    @staticmethod
    def list_value(node_value):
        val_list = []
        for node in node_value:
            val_list.append(node.NodeValue)
        return val_list

    def test_Event_Trees(self):
        tree = self.Creat_tree()
        self.assertEqual(self.list_value(tree.EvenTrees()), [1, 3, 1, 6])
        self.assertEqual(self.list_value(tree.GetAllNodes()), [1, 2, 5, 7, 3, 4, 6, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
