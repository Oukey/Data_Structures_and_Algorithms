class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):  # метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    def delete(self, val, all=False):  # удаления одного или всех узлов по заданному значению
        if self.head is not None:
            node = self.head
            if node.value == val and node.next is None:
                self.clean()
                return
            while node.next is not None:
                if node.next.value == val and node.next.next is not None:
                    node.next = node.next.next
                    if all is False:
                        return
                    else:
                        continue
                elif node.next.value == val and node.next.next is None:
                    self.tail = node
                    node.next = None
                    if all is False:
                        return
                    else:
                        continue
                elif self.head.value == val:
                    self.head = node.next
                    if all is False:
                        return
                    else:
                        continue
                node = node.next

    def clean(self):  # метод очистки всего содержимого
        self.__init__()

    def len(self):  # метод вычисления длины списка
        node = self.head
        ln = 0
        while node is not None:
            ln += 1
            node = node.next
        return ln

    def insert(self, afterNode, newNode):
        # если список пуст и afterNode = None
        if self.head is None and afterNode is None:
            self.head = newNode
            self.tail = newNode
        elif self.head is not None:
            # если afterNode последний элемент списка
            if afterNode == self.tail:
                afterNode.next = newNode
                self.tail = newNode
            else:
                newNode.next = afterNode.next
                afterNode.next = newNode


'''
1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
delete(val, all=False)

где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).

1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()

1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается список найденных узлов). 

find_all(val)
1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()

1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка) 
insert(afterNode, newNode)

Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
'''
