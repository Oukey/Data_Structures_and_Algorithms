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
            return self.list.pop(0)
        else:
            return None  # если очередь пустая

    def size(self):
        # размер очереди
        if len(self.list) == 0:
            return 0
        else:
            return len(self.list)


def rotate(queue, elem):
    if queue.size != 0:
        rep = 0
        while rep < elem:
            queue.enqueue(queue.dequeue())
            # queue.dequeue()
            rep += 1
        return queue
    else:
        return None


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)

print('До')
rotate(q, 5)
print('После')
while q.size() > 0:
    print(q.dequeue())
