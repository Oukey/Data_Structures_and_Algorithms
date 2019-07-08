import unittest
import SimpleGraph as G


class GraphTest(unittest.TestCase):

    def test_norm_0(self):
        g = G.SimpleGraph(5)
        self.assertEqual(g.max_vertex, 5)
        self.assertEqual(len(g.vertex), 5)
        for i in range(g.max_vertex):
            self.assertIsNone(g.vertex[i])
        for el in g.m_adjacency:
            for em in el:
                self.assertEqual(em, 0)

    def test_norm_1(self):
        g = G.SimpleGraph(5)
        for i in range(g.max_vertex):
            self.assertIsNone(g.vertex[i])
        for el in g.m_adjacency:
            for em in el:
                self.assertEqual(em, 0)
        g.AddVertex(10)
        g.AddVertex(11)
        g.AddVertex(12)
        g.AddVertex(13)
        g.AddVertex(14)
        for i in range(g.max_vertex):
            self.assertIsNotNone(g.vertex[i])
        self.assertEqual(g.vertex[0].Value, 10)
        self.assertEqual(g.vertex[1].Value, 11)
        self.assertEqual(g.vertex[2].Value, 12)
        self.assertEqual(g.vertex[3].Value, 13)
        self.assertEqual(g.vertex[4].Value, 14)
        for el in g.m_adjacency:
            for em in el:
                self.assertEqual(em, 0)
        g.AddEdge(1, 3)
        self.assertEqual(g.m_adjacency[1][3], 1)
        self.assertEqual(g.m_adjacency[3][1], 1)
        g.RemoveEdge(1, 3)
        self.assertEqual(g.m_adjacency[1][3], 0)
        self.assertEqual(g.m_adjacency[3][1], 0)

    def test_norm_2(self):
        g = G.SimpleGraph(5)
        g.AddVertex('A')
        g.AddVertex('B')
        g.AddVertex('C')
        g.AddVertex('D')
        g.AddVertex('E')
        g.AddVertex('F')
        self.assertEqual(g.max_vertex, 5)
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(0, 3)
        g.AddEdge(1, 4)
        g.AddEdge(1, 3)
        g.AddEdge(2, 3)
        g.AddEdge(3, 4)
        g.AddEdge(3, 3)
        self.assertEqual(g.m_adjacency[0], [0, 1, 1, 1, 0])
        self.assertEqual(g.m_adjacency[1], [1, 0, 0, 1, 1])
        self.assertEqual(g.m_adjacency[2], [1, 0, 0, 1, 0])
        self.assertEqual(g.m_adjacency[3], [1, 1, 1, 1, 1])
        self.assertEqual(g.m_adjacency[4], [0, 1, 0, 1, 0])
        g.RemoveVertex(3)
        self.assertEqual(g.m_adjacency[0], [0, 1, 1, 0, 0])
        self.assertEqual(g.m_adjacency[1], [1, 0, 0, 0, 1])
        self.assertEqual(g.m_adjacency[2], [1, 0, 0, 0, 0])
        self.assertEqual(g.m_adjacency[3], [0, 0, 0, 0, 0])
        self.assertEqual(g.m_adjacency[4], [0, 1, 0, 0, 0])

    if __name__ == '__main__':
        unittest.main()
