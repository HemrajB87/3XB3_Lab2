import random

from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()
    
    #create_random_graph: assumes nodes are labeled from 0 to I-1
    def create_random_graph(self, I, J):
        if J < I - 1 or J > I * (I - 1) // 2:
            raise ValueError("Invalid number of edges")

        edges = set()
        while len(edges) < J:
            node1 = random.randint(0, I - 1)
            node2 = random.randint(0, I - 1)
            if node1 != node2:
                edge = tuple(sorted((node1, node2)))
                if edge not in edges:
                    edges.add(edge)
                    self.add_edge(node1, node2)

        return self
    
    #approx1:
    def approx1(self, G):
        graph_copy = G
        C = set()
        while True:
            v = max(graph_copy.adj, key=lambda v: len(graph_copy.adj[v]))
            C.add(v)
            for neighbor in graph_copy.adj[v]:
                graph_copy.adj[neighbor].remove(v)
            del graph_copy.adj[v]
            if not any(graph_copy.adj.values()):
                break

        return C


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


#Use the methods below to determine minimum Vertex Covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


#DFS2

def DFS2(self, node1, node2):
    S = [(node1, [node1])]
    marked = {}
    while S:
        current_node, path = S.pop()
        if current_node == node2:
            return path
        if not marked.get(current_node, False):
            marked[current_node] = True
            for neighbor in self.adj[current_node]:
                new_path = path + [neighbor]
                S.append((neighbor, new_path))
    return []

#BFS2

def BFS2(self, node1, node2):
    Q = deque([(node1, [node1])])
    marked = {node1: True}
    while Q:
        current_node, path = Q.popleft()
        if current_node == node2:
            return path
        for neighbor in self.adj[current_node]:
            if not marked.get(neighbor, False):
                marked[neighbor] = True
                new_path = path + [neighbor]
                Q.append((neighbor, new_path))
    return []

#has_cycle
def has_cycle(self, G):
    visited = set()
    for node in G:
        if node not in visited:
            stack = [node]
            while stack:
                current_node = stack[-1]
                if current_node in visited:
                    return True
                visited.add(current_node)
                stack.pop()
                for neighbor in self.adj[current_node]:
                    stack.append(neighbor)
    return False

def is_connected(self, G):
    visited = set()
    stack = [G[0]]
    while stack:
        current_node = stack[-1]
        if current_node not in visited:
            visited.add(current_node)
            stack.pop()
            for neighbor in self.adj[current_node]:
                stack.append(neighbor)
    return len(visited) == len(G)

