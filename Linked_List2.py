# from collections import deque
import collections


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
                return node.value
            node = node.next

    # 2.2. Добавьте в класс LinkedList2 метод удаления одного узла по его значению
    def del_first(self, val):
        if self.head is not None:  # если список не пуст...
            node = self.head  # переменная node будет хранить ссылку на голову списка
            while node is not None:  # цикл по списку
                if node.value == val and node == self.head:  # если значение узла соответствует искомому и узе головной
                    self.head = node.next  # головным узлом становится следующий узел
                    node.next.prev = None  # у следующего узла указатель на предыдущий ссылается на None
                    return
                # иначе если найдено значение в "среднем" узле...
                elif node.value == val and node != self.head and node != self.tail:
                    node.prev.next = node.next  # предыдущий узел будет ссылаться на следующий за найденным
                    # указатель "до" следующего за найденным узла будет ссылаться на предыдущий Оо
                    node.next.prev = node.prev
                    return
                elif node.value == val and node.next is None:  # если поиск вышел на хвостовой узел...
                    self.tail = node.prev  # хвостовым узлом станет предыдущий узел
                    node.prev.next = None  # указатель на следующий узел предыдущего узла будет указывать на None Оо
                    return
                node = node.next  # переход к следующему узлу для новой итерации

    # 2.3. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    def insert_next(self, num, val):
        new_node = Node2(val)  # создание нового узла (объект класса Node2)
        node = self.head  # переменная node будет хранить ссылку на голову списка
        ln = 0  # счетчик узлов
        while node is not None:  # цикл по узлам списка
            if ln == num:  # если номер узла совпадает с заданным...
                if node.next is not None:  # если узел не последний...
                    new_node.next = node.next  # добавление/изменение связей для включений нового узла в списк
                    node.next.prev = new_node
                    new_node.prev = node
                    node.next = new_node
                else:  # если если найденный узел является последним/хвостовым...
                    node.next = new_node  # добавление/изменение связей для включений нового узла в конец списка
                    new_node.next = None
                    new_node.prev = node
                    self.tail = new_node
            ln += 1  # увеличение счетчика узлов списка
            node = node.next  # переход к следующему узлу для новой итерации цика

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
