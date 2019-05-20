# модель построения Графов


class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        '''Метод добавления новой вершины с значением Value'''
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        pass

        # здесь и далее, параметры v -- индекс вершины
        # в списке  vertex

    def RemoveVertex(self, v):
        '''Метод удаления вершины со всеми её ребрами'''
        # ваш код удаления вершины со всеми её рёбрами
        pass

    def IsEdge(self, v1, v2):
        '''
        Метод проверки наличия ребра между вершинами v1 и v2
        return True если ребро есть, иначе return False
        '''
        # True если есть ребро между вершинами v1 и v2
        return False

    def AddEdge(self, v1, v2):
        '''Метод добавления ребра между вершинами v1 и v2'''
        # добавление ребра между вершинами v1 и v2
        pass

    def RemoveEdge(self, v1, v2):
        '''Метод удаления ребра между вершинами v1 и v2'''
        # удаление ребра между вершинами v1 и v2
        pass
