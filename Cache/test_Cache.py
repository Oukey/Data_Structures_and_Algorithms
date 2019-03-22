import unittest
import Cache


class CacheTest(unittest.TestCase):

    def test_norm(self):
        nc = Cache.NativeCache(3)
        nc.put('01', 10)
        nc.put('02', 20)
        nc.put('03', 30)
        self.assertEqual(nc.slots[0], '01')
        self.assertEqual(nc.slots[1], '02')
        self.assertEqual(nc.slots[2], '03')
        self.assertEqual(nc.values[0], 10)
        self.assertEqual(nc.values[1], 20)
        self.assertEqual(nc.values[2], 30)
        self.assertEqual(nc.hits[0], 1)
        self.assertEqual(nc.hits[1], 1)
        self.assertEqual(nc.hits[2], 1)

    def test_overhang(self):
        nc = Cache.NativeCache(3)
        nc.put('I', 1)
        nc.put('II', 2)
        nc.put('III', 3)
        nc.get('I')
        nc.get('II')
        nc.get('II')
        self.assertEqual(nc.hits[0], 3)
        self.assertEqual(nc.hits[1], 2)
        self.assertEqual(nc.hits[2], 1)
        nc.put('ololo', 'Oo')
        self.assertEqual(nc.slots[2], 'ololo')
        self.assertEqual(nc.values[2], 'Oo')

    if __name__ == '__main__':
        unittest.main()
