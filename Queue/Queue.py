class Queue:
    def __init__(self):
        self.list = []
        # инициализация хранилища данных

    def enqueue(self, item):
        # вставка в хвост
        self.list.append(item)

    def dequeue(self):
        # выдача из головы
        if len(self.list) > 0:
            return self.list.pop()
        else:
            return None  # если очередь пустая

    def size(self):
        # размер очереди
        if len(self.list) == 0:
            return 0
        else:
            return len(self.list)

'''
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
while q.size() > 0:
    print(q.dequeue())
'''

