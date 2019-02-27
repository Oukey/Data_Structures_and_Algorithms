class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        # метод сравнения
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        new_node = Node(value)
        if self.head is None:  # если список пуст
            self.head = new_node
            self.tail = new_node
            return
        else:  # если в списке есть узлы
            if self.__ascending:  # для сортировки по возрастанию
                # если значение нового узла меньше чем значение головного
                if self.compare(new_node.value, self.head.value) != 1:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                # если значение нового узла больше чем значение хвостового
                elif self.compare(new_node.value, self.tail.value) != -1:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                else:  # для средних узлов
                    node = self.tail
                    # пока значение нового узла не меньше очередного (перебор от хвоста к голове)
                    while self.compare(new_node.value, node.value) != 1:
                        node = node.prev
                    new_node.prev = node
                    new_node.next = node.next
                    node.next.prev = new_node
                    node.next = new_node
                    return
            else:  # при сортировке по убыванию
                # если значение нового узла боьше или равно значению головного узла
                if self.compare(new_node.value, self.head.value) != -1:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                    return
                # если значение нового узла меньше или равно значению хвостового узла
                elif self.compare(new_node.value, self.tail.value) != 1:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                    return
                else:  # для средних узлов
                    node = self.head
                    # пока значение нового узла не меньше очередного (перебор от головы к хвосту)
                    while self.compare(new_node.value, node.value) != -1:
                        node = node.next
                    new_node.prev = node
                    new_node.next = node.next
                    node.next.prev = new_node
                    node.next = new_node
                    return

    # def find(self, val):
    #     if self.head is None:
    #         return
    #     else:
    #         if self.__ascending:
    #             node = self.tail
    #             while self.compare(node.value, val) != -1:
    #                 if val == node.value:
    #                     return node
    #                 else:
    #                     if node.prev is not None:
    #                         node = node.prev

    def find(self, val):
        if self.head is None:
            return
        else:
            node = self.head
            if self.__ascending:
                while self.compare(node.value, val) != 1:
                    if val > self.tail.value:
                        return
                    elif val == node.value:
                        return node
                    else:
                        if node.next is not None:
                            node = node.next
            else:
                while self.compare(node.value, val) != -1:
                    if val < self.tail.value:
                        return
                    elif val == node.value:
                        return node
                    else:
                        if node.next is not None:
                            node = node.next

    def delete(self, val):
        if self.head is not None:  # если список не пустой
            if val == self.head.value:  # если значение найдено в головном узле
                if self.head.next is None:  # если список состоит из одного узла
                    self.head = None
                    self.tail = None
                    return
                else:
                    self.head.next.prev = None  # если узел в списке не один
                    self.head = self.head.next
                    return
            elif val == self.tail.value:  # если значение найдено в хвостовом узле
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return
            else:
                if self.__ascending:  # если список сортирован по возрастанию
                    if val > self.tail.value or val < self.head.value:
                        return
                    node = self.tail
                    # перебор от хвоста к голове
                    while self.compare(val, node.value) != 1:
                        node = node.prev
                        if val == node.value:
                            node.prev.next = node.next
                            node.next.prev = node.prev
                            return

                else:  # если список сортирован по убыванию
                    if val < self.tail.value or val > self.head.value:
                        return
                    node = self.head
                    # перебор узлов от головы до хвоста
                    while self.compare(val, node.value) != 1:
                        node = node.next
                        if val == node.value:
                            node.prev.next = node.next
                            node.next.prev = node.prev
                            return

    def clean(self, asc):
        # очистка списка
        self.head = None
        self.tail = None
        # self.__init__()
        self.__ascending = asc

    def len(self):
        if self.head is not None:
            ln = 0
            node = self.head
            while node is not None:
                ln += 1
                node = node.next
            return ln
        else:
            return 0

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.strip() == v2.strip():
            return 0
        elif v1.strip() > v2.strip():
            return 1
        else:
            return -1

        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
