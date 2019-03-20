import unittest
import Set


class PoserSetTest(unittest.TestCase):

    def test_norm(self):
        st_1 = Set.PowerSet()
        self.assertEqual(st_1.size(), 0)
        st_1.put(10)
        st_1.put(11)
        st_1.put(10)
        self.assertTrue(st_1.get(10), st_1.get(11))
        self.assertEqual(st_1.size(), 2)
        st_1.remove(12)
        self.assertEqual(st_1.size(), 2)
        st_1.remove(10)
        self.assertFalse(st_1.get(10))

    def test_intersection(self):
        st_1 = Set.PowerSet()
        st_2 = Set.PowerSet()
        st_1.put(1)
        st_1.put(3)
        st_2.put(2)
        st_2.put(4)
        st_3 = st_1.intersection(st_2)
        self.assertEqual(st_3.size(), 0)
        st_1.put(5)
        st_2.put(5)
        st_3 = st_1.intersection(st_2)
        self.assertEqual(st_3.size(), 1)

    def test_union(self):
        st_1 = Set.PowerSet()
        st_2 = Set.PowerSet()
        st_2.put(8)
        st_2.put(8.1)
        st_3 = st_1.union(st_2)
        self.assertEqual(st_3.size(), 2)
        st_3.put(8.2)
        st_3.put(8.3)
        st_4 = st_2.union(st_3)
        self.assertEqual(st_4.size(), 4)

    def test_difference(self):
        st_1 = Set.PowerSet()
        st_2 = Set.PowerSet()
        st_1.put(5)
        st_2.put(5)
        st_3 = st_1.difference(st_2)
        self.assertEqual(st_3.size(), 0)
        st_1.put(7)
        st_1.put(9)
        st_2.put(3)
        st_2.put(9)
        st_3 = st_1.difference(st_2)
        self.assertFalse(st_3.get(9))

    def test_issubset(self):
        st_1 = Set.PowerSet()
        st_2 = Set.PowerSet()
        st_1.put(1)
        st_1.put(3)
        st_2.put(1)
        st_2.put(3)
        self.assertTrue(st_1.issubset(st_2))
        st_1.put(2)
        self.assertFalse(st_2.issubset(st_1))
        st_2.put(2)
        self.assertTrue(st_2.issubset(st_1))

    if __name__ == '__main__':
        unittest.main()
