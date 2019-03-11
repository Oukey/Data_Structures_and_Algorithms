# тесты к модели соваря


import unittest
import NativeDictionary


class NativeDictionaryTest(unittest.TestCase):

    def test_norm(self):
        nd = NativeDictionary.NativeDictionary(5)
        count = 0
        for i in nd.slots_key:
            if i is None:
                count += 1
        self.assertEqual(count, 5)
        count = 0
        nd.put('01', 1321961)
        for i in nd.slots_key:
            if i is None:
                count += 1
        self.assertEqual(count, 4)

    def test_put(self):
        nd = NativeDictionary.NativeDictionary(5)
        nd.put(1, 1)
        self.assertEqual(nd.get(1), 1)
        nd.put(1, 10)
        self.assertEqual(nd.get(1), 10)

    def test_is_key(self):
        nd = NativeDictionary.NativeDictionary(5)
        self.assertFalse(nd.is_key(1))
        nd.put(1, 'new_value')
        self.assertTrue(nd.is_key(1))
        self.assertFalse(nd.is_key(4))

    def test_get(self):
        nd = NativeDictionary.NativeDictionary(4)
        nd.put('1', 'val')
        self.assertEqual(nd.get('1'), 'val')
        self.assertNotEqual(nd.get(1), 'val')

    if __name__ == '__main__':
        unittest.main()
