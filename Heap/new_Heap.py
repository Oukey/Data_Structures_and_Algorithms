# Модель кучи/пирамиды

class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, array, depth):
        '''
        Метод создания массива кучи HeapArray из заданного массива 'a'
        Параметр 'depth' - глубина кучи
        '''
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
            if self.HeapArray[-1]:
                ind = self.HeapArray[0]
            else:
                ind = self.HeapArray.index(None) - 1
                self.HeapArray[0] = None
                self.HeapArray[0], self.HeapArray[ind] = self.HeapArray[ind], self.HeapArray[0]

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

    # def move_up(self):  # дополнительный метод
    #     '''Метод перемещения элемента вверх'''
    #     pass
    #
    # def move_sown(self):  # дополнительный метод
    #     '''Метод перемещения элемента вниз'''
    #     pass


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = Heap()
n.MakeHeap(a, 3)
n.Add(11)
n.Add(12)
n.Add(13)
n.Add(14)
# n.Add(15)
print(n.GetMax())

print(n.HeapArray)

# print(m.index(None))
