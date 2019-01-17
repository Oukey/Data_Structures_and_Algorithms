import unittest

import Dyn_Array

'''
4.4.4. Напишите тесты, проверяющие работу методов insert() и delete():
-- вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);
-- вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);
-- попытка вставки элемента в недопустимую позицию;
-- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);
-- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);
-- попытка удаления элемента в недопустимой позиции.
'''

class DynArrayTest(unittest.TestCase):
    def test_insert1(self):  # тест вставки элемента без превышения буфера
        d_a = Dyn_Array.DynArray()
        for i in range(10):
            d_a.append(i)
        buffer = d_a.capacity
        d_a.insert(2, 100)
        new_buffer = d_a.capacity
        self.assertEqual(d_a[2], 100)
        self.assertEqual(buffer, new_buffer)

    def test_insert2(self):  # тест вставки элемента с превышением буфера
        d_a = Dyn_Array.DynArray()
        for i in range(16):
            d_a.append(i)
        buffer = d_a.capacity
        d_a.insert(10, 100)
        new_buffer = d_a.capacity
        self.assertEqual(d_a[10], 100)
        self.assertNotEqual(buffer, new_buffer)
        self.assertEqual(new_buffer, 32)

    def test_delete1(self):  # тест удаления без изменения размера буфера
        d_a = Dyn_Array.DynArray()
        for i in range(10):
            d_a.append(i)
        buffer = d_a.capacity
        d_a.delete(2)
        new_buffer = d_a.capacity
        self.assertNotEqual(d_a[2], 2)
        self.assertEqual(buffer, new_buffer)

    def test_delete2(self):  # тест удаления с изменением объема буфера
        d_a = Dyn_Array.DynArray()
        for i in range(36):
            d_a.append(i)
        buffer = d_a.capacity
        d_a.delete(35)
        new_buffer = d_a.capacity
        self.assertNotEqual(buffer, new_buffer)
        self.assertEqual(new_buffer, 48)

    if __name__ == '__main__':
        unittest.main()
