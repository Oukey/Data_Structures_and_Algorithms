import ctypes


class DynArray:
    def __init__(self):
        self.count = 0  # счетчик текущего количества элементов в массиве
        self.capacity = 16  # вместительность, текущая емкость буфера
        self.array = self.make_array(self.capacity)  # массив, указатель на блок памяти

    def __len__(self):  # метод определения длинны массива
        return self.count

    def make_array(self, new_capacity):  # метод формирование блока памяти
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):  # метод индексации класса
        if i < 0 or i >= self.count:  # проверка корректности индекса в рамках границ
            raise IndexError('Index is out of bounds')  # генерация исключения IndexError
        return self.array[i]

    def resize(self, new_capacity):  # метод изменения размера внутреннего буфера
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):  # метод добавления элемента в конец массива
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    '''
    4.1. Добавьте елемент insert(i, itm), который вставляет в i-ю позицию объект itm, сдвигая вперёд все последующие 
    элементы. Учтите, что новая длина массива может привысить размер буфера.
    '''

    def insert(self, i, itm):
        new_array = []
        for el in range(self.count):
            if self.count == self.capacity:
                self.resize(2 * self.capacity)
            elif el == i:
                new_array.append(itm)
                self.count += 1
            new_array.append(el)
        self.array = new_array
        return self.array

    '''
    4.2. Добавьте метод delete(i), который удаляет объект из i-й позициию Если количество элементов массива стало в 
    два или более раз меньше его потенциальной ёмкости, выполните сжатие буфера, сохраняя минимальную ёмкость 
    16 элементов.
    '''

    def delete(self, ind):
        new_array = []
        for el in range(self.count):
            if el == ind:
                self.count -= 1
                continue
            elif self.capacity / self.count >= 2 and self.capacity / 2 > 16:
                self.capacity /= 2
            new_array.append(self.array[el])
        self.array = new_array
        return self.array


da = DynArray()
for i in range(2):
    da.append(i)
    print(da[i])

da.insert(1, 111)
for i in da:
    print(i)

da.delete(0)
for i in da:
    print(i)
