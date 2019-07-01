# модель построения Графов + метод обхода в глубину + обход вширину


class Stack:
    '''класс стека для метода обхода в глубину'''

    def __init__(self):
        self.stack = []

    def pop(self):
        '''метод вставки в конец стека'''
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def size(self):
        '''метод возврата размера стека'''
        return len(self.stack)


class Queue:
    '''класс очереди для метода обхода в ширину'''

    def __init__(self):
        self.list = []

    def enqueue(self, item):
        '''метод вставки в конец очереди'''
        self.list.append(item)

    def dequeue(self):
        '''метод изъятия из начала очереди'''
        # выдача из головы
        if len(self.list) > 0:
            return self.list.pop(0)
        else:
            return None  # если очередь пустая

    def size(self):
        '''метод возврата размера очереди'''
        if len(self.list) == 0:
            return 0
        else:
            return len(self.list)


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

    def __repr__(self):
        '''Метод упрощенного отображения объектов класса Vertex'''
        return 'V_{}'.format(self.Value)


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = []

    def is_vertex(self, v):
        return v <= self.max_vertex - 1 and self.vertex[v]

    def AddVertex(self, value):
        '''Метод добавления новой вершины с значением Value в свободное место self.vertex'''
        self.vertex.append(Vertex(value))
        if len(self.vertex) > self.max_vertex:
            [i.append(0) for i in self.m_adjacency]
            self.max_vertex += 1
            self.m_adjacency.append([0] * self.max_vertex)

    def RemoveVertex(self, value):
        '''Метод удаления вершины со всеми её ребрами'''
        if self.is_vertex(value):
            [i.pop(value) for i in self.m_adjacency]
            self.m_adjacency.pop(value)
            self.vertex.pop(value)
            self.max_vertex -= 1
            return True
        else:
            return False

    def IsEdge(self, v1, v2):
        '''
        Метод проверки наличия ребра между вершинами v1 и v2
        return True если ребро есть, иначе return False
        '''
        if self.is_vertex(v1) and self.is_vertex(v2):
            return self.m_adjacency[v1][v2] == 1
        else:
            return False

    def AddEdge(self, v1, v2):
        '''Метод добавления ребра между вершинами v1 и v2'''
        if self.is_vertex(v1) and self.is_vertex(v2):
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        else:
            return False

    def RemoveEdge(self, v1, v2):
        '''Метод удаления ребра между вершинами v1 и v2'''
        if self.is_vertex(v1) and self.is_vertex(v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
            return True
        return False

    def available_vertices(self, v):
        for i, value in enumerate(self.m_adjacency[v]):
            if value == 1 and not self.vertex[i].Hit:
                return self.vertex[i]
        return False

    def DepthFirstSearch(self, VFrom, VTo):
        '''
        Метод поиска кратчайшего пути от VFrom до  VTo
        return: список узлов  путь из VFrom в VTo или [] если пути нет
        '''
        stack = Stack()
        for v in self.vertex:
            v.Hit = False

        current = self.vertex[VFrom]
        current.Hit = True
        stack.push(current)
        while True:

            VFrom = self.vertex.index(current)
            if self.m_adjacency[VFrom][VTo] == 1:
                stack.push(self.vertex[VTo])
                break
            else:
                current = self.available_vertices(VFrom)

            if not current:
                stack.pop()
                if stack.size() == 0:
                    return stack.stack
                else:
                    current = stack.stack[0]
                    current.Hit = True
            else:
                current.Hit = True
                stack.push(current)

        return stack.stack[::]

    def get_path_bfs(self, vertex):
        '''Метод обхода'''
        yield vertex
        if vertex.Parent is None:
            return vertex
        yield from self.get_path_bfs(vertex.Parent)

    def BreadthFirstSearch(self, VFrom, VTo):
        '''
        Метод получает в качестве параметров индексы в массиве vertex двух узлов
        и возвращает список узлов, представляющий собой путь из начального узла в конечный,
        либо пустой список, если пути не существует.
        '''
        queue = Queue()
        for v in self.vertex:
            v.Hit = False
            v.Parent = None
        current = self.vertex[VFrom]
        current.Hit = True
        queue.enqueue(current)
        while True:
            index_current = self.vertex.index(current)
            adjacent_vertex = self.available_vertices(index_current)
            if not adjacent_vertex:
                if queue.size():
                    current = queue.dequeue()
                else:
                    break
            else:
                adjacent_vertex.Parent = self.vertex[index_current]
                adjacent_vertex.Hit = True
                queue.enqueue(adjacent_vertex)
        return [i for i in self.get_path_bfs(self.vertex[VTo])][::-1]
    
