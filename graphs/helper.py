class Vertex(object):
    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        """
        self.id = vertex_id
        self.neighbors_dict = {} # id -> (obj, weight)

    def add_neighbor(self, vertex_obj, weight):
        """
        Add a neighbor by storing it in the neighbors dictionary.
        """
        if vertex_obj.get_id() in self.neighbors_dict.keys():
            return # it's already a neighbor

        self.neighbors_dict[vertex_obj.get_id()] = (vertex_obj, weight)

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return [neighbor for (neighbor, weight) in self.neighbors_dict.values()]

    def get_neighbors_with_weights(self):
        """Return the neighbors of this vertex."""
        return list(self.neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = [neighbor.get_id() for neighbor in self.get_neighbors()]
        return f'{self.id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = [neighbor.get_id() for neighbor in self.get_neighbors()]
        return f'{self.id} adjacent to {neighbor_ids}'

class Graph:
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.
        """
        self.vertex_dict = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        """
        if vertex_id in self.vertex_dict.keys():
            return False # it's already there
        vertex_obj = Vertex(vertex_id)
        self.vertex_dict[vertex_id] = vertex_obj
        return True

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.vertex_dict.keys():
            return None
        vertex_obj = self.vertex_dict[vertex_id]
        return vertex_obj
    
    def add_edge(self, vertex_id1, vertex_id2, weight):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.
        """
        all_ids = self.vertex_dict.keys()
        if vertex_id1 not in all_ids or vertex_id2 not in all_ids:
            return False
        vertex_obj1 = self.get_vertex(vertex_id1)
        vertex_obj2 = self.get_vertex(vertex_id2)
        vertex_obj1.add_neighbor(vertex_obj2, weight)
        if not self.is_directed:
            vertex_obj2.add_neighbor(vertex_obj1, weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return list(self.vertex_dict.values())
        
    def union(self, parent_map, vertex_id1, vertex_id2):
        """Combine vertex_id1 and vertex_id2 into the same group."""
        vertex1_root = self.find(parent_map, vertex_id1)
        vertex2_root = self.find(parent_map, vertex_id2)
        parent_map[vertex1_root] = vertex2_root

    def find(self, parent_map, vertex_id):
        """Get the root (or, group label) for vertex_id."""
        if(parent_map[vertex_id] == vertex_id):
            return vertex_id
        return self.find(parent_map, parent_map[vertex_id])