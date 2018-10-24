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
        while node is not None:  # пока указатель на узел не равен None...
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
        if self.head is not None:
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
        ln = 0
        while node is not None:
            ln += 1
            node = node.next
        return ln

    def insert_node(self, val, num):  # метод добавление нового узла после заданного
        new_node = Node(val)  # создание узла c заданным значением (объект класса Node)
        node = self.head
        ln = 1  # счетчик узлов
        while node is not None:  # перебор узлов списка от головы до хвоста
            if ln == num:  # если номер узла в списке соответствует заданному значению...
                if node.next is not None:  # и если этот узел не последний
                    new_node.next = node.next  # определить указатель нового узла на следующий после найденного
                    node.next = new_node  # определить указатель найденного узла на новый
                else:  # если найденный узел является последним в списке...
                    node.next = new_node  # определить указатель найденного узла на новый
                    new_node.next = None  # указатель нового уза содержит None
                    new_node = self.tail  # новый узел указывает на хвост
            ln += 1  # увеличить счетчик узлов
            node = node.next  # перейти к следующему узлу для новой итерации цикла


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

'''
Задание № 1.7. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины
равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
'''


def comp_list(list_1, list_2):  # функция сравнения и суммирования двух св. списков
    final_list = LinkedList()  # создание пустого связанного списка
    node_1 = list_1.head  # указатель на первый узел первого списка
    node_2 = list_2.head  # указатель на первый узел второго списка
    if list_1.list_len() == list_2.list_len():  # если количество узлов в списках одинаковая...
        while node_1 is not None and node_2 is not None:  # выполни перебор списков от начала до конца
            #  добавь в пустой список сумму данных из узлов двух списков
            final_list.add_in_tail(Node(int(node_1.value + node_2.value)))
            node_1 = node_1.next  # переход к следующему узлу
            node_2 = node_2.next  # переход к следующему узлу
    else:  # иначе, если длины списков отличаются
        return  # верни None
    return final_list  # при положительном сравнении списков верни список сумм


# формирование двух списков для задания №1.7
L_1 = LinkedList()
L_2 = LinkedList()
L_1.add_in_tail(Node(1))
L_1.add_in_tail(Node(3))
L_1.add_in_tail(Node(5))
L_2.add_in_tail(Node(2))
L_2.add_in_tail(Node(4))
L_2.add_in_tail(Node(6))
