import unittest
import Cache_1


class CacheTest(unittest.TestCase):

    def test_norm(self):
        nc = Cache_1.NativeCache(3)
        nc.put('01', 10)
        nc.put('02', 20)
        nc.put('03', 30)
        slot_0 = nc.find('01')
        slot_1 = nc.find('02')
        slot_2 = nc.find('03')
        self.assertEqual(nc.slots[slot_0], '01')
        self.assertEqual(nc.slots[slot_1], '02')
        self.assertEqual(nc.slots[slot_2], '03')
        self.assertEqual(nc.values[slot_0], 10)
        self.assertEqual(nc.values[slot_1], 20)
        self.assertEqual(nc.values[slot_2], 30)
        self.assertEqual(nc.hits[slot_0], 1)
        self.assertEqual(nc.hits[slot_1], 1)
        self.assertEqual(nc.hits[slot_2], 1)

    def test_overhang(self):
        nc = Cache_1.NativeCache(3)
        nc.put('I', 1)
        nc.put('II', 2)
        nc.put('III', 3)
        nc.get('I')
        nc.get('II')
        nc.get('II')
        slot_0 = nc.find('I')
        slot_1 = nc.find('II')
        slot_2 = nc.find('III')
        self.assertEqual(nc.hits[slot_2], 1)
        self.assertEqual(nc.hits[slot_1], 3)
        self.assertEqual(nc.hits[slot_0], 2)
        nc.put('ololo', 'Oo')
        slot = nc.find('ololo')
        self.assertEqual(nc.slots[slot], 'ololo')
        self.assertEqual(nc.values[slot], 'Oo')

    if __name__ == '__main__':
        unittest.main()

