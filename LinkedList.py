import unittest


# Связанный список.
# Состоит из отдельных узлов (данные + связь/ссылка на следующий узел)


class Node:  # класс Node определяет узел:
    def __init__(self, v):
        self.value = v  # данное
        self.next = None  # Next - связь (указатель на следующий узел. Для последнего next будет хранить None


n1 = Node(1)  # создание узла (объект класса Node)
n2 = Node(2)  # создание узла (объект класса Node)
n1.next = n2  # узлу n1 определить указатель на следующий узел n2


class LinkedList:  # Класс LinkedList определяет методы связанного списка
    def __init__(self):
        self.head = None  # указатель на голову (первый узел) списка
        self.tail = None  # указатель на хвост (завершающий узел) списка

    def add_in_tail(self, item):  # метод добавление нового узла в конец списка
        if self.head is None:  # если указатель на первый узел хранит None, т.е. список пуст
            self.head = item  # первым узлом станет новый узел item
        else:  # иначе, т.е. если связанный список уже содержит узлы...
            self.tail.next = item  # указатель на последний узел будет указывать на новый узел item
        self.tail = item  # В любом случае новый узел item будет последним узлом в списке

    def print_all_nodes(self):  # метод вывода всего списка для отладки
        node = self.head  # создание переменной, которая будет хранить указатель на голову списка
        print('[', end='')
        while node != None:  # пока указатель на узел не равен None...
            print(node.value, end=', ')  # выведи на экран значение указанного узла
            node = node.next  # сохрани в переменной указатель на следующий узел для следующей итерации
        print(']')

    def find(self, val):  # метод поиска узла по значению
        node = self.head  # создание переменной, которая будет хранить указатель на голову списка
        while node is not None:  # пока переменная не хранит None выполняется следующее:
            if node.value == val:  # если значение текущего узла равняется искомому значению...
                return node  # верни текущий узел
            node = node.next  # сохрани в переменной указатель на следующий узел для следующей итерации
        return None  # значение узлов не равно искомому значению верни None

    def del_nod(self, val):  # метод удаления узла с найденным значением
        if self.head != None:
            node = self.head
            if node.value == val:  # если значение найдено в головном узле
                self.head = node.next  # головой узла станет следующий узел
                node.next = None
                return
            while node.next is not None:
                if node.next.value == val and node.next.next is not None:  # если значение найдено в среднем узле
                    node.next = node.next.next  # перевести указатель предыдущего на следующий узел
                    return
                elif node.next.value == val and node.next.next is None:  # если значение найдено в хвостовом узле
                    self.tail = node  # предыдущий узел станет хвостовым
                    node.next = None
                    return
                node = node.next  # перейти к следующему узлу для новой итерации
        return

    def del_ever_nod(self, val):  # метод удаления всех узлов с найденными значениями
        node = self.head
        while node.next is not None:
            if node.next.value == val and node.next.next is not None:
                node.next = node.next.next
                continue
            elif node.next.value == val and node.next.next is None:
                self.tail = node
                node.next = None
                continue
            elif self.head.value == val:
                self.head = node.next
                continue
            node = node.next
        return

    def clear(self):  # метод очистки всего содержимого списка
        self.__init__()

    def find_all(self, val):  # метод поиска всех узлов по значению
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list.append(node.value)
            node = node.next
        return find_list

    def list_len(self):  # метод определения длинны списка
        node = self.head
        len = 0
        while node is not None:
            len += 1
            node = node.next
        return len

    def insert_node(self, val, num):  # метод добавление нового узла после заданного
        new_node = Node(val)
        node = self.head
        len = 1
        while node is not None:
            if len == num:
                new_node.next = node.next
                node.next = new_node
            len += 1
            node = node.next
        return


# формирование списка:
s_list = LinkedList()  # Создание пустого связанного списка
s_list.add_in_tail(n1)  # добавление узла n1 в хвост списка (пока ещё пустого)
s_list.add_in_tail(Node(1))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(n2)  # добавление узла n2 в хвост списка
s_list.add_in_tail(Node(3))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(4))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(1))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(2))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(3))  # добавление в конец списка новый узел (объект класса Node)
s_list.add_in_tail(Node(4))  # добавление в конец списка новый узел (объект класса Node)

print('Сформированный список:')
s_list.print_all_nodes()  # Вывод на экран всего связанного списка

nf = s_list.find(55)  # создание объекта, который будет хранить результаты метода поиска класса LinkedList
if nf is not None:  # если результаты поиска не хранят None...
    print('Результат поиска: ', nf.value)  # выведи данное(значение) узла

print('Удаление всех узлов с найденным значением:')
s_list.del_ever_nod(1)
s_list.print_all_nodes()

print('Удаление первого узла с найденным значением:')
s_list.del_nod(4)
s_list.print_all_nodes()

# s_list.clear() # удаление всех узлов списка

print('Найденные узлы:', s_list.find_all(4))

print('Список состоит из {} узлов'.format(s_list.list_len()))

print('После добавления узла:')
s_list.insert_node(100, 3)
s_list.print_all_nodes()

print('Задание № 1.7')
'''
1.7. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины
равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
'''


def comp_list(list_1, list_2):
    final_list = []
    if len(list_1) == len(list_2):
        for i in range(len(list_1)):
            final_list.append(list_1[i] + list_2[i])
    else:
        return
    return final_list


R = comp_list([1, 3, 5, 7, 9], [10, 8, 6, 4, 2])
if R is not None:
    print('Результирующий список:', R)
else:
    print('У списков разная длина...')


class test_comp_list(unittest.TestCase):
    def test_normal(self):
        remove = comp_list([1, 2, 3], [0, 1, 2])
        self.assertEqual(remove, [1, 3, 5])

    def test_unequal_len(self):
        remove = comp_list([1, 2], [1])
        self.assertEqual(remove, None)

    def test_negative_num(self):
        remove = comp_list([1, -1], [-10, -10])
        self.assertEqual(remove, [-9, -11])


if __name__ == '__main__':
    unittest.main()
