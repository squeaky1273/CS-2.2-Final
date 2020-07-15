from graphs.graph import Vertex, Graph
import unittest

class TestGraph(unittest.TestCase):
    def make_graph(self):
        graph = Graph(is_directed=False)
        vertex_a = graph.add_vertex('A')
        vertex_b = graph.add_vertex('B')
        vertex_c = graph.add_vertex('C')
        vertex_c = graph.add_vertex('D')
        vertex_c = graph.add_vertex('E')
        vertex_c = graph.add_vertex('F')

        graph.add_edge('A','B', 4)
        graph.add_edge('A','C', 8)
        graph.add_edge('B','C', 11)
        graph.add_edge('B','D', 8)
        graph.add_edge('C','F', 1)
        graph.add_edge('C','E', 4)
        graph.add_edge('D','E', 2)
        graph.add_edge('E','F', 6)

        return graph

    def test_shortest_path(self):
        graph = self.make_graph()

        expected_shortest_path = 9

        self.assertEqual(
            graph.find_shortest_path('A', 'F'), expected_shortest_path)

    def test_fastest_route(self):
        """Create a weighted graph."""
        graph = self.make_graph()

        expected_output = [
            ('A', 'B', 4),
            ('A', 'C', 8),
            ('C', 'E', 4),
            ('C', 'F', 1),
            ('D', 'E', 2),
        ]

        self.assertEqual(sorted(graph.fastest_route()), expected_output)

    # def test_location_to_location(self):
    #     graph = self.make_graph()
    #     expected_output = {
    #         "A": {"A":0, "B":, "C":, "D":, "E":, "F":},
    #         "B": {"A":, "B":0, "C":, "D":, "E":, "F":},
    #         "C": {"A":, "B":, "C":0, "D":, "E":, "F":},
    #         "D": {"A":, "B":, "C":, "D":0, "E":, "F":},
    #         "E": {"A":, "B":, "C":, "D":, "E":0, "F":},
    #         "F": {"A":, "B":, "C":, "D":, "E":, "F":0}
    #     }
    #     self.assertEqual(graph.location_to_location(), expected_output)


if __name__ == '__main__':
    unittest.main()