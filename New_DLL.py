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
        if self.head is not None:  # если список не пустой
            node = self.head
            if node.value == val and node.next is None:  # если список из 1 кзла и значение равняется искомому
                self.clean()  # очистить список
                return
            while node is not None:
                # 1. Если найден первыый узел
                if node.value == val and node == self.head:

                    pass
                # 2. Если найден средний узел
                elif node.value == val and node == self.tail:
                    pass
                # 3. Если найден хвостовой узел
                elif node.value == val and self.head != node != self.tail:
                    pass

        # if all == False:
        #     node = self.find(val)
        # else:
        #     node = self.find_all()
        #     while node.next is not None:
        #         if node is not None:
        #             if node == self.head:  # еси найден первый узел
        #                 self.head = node.next
        #                 node.next.prev = None
        #             elif node != self.head and node != self.tail:  # Если найден средний узел
        #                 node.prev.next = node.next
        #                 node.next.prev = node.prev
        #             elif node == self.tail:  # если найден последний узел
        #                 self.tail = node.prev
        #                 node.prev.next = None
        #
        # # while node is not None:
        # #     if node.value == val:
        #
        # pass  # здесь будет ваш код

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
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            elif self.head is not None:
                if afterNode == self.tail:
                    self.add_in_tail(newNode)
                    return
                else:
                    newNode.next = afterNode.next
                    afterNode.next.prev = newNode
                    afterNode.next = newNode
                    newNode.prev = afterNode
                    return
                    # if afterNode == self.head:
                #     afterNode.next = newNode
                #     newNode.prev = afterNode
                #     self.tail = newNode
                # else:
                #     newNode.next = afterNode.next
                #     afterNode.next.prev = newNode
                #     afterNode.next = newNode

        def add_in_head(self, newNode):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    '''
     2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    insert(afterNode, newNode)
    Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
    Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    '''

