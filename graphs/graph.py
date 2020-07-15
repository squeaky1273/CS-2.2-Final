from helper import Graph, Vertex

def find_shortest_path(self, start_id, target_id):
    """
    Use Dijkstra's Algorithm to return the total weight of the shortest path
    from a start vertex to a destination.
    """
    location_to_distance = dict()

    for vertex_obj in self.vertex_dict.values():
        location_to_distance[vertex_obj] = float('inf')

    start_location = self.vertex_dict[start_id]
    location_to_distance[start_location] = 0

    while len(location_to_distance) > 0:

        min_distance = min(location_to_distance.values())
        location = None

        for vertex in location_to_distance:
            if location_to_distance[vertex] == min_distance:
                min_vertex = vertex

        weight_of_neighbor = (
            list(min_vertex.neighbors_dict.values())
        )

        if location.id == target_id:
            return location_to_distance[location]

        for neighbor, weight in weight_of_neighbor:
            if neighbor in location_to_distance:
                current_distance = location_to_distance[neighbor]
                new_distance = weight + location_to_distance[location]
                if new_distance < current_distance:
                    location_to_distance[neighbor] = new_distance

        del location_to_distance[location]
        
    return None

def fastest_route(self):
    """
    Use Kruskal's Algorithm to return a list of edges, as tuples of 
    (start_id, dest_id, weight) in the graph's minimum spanning tree.
    """
    # Create a list of all edges in the graph, sort them by weight 
    # from smallest to largest
    locations_list = []

    for vertex in self.get_vertices():
        for neighbor, dist in vertex.get_neighbors_with_weights():
            locations_list.append((vertex.get_id(), neighbor.get_id(), dist))
    locations_list = sorted(locations_list, key=lambda item: item[2])
    
    # Create a dictionary `parent_map` to map vertex -> its "parent". 
    # Initialize it so that each vertex is its own parent.
    parent_map = {x[0]:x[0] for x in locations_list}

    # Create an empty list to hold the solution (i.e. all edges in the 
    # final spanning tree)
    route_list = list()

    # While the spanning tree holds < V-1 edges, get the smallest 
    # edge. If the two vertices connected by the edge are in different sets 
    # (i.e. calling `find()` gets two different roots), then it will not 
    # create a cycle, so add it to the solution set and call `union()` on 
    # the two vertices.
    while len(route_list) <= len(locations_list) - 1:
        current_edge = locations_list.pop(0)
        (vertex_1, vertex_2, dist) = current_edge
        if self.find(parent_map, vertex_1) != self.find(parent_map, vertex_2):
            route_list.append(current_edge)
            self.union(parent_map, vertex_1, vertex_2)
        else:
            continue

    # Return the route list.
    return route_list

def location_to_location(self):
    '''floyd_warshall'''
    """
    Return the All-Pairs-Shortest-Paths dictionary, containing the shortest
    paths from each location on the map to each other locations.
    """
    all_locations = self.get_vertices()
    all_location_vertex_id = [vertex.get_id() for vertex in all_locations]

    vertex_index_map = {}
    for index in range(len(all_location_vertex_id)):
        location_id = all_location_vertex_id[index]
        vertex_index_map[location_id] = index

    distances_graph = [[float("inf") for _ in all_location_vertex_id] for _ in all_location_vertex_id]

    for vertex in all_locations:
        vertex_index = vertex_index_map[vertex.get_id()]
        distances_graph[vertex_index][vertex_index] = 0
        for neighbor, weight in vertex.get_neighbors():
            neighbor_index = vertex_index_map[neighbor.get_id()]
            distances_graph[vertex_index][neighbor_index] = weight

    for k in range(len(all_location_vertex_id)):
        for i in range(len(all_location_vertex_id)):
            for j in range(len(all_location_vertex_id)):
                distances_graph[i][j] = min(distances_graph[i][j], distances_graph[i][k] + distances_graph[k][j])