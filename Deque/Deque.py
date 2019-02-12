class Deque:
    def __init__(self):
        # инициализация внутреннего хранилища
        self.list = []

    def addFront(self, item):
        # добавление в голову
        # self.list.insert(0, item)
        self.list.reverse()
        self.addTail(item)
        self.list.reverse()

    def addTail(self, item):
        # добавление в хвост
        self.list.append(item)

    def removeFront(self):
        # удаление из головы
        if self.size() != 0:
            return self.list.pop(0)
        else:
            return None  # если очередь пуста

    def removeTail(self):
        # удаление из хвоста
        if self.size() != 0:
            return self.list.pop(-1)
            # return self.list.pop(self.size() - 1)
        else:
            return None  # если очередь пуста

    def size(self):
        if len(self.list) == 0:
            return 0  # размер очереди
        else:
            return len(self.list)
