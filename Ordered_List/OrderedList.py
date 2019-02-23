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
        node = self.head
        # еси список пуст
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.__ascending is True:
                # по возрастанию
                # вставка в голову
                if self.compare(self.head.value, new_node.value) == 1 or self.compare(self.head.value,
                                                                                      new_node.value) == 0:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                # вставка в хвост
                elif self.compare(self.tail.value, new_node.value) == 1 or self.compare(self.tail.value,
                                                                                        new_node.value) == 0:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                # вставка в середину
                else:
                    while self.compare(node.value, new_node.value) == -1 or self.compare(node.value,
                                                                                         new_node.value) == 0:
                        if self.compare(node.next.value, new_node.value) == 1:
                            new_node.next = node.next
                            new_node.prev = node
                            node.next.prev = new_node
                            node.next = new_node
                        node = node.next
            else:
                # по убыванию
                # вставка в голову
                if self.compare(self.head.value, new_node.value) == -1 or self.compare(self.head.value,
                                                                                       new_node.value) == 0:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                # вставка в хвост
                elif self.compare(self.tail.value, new_node.value) == -1 or self.compare(self.tail.value,
                                                                                         new_node.value) == 0:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                # вставка в середину
                else:
                    while self.compare(node.value, new_node.value) == 1 or self.compare(node.value,
                                                                                        new_node.value) == 0:
                        if self.compare(node.next.value, new_node.value) == -1:
                            new_node.next = node.next
                            new_node.prev = node
                            node.next.prev = new_node
                            node.next = new_node
                        node = node.next
        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        return None  # здесь будет ваш код

    def delete(self, val):
        pass  # здесь будет ваш код

    def clean(self, asc):
        # {
        self.__ascending = asc

    pass  # здесь будет ваш код

    def len(self):
        return 0  # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0
