import unittest
import Heap as H


class HeapTest(unittest.TestCase):

    def test_norm_1(self):
        heap = H.Heap()
        self.assertEqual(heap.HeapSize, 0)
        self.assertEqual(heap.HeapArray, [])
        self.assertFalse(heap.Add(0))
        self.assertEqual(heap.GetMax(), -1)

    def test_norm_2(self):
        heap = H.Heap()
        a = []
        heap.MakeHeap(a)
        self.assertEqual(heap.HeapSize, 0)
        self.assertEqual(heap.HeapArray, [])
        self.assertFalse(heap.Add(0))
        self.assertEqual(heap.GetMax(), -1)

    def test_norm_3(self):
        heap = H.Heap()
        a = [0]
        heap.MakeHeap(a)
        self.assertEqual(heap.HeapSize, 3)
        self.assertEqual(heap.HeapArray, [0])
        self.assertTrue(heap.Add(0))
        self.assertEqual(heap.GetMax(), 0)

    def test_Add(self):
        heap = H.Heap()
        a = [0]
        heap.MakeHeap(a)
        self.assertTrue(heap.Add(1))
        self.assertTrue(heap.Add(2))
        self.assertFalse(heap.Add(3))
        heap.GetMax()
        self.assertTrue(heap.Add(3))

    def test_get_max(self):
        heap = H.Heap()
        a = [0, 1, 2, 3, 4, 5, 6]
        sample = [6, 5, 4, 3, 2, 1, 0]
        sort_list = []
        heap.MakeHeap(a)
        self.assertEqual(heap.HeapArray, [6, 3, 5, 0, 2, 1, 4])
        self.assertEqual(heap.HeapSize, 7)
        for el in range(heap.HeapSize):
            sort_list.append(heap.GetMax())
        self.assertEqual(sort_list, sample)



        heap.MakeHeap(a)

    if __name__ == '__main__':
        unittest.main()
        
