class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):  # метод поиска первого узла по его значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):  # метод поиска всех узлов по значению (возвращает список найденных узлов)
        node = self.head
        list_node = []
        while node is not None:
            if node.value == val:
                list_node.append(node)
            node = node.next
        return list_node

    def delete(self, val, all=False):  # метод удаления узла по значению
        if self.head is not None:  # если список не пустой
            node = self.head
            if node.value == val and node.next is None:  # если список из 1 узла и значение равняется искомому
                self.clean()  # очистить список
                return
            while node is not None:
                # 1. Если найден средний узел
                if node.value == val and node != self.head and node != self.tail:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    if all is False:
                        return
                    else:
                        node = node.next
                        continue
                # 2. Если найден первый узел
                elif node.value == val and node == self.head:
                    node.next.prev = None
                    self.head = node.next
                    if all is False:
                        return
                    else:
                        node = node.next
                        continue
                # 3. Если найден хвостовой узел
                elif node.value == val and node == self.tail:
                    node.prev.next = None
                    self.tail = node.prev
                    if all is False:
                        return
                    else:
                        node = node.next
                        continue

                node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        node = self.head
        ln = 0
        while node is not None:
            ln += 1
            node = node.next
        return ln

    def insert(self, afterNode, newNode):
        if self.head is None and afterNode is None:
            self.head = newNode
            self.tail = newNode
        elif self.head is not None and afterNode is None:
            self.add_in_tail(newNode)
        elif self.head is not None:
            if afterNode == self.tail:
                self.add_in_tail(newNode)
                return
            else:
                newNode.next = afterNode.next
                afterNode.next.prev = newNode
                afterNode.next = newNode
                newNode.prev = afterNode

    def add_in_head(self, newNode):
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def print_first(self):
        node = self.head
        list_print = []
        while node is not None:
            list_print.append(node.value)
            node = node.next
        return list_print
