# Модель кучи/пирамиды

class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        '''
        Метод создания массива кучи HeapArray из заданного массива 'a'
        Параметр 'depth' - глубина кучи
        '''
        # depth = self. Get_size_depth(a)[0]
        self.HeapArray = [None] * self.Get_size_depth(a)[1]
        for node in a:
            self.Add(node)

    def GetMax(self):
        '''
        Метод возврата корня (максимального значения) с дальнейшей перестройкой кучи
        Возвращает значение корня или -1 если куча пуста
        '''
        return -1  # если куча пуста

    def Add(self, key):
        '''
        Метод добавления нового элемента с ключем 'key' и перестройки кучи
        Возвращает True при добавлении или False если куча заполнена
        '''
        # добавляем новый элемент key в кучу и перестраиваем её
        return False  # если куча вся заполнена
    
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

    def move_up(self):  # дополнительный метод
        '''Метод перемещения элемента вверх'''
        pass

    def move_sown(self):  # дополнительный метод
        '''Метод перемещения элемента вниз'''
        pass
