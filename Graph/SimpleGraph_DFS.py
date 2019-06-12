# модель построения Графов + метод обхода в глубину


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() > 0:
            return self.stack[0]
        return None

    def size(self):
        return len(self.stack)

    
class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False  # флаг посещения

    def __repr__(self):
        '''Метод упрощенного отображения объектов класса Vertex'''
        return 'V_{}'.format(self.Value)


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size  # спаисок вершин

    def AddVertex(self, value):
        '''Метод добавления новой вершины с значением Value в свободное место self.vertex'''
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for ind in range(self.max_vertex):
            if self.vertex[ind] is None:
                self.vertex[ind] = Vertex(value)
                break

        # здесь и далее, параметры v -- индекс вершины
        # в списке  vertex

    def RemoveVertex(self, v):
        '''Метод удаления вершины со всеми её ребрами'''
        # ваш код удаления вершины со всеми её рёбрами
        if self.is_vertex(v):
            for i in range(self.max_vertex):  # Удаление ребер
                self.RemoveEdge(i, v)
            self.vertex[v] = None  # удаление вершины

        pass

    def IsEdge(self, v1, v2):
        '''
        Метод проверки наличия ребра между вершинами v1 и v2
        return True если ребро есть, иначе return False
        '''
        # True если есть ребро между вершинами v1 и v2:
        if self.is_vertex(v1) and self.is_vertex(v2):
            return self.m_adjacency[v1][v2] == 1
        else:
            return False

    def AddEdge(self, v1, v2):
        '''Метод добавления ребра между вершинами v1 и v2'''
        # добавление ребра между вершинами v1 и v2
        if self.is_vertex(v1) and self.is_vertex(v2):
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        else:
            return False

    def RemoveEdge(self, v1, v2):
        '''Метод удаления ребра между вершинами v1 и v2'''
        # удаление ребра между вершинами v1 и v2
        if self.is_vertex(v1) and self.is_vertex(v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

    def is_vertex(self, v):
        '''Метод проверки вершины в списке vertex'''
        return v <= self.max_vertex - 1 and self.vertex[v]
    
    def available_vertices(self, v):
        '''
        Метод поиска соседних вершин
        return: список доступных вершин или False
        '''
        for i, val in enumerate(self.m_adjacency[v]):
            if val == 1 and not self.vertex[i].Hit:
                return self.vertex[i]
        return False    

    def DepthFirstSearch(self, VFrom, VTo):
        '''
        Метод поиска кратчайшего пути от VFrom до  VTo
        return: список узлов  путь из VFrom в VTo или [] если пути нет
        '''
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        # Проверка присутствия обоих узлов в куче:
        # if VFrom > len(self.vertex):

        stack = Stack()
        for vert in self.vertex:
            vert.Hit = False
        selected_vertex = self.vertex[VFrom]
        selected_vertex.Hit = True
        stack.push(selected_vertex)
        while True:
            VFrom = self.vertex.index(selected_vertex)
            if self.m_adjacency[VFrom][VTo] == 1:
                stack.push(self.vertex[VTo])
                break
            else:
                selected_vertex = self.available_vertices(VFrom)
            if not selected_vertex:
                stack.pop()
                if stack.size() == 0:
                    return stack.stack
                else:
                    selected_vertex = stack.stack[0]
                    selected_vertex.Hit = True
            else:
                selected_vertex.Hit = True
                stack.push(selected_vertex)
        return stack.stack[::-1]
    
