import unittest
import BST


class BSTTest(unittest.TestCase):

    def creat_tree(self):
        '''
                5
              /   \
            3      8
        '''
        tree = BST.BST(None)
        tree.AddKeyValue(5, 500)
        tree.AddKeyValue(8, 80)
        tree.AddKeyValue(3, 33)
        return tree

    def test_norm(self):
        tree = BST.BST(None)
        self.assertIsNone(tree.Root)
        self.assertIsNone(tree.FindNodeByKey(10))
        tree.AddKeyValue(5, 50)
        tree.AddKeyValue(3, 30)
        tree.AddKeyValue(8, 80)
        self.assertEqual(tree.Root.NodeKey, 5)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 3)
        self.assertEqual(tree.Root.RightChild.NodeKey, 8)

    def test_FindNodeByKey(self):
        tree = self.creat_tree()
        find_r = tree.FindNodeByKey(50)
        self.assertFalse(find_r.NodeHasKey)
        self.assertEqual(tree.Root.RightChild, find_r.Node)
        self.assertFalse(find_r.ToLeft)
        find_l = tree.FindNodeByKey(2)
        self.assertFalse(find_l.NodeHasKey)
        self.assertEqual(tree.Root.LeftChild, find_l.Node)
        self.assertTrue(find_l.ToLeft)
        find = tree.FindNodeByKey(5)
        self.assertEqual(find.Node, tree.Root)
        self.assertTrue(find.NodeHasKey)
        self.assertFalse(find_r.ToLeft)

    def test_add(self):
        tree = self.creat_tree()
        self.assertFalse(tree.FindNodeByKey(7).NodeHasKey)
        tree.AddKeyValue(7, 700)
        self.assertTrue(tree.FindNodeByKey(7).NodeHasKey)
        self.assertFalse(tree.FindNodeByKey(4).NodeHasKey)
        tree.AddKeyValue(4, 45)
        self.assertTrue(tree.FindNodeByKey(4).NodeHasKey)
        tree.AddKeyValue(5, 505050)
        self.assertNotEqual(tree.Root.NodeValue, 505050)


    if __name__ == '__main__':
        unittest.main()
