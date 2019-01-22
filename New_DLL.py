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

    def find(self, val):  # метод поиска певого узла по его значению
        node = self.head
        while node is not None:
            if node.valut == val:
                return node
            node = node.next

    def find_all(self, val):  # метод поиска всех узлов по значению (возвращает список найдённых узлов)
        node = self.head
        list_node = []
        while node is not None:
            if node.value == val:
                list_node.append(node)
            node = node.next
        return list_node

    def delete(self, val, all=False):  # метод удаления узла по значению
        node = self.find(val)
        if node is not None:
            if node == self.head:  # еси найден первый узел
                self.head = node.next
                node.next.prev = None
            elif node != self.head and node != self.tail:  # Если найден средний узел
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node == self.tail:  # если найден последний узел
                self.tail = node.prev
                node.prev.next = None

        while node is not None:
            if node.value == val:

        pass  # здесь будет ваш код

    def clean(self):
        pass  # здесь будет ваш код

    def len(self):
        return 0  # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код

    def add_in_head(self, newNode):
        pass  # здесь будет ваш код
