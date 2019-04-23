import unittest
import aBST


class aBSTTest(unittest.TestCase):

    def test_norm(self):  # проверка правильности расчета размера массива
        tr = aBST.aBST(0)
        self.assertEqual(len(tr.Tree), 1)
        tr = aBST.aBST(1)
        self.assertEqual(len(tr.Tree), 3)
        tr = aBST.aBST(2)
        self.assertEqual(len(tr.Tree), 7)
        tr = aBST.aBST(3)
        self.assertEqual(len(tr.Tree), 15)
        tr = aBST.aBST(4)
        self.assertEqual(len(tr.Tree), 31)

    def test_Find(self):
        tr = aBST.aBST(2)
        self.assertEqual(tr.FindKeyIndex(50), 0)  # возвращает индекс 0 при пустом дереве
        self.assertEqual(tr.AddKey(50), 1)
        tr.AddKey(50)
        self.assertEqual(tr.AddKey(50), -1)
        self.assertEqual(tr.FindKeyIndex(50), 0)  # возвращает -1 если
        self.assertEqual((tr.FindKeyIndex(25)), -1)
        self.assertEqual((tr.FindKeyIndex(75)), -2)

    if __name__ == '__main__':
        unittest.main()
