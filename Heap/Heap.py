# Модель кучи/пирамиды

class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.HeapSize = 0

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

    def MakeHeap(self, array, depth=None):  # основной вариант
        '''
        Метод создания массива кучи HeapArray из заданного массива 'a'
        Параметр 'depth' - глубина кучи
        '''
        if depth is None:
            self.HeapSize = self.Get_size_depth(array)[1]
        else:
            self.HeapSize = 2 ** (depth + 1) - 1
        for key in array:
            self.Add(key)

    def Add(self, key):
        '''
        Метод добавления нового элемента с ключем 'key' и перестройки кучи
        Возвращает True при добавлении или False если куча заполнена
        '''
        if len(self.HeapArray) < self.HeapSize:
            self.HeapArray.append(key)
            self.sift_up()
            return True
        else:
            return False

    def sift_up(self):
        '''Метод просеивание вверх'''
        ind = len(self.HeapArray) - 1
        while ind != 0:
            parent = (ind - 1) // 2
            if self.HeapArray[ind] <= self.HeapArray[parent]:
                break
            # if self.HeapArray[ind] > self.HeapArray[parent]:
            else:
                self.value_exchange(ind, parent)
                ind = parent

    def value_exchange(self, value_1, value_2):
        '''Метод обмена значениями двух элементов'''
        self.HeapArray[value_1], self.HeapArray[value_2] = self.HeapArray[value_2], self.HeapArray[value_1]

    def GetMax(self):
        '''
        Метод возврата корня (максимального значения) с дальнейшей перестройкой кучи
        Возвращает значение корня или -1 если куча пуста
        '''
        if len(self.HeapArray) == 0:
            return - 1
        else:
            max_elem = self.HeapArray[0]
            if len(self.HeapArray) > 1:
                self.HeapArray[0] = self.HeapArray.pop(-1)
                self.sift_down()
            elif len(self.HeapArray) == 1:
                self.HeapArray = []
            return max_elem

    def sift_down(self):
        '''Метод просеивания вниз'''
        ind = 0
        end = len(self.HeapArray) - 1
        while True:
            child = 2 * ind + 1
            if child > end:
                break
            if child + 1 <= end and self.HeapArray[child] < self.HeapArray[child + 1]:
                child += 1
            if self.HeapArray[ind] < self.HeapArray[child]:
                self.value_exchange(ind, child)
                ind = child
            else:
                break
