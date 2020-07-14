from graphs.graph import Graph
# from util.file_reader import read_graph_from_file

# Driver code
if __name__ == '__main__':

    # Create the graph

    graph = Graph()

    # Add some vertices
    graph.add_vertex('A')
    graph.add_vertex('E')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('F')
    graph.add_vertex('G')

    # Add connections
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('D', 'E')
    graph.add_edge('F', 'G')