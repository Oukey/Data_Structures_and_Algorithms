# Модель кучи/пирамиды

class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, array, depth=None):
        '''
        Метод создания массива кучи HeapArray из заданного массива 'a'
        Параметр 'depth' - глубина кучи
        '''
        if depth is None:
            size = self.Get_size_depth(array)[1]
        else:
            size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * size
        for key in array:
            self.Add(key)

    def GetMax(self):
        '''
        Метод возврата корня (максимального значения) с дальнейшей перестройкой кучи
        Возвращает значение корня или -1 если куча пуста
        '''
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return - 1
        else:
            max_elem = self.HeapArray[0]
            self.HeapArray[0] = None
            if self.HeapArray[-1]:
                self.HeapArray[0], self.HeapArray[-1] = self.HeapArray[-1], self.HeapArray[0]
            else:
                ind = self.HeapArray.index(None) - 1
                self.HeapArray[0], self.HeapArray[ind] = self.HeapArray[ind], self.HeapArray[0]
            # sift_down
            ind = 0
            while self.HeapArray[2 * ind + 2]:
                left = 2 * ind + 1
                right = 2 * ind + 2
                if self.HeapArray[left] > self.HeapArray[right]:
                    max_key = left
                else:
                    max_key = right
                if self.HeapArray[ind] < self.HeapArray[max_key]:
                    self.HeapArray[ind], self.HeapArray[max_key] = self.HeapArray[max_key], self.HeapArray[ind]
                    ind = max_key
                else:
                    break
            return max_elem

    def Add(self, key):
        '''
        Метод добавления нового элемента с ключем 'key' и перестройки кучи
        Возвращает True при добавлении или False если куча заполнена
        '''
        if self.HeapArray[-1] is not None:
            return False  # если куча вся заполнена
        else:
            ind = self.HeapArray.index(None)
            self.HeapArray[ind] = key
            while ind != 0:
                parent = (ind - 1) // 2
                if self.HeapArray[ind] < self.HeapArray[parent]:
                    break
                if self.HeapArray[ind] > self.HeapArray[parent]:
                    self.HeapArray[ind], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[ind]
                ind = parent

            return True
    
    def Get_size_depth(self, array):  # дополнительный метод
        '''
        Метод расчета и возврата глубины и размера кучи по размеру массива array
        Возвращает кортеж с параметрами: 0 - глубина кучи, 1 - размер кучи
        '''
        if array:
            depth_heap = 0
            size_heap = 0
            while size_heap < len(array):
                depth_heap += 1
                size_heap = 2 ** (depth_heap + 1) - 1
            return depth_heap, size_heap
        else:
            return 0, 0

   
