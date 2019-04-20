import unittest
import new_BST


class BSTTest(unittest.TestCase):

    def creat_tree(self):
        '''
                5
              /   \
            3      8
        '''
        tree = new_BST.BST(None)
        tree.AddKeyValue(5, 500)
        tree.AddKeyValue(8, 80)
        tree.AddKeyValue(3, 33)
        return tree

    def test_norm(self):
        tree = new_BST.BST(None)
        self.assertIsNone(tree.Root)
        self.assertEqual(tree.Count(), 0)
        self.assertIsNone(tree.FindNodeByKey(10).Node)
        tree.AddKeyValue(5, 50)
        tree.AddKeyValue(3, 30)
        tree.AddKeyValue(8, 80)
        self.assertEqual(tree.Count(), 3)
        self.assertEqual(tree.Root.NodeKey, 5)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 3)
        self.assertEqual(tree.Root.RightChild.NodeKey, 8)

    def test_FindNodeByKey(self):
        tree = self.creat_tree()
        self.assertEqual(tree.Count(), 3)
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
        self.assertEqual(tree.Count(), 5)

    def test_FinMinMax(self):
        tree = self.creat_tree()
        self.assertEqual(tree.FinMinMax(tree.Root, True), tree.Root.RightChild)
        self.assertEqual(tree.FinMinMax(tree.Root, False), tree.Root.LeftChild)
        tree.AddKeyValue(1, '1')
        tree.AddKeyValue(4, '4')
        tree.AddKeyValue(7, '7')
        tree.AddKeyValue(10, '10')
        self.assertEqual(tree.FinMinMax(tree.Root.LeftChild, True), tree.FindNodeByKey(4).Node)
        self.assertEqual(tree.FinMinMax(tree.Root.LeftChild, False), tree.FindNodeByKey(1).Node)
        self.assertEqual(tree.FinMinMax(tree.Root.RightChild, True), tree.FindNodeByKey(10).Node)
        self.assertEqual(tree.FinMinMax(tree.Root.RightChild, False), tree.FindNodeByKey(7).Node)

    def test_delete(self):
        tree = new_BST.BST(None)
        self.assertFalse(tree.DeleteNodeByKey(None))
        tree.AddKeyValue(5, '55')  # 1
        tree.AddKeyValue(3, 3)  # 2
        tree.AddKeyValue(8, 8)  # 3
        tree.AddKeyValue(2, 2)  # 4
        tree.AddKeyValue(4, 4)  # 5
        tree.AddKeyValue(1, 1)  # 6
        tree.AddKeyValue(7, 7)  # 7
        tree.AddKeyValue(10, 10)  # 8
        tree.AddKeyValue(9, 9)  # 9
        tree.AddKeyValue(6, 6)  # 10
        tree.AddKeyValue(0, 0)  # 11
        tree.AddKeyValue(11, 0)  # 12
        tree.AddKeyValue(12, 0)  # 13
        self.assertEqual(tree.Count(), 13)
        tree.DeleteNodeByKey(8)
        self.assertEqual(tree.Count(), 12)
        self.assertFalse(tree.FindNodeByKey(8).NodeHasKey)
        tree.DeleteNodeByKey(3)
        self.assertEqual(tree.Count(), 11)
        self.assertFalse(tree.FindNodeByKey(3).NodeHasKey)
        tree.DeleteNodeByKey(0)
        self.assertEqual(tree.Count(), 10)
        self.assertFalse(tree.FindNodeByKey(0).NodeHasKey)
        tree.DeleteNodeByKey(9)
        self.assertEqual(tree.Count(), 9)
        self.assertFalse(tree.FindNodeByKey(9).NodeHasKey)
        tree.DeleteNodeByKey(4)
        self.assertEqual(tree.Count(), 8)
        self.assertFalse(tree.FindNodeByKey(4).NodeHasKey)
        tree.DeleteNodeByKey(12)
        self.assertEqual(tree.Count(), 7)
        self.assertFalse(tree.FindNodeByKey(12).NodeHasKey)
        tree.DeleteNodeByKey(10)
        self.assertEqual(tree.Count(), 7)
        self.assertFalse(tree.FindNodeByKey(10).NodeHasKey)
        tree.DeleteNodeByKey(6)
        self.assertEqual(tree.Count(), 6)
        self.assertFalse(tree.FindNodeByKey(6).NodeHasKey)
        tree.DeleteNodeByKey(5)
        self.assertEqual(tree.Count(), 5)
        self.assertFalse(tree.FindNodeByKey(5).NodeHasKey)
        tree.DeleteNodeByKey(7)
        self.assertEqual(tree.Count(), 4)
        self.assertFalse(tree.FindNodeByKey(7).NodeHasKey)
        tree.DeleteNodeByKey(1)
        self.assertEqual(tree.Count(), 3)
        self.assertFalse(tree.FindNodeByKey(1).NodeHasKey)
        tree.DeleteNodeByKey(2)
        self.assertEqual(tree.Count(), 2)
        self.assertFalse(tree.FindNodeByKey(2).NodeHasKey)

    if __name__ == '__main__':
        unittest.main()
