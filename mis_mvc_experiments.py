from graph import Graph, MIS, power_set, is_vertex_cover


# Given MVC is incorrect, there is no get_size() defined in graph
def MVC_new(G):
    nodes = [i for i in range(len(G.adj))]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


# experiment shows complimentary relationship

graph = Graph(6)


graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

# Finding Maximum Independent Set
max_independent_set = MIS(graph)
print("Maximum Independent Set:", max_independent_set)

# Finding the Minimum Vertex Cover
min_vertex_cover = MVC_new(graph)
print("Minimum Vertex Cover:", min_vertex_cover)
