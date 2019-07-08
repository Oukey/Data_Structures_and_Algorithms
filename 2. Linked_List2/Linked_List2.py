# Двухнаправленный связанный список
# Кажды узел списка содержит данные и два указателя (до и после)

class Node2:  # класс Node2 определяет узел:
    def __init__(self, val):
        self.value = val  # данные
        self.prev = None  # указатель на предыдущий узел
        self.next = None  # указатель на следующий узел


n1 = Node2(12)  # создание узла (объект класса Node2)
n2 = Node2(55)  # создание узла (объект класса Node2)
n1.next = n2  # узлу n1 задать указатель на следующий узел n2 ( 12 -> 55)
n2.prev = n1  # узлу n2 задать указатель на предшествующий узел n1


class LinkedList2:  # класс LinkedList2 определяет методы двухнаправленного связанного списка
    def __init__(self):
        self.head = None  # указатель на голову (первый узел) списка
        self.tail = None  # указатель на хвост (последний узел) списка

    def add_in_tail(self, item):  # метод добавления узла в конец списка
        if self.head is None:  # если список пуст:
            self.head = item  # новый узел станет головным (первым узлом списка)
            item.prev = None  # для нового узла указатель на предыдущий узел содержит None
            item.next = None  # для нового узла указатель на следующий узел содержит None
        else:  # иначе (если список не пуст):
            self.tail.next = item  # последний узел списка будет ссылать на новый узел item
            item.prev = self.tail  # указатель "до" нового узла будет ссылаться на последний узел списка
        self.tail = item  # новый узел станет последним узлом в списке

    def print_first(self):
        node = self.head
        list_print = []
        while node is not None:
            list_print.append(node.value)
            node = node.next
        return list_print

    def print_end(self):
        node = self.tail
        list_print = []
        while node is not None:
            list_print.append(node.value)
            node = node.prev
        return list_print

    # 2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    def find_first(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # 2.2. Добавьте в класс LinkedList2 метод удаления одного узла по его значению
    def del_first(self, val):
        node = self.find_first(val)  # переменная для хранения результата поиска
        if node is not None:  # если поиск дал результат...
            if node == self.head:  # если найден головной узел...
                self.head = node.next  # головным узлом будет следующий
                node.next.prev = None  # указатель на предыдущий узел головного узла содержит None
            elif node == self.tail:  # иначе если найден хвостовой узел...
                self.tail = node.prev  # хвостовым узлом будет предыдущий
                node.prev.next = None  # указатель предыдущего узла на следующий содержит None
            elif node != self.head and node != self.tail:  # иначе если найден средний узел:
                node.prev.next = node.next  # переопределение связей для исключения найденного узла
                node.next.prev = node.prev
        else:  # если поиск не дал результатов верни None
            return

    # 2.3. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    def insert_next(self, node, new_node):  # в качестве параметров метод принимает объекты касса Node2
        if node == self.tail:  # если указанный узел списка соответствует хвостовому узлу...
            self.add_in_tail(new_node)  # добавить новый узел при помощи метода add_in_tail
            return
        else:  # в противном случае добавить новый узел (объект класса Node2) в список после указанного узла
            new_node.next = node.next  # изменить указатели узлов
            node.next.prev = new_node
            node.next = new_node
            new_node.prev = node
            return

    # 2.4. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
    def insert_first(self, val):
        new_node = Node2(val)  # создание нового узла (объект класса Node2)
        node = self.head  # переменная node будет хранить ссылку на голову списка
        if node is not None:  # если список не пустой...
            node.prev = new_node  # указатель "до" головного элемента будет указывать на новый узе
            new_node.next = node  # указатель на следующий узел нового элемента будет ссылатьна на головной узел
            self.head = new_node  # головным узлом будет новый узел
        else:  # если список был пуст...
            self.head = new_node  # головным узлом будет новый узел
            self.tail = new_node

    def get_node(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

# from collections import deque
#
# class Node0:
#     def __init__(self, v):
#         self.value = v
#
# list2 = deque([Node0(16), Node0(32), Node0(64)])
#
# list2.appendleft(Node0(8))
# for itm in list2:
#     print(itm.value)
#
# list2.insert(2, Node0(777))
# for itm in list2:
#     print(itm.value)
