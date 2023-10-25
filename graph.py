import random
import copy

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

    def number_of_nodes(self):
        return len()
    
 
    


    
#create_random_graph: assumes nodes are labeled from 0 to i-1
def create_random_graph(i, j):
    if j > (i * (i - 1)) / 2:
        raise ValueError("Too many edges for the given number of nodes.")
    graph = Graph(i)
    while j > 0:
        node1 = random.randint(0, i - 1)
        node2 = random.randint(0, i - 1)
        if node1 != node2 and not graph.are_connected(node1, node2):
            graph.add_edge(node1, node2)
            j -= 1
    return graph

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


# Part 2 MIS(G)
def is_independent_set(G, potential_set):
    for i in range(len(potential_set)):
        for j in range(i + 1, len(potential_set)):
            if G.are_connected(potential_set[i], potential_set[j]):
                return False
    return True

def MIS(G):
    nodes = [i for i in range(len(G.adj))]

    max_independent_set = []
    for size in range(len(nodes), -1, -1):
        subsets = [subset for subset in power_set(nodes) if len(subset) == size]
        for subset in subsets:
            if is_independent_set(G, subset):
                max_independent_set = subset
                break

    return max_independent_set




# BFS3
def BFS3(G, start_node):
    Q = deque([start_node])
    marked = {start_node: None}  # Predecessor dictionary, initialized with None for the start node
    while Q:
        current_node = Q.popleft()
        for neighbor in G.adj[current_node]:
            if neighbor not in marked:
                marked[neighbor] = current_node
                Q.append(neighbor)
    return marked

# DFS3
def DFS3(G, start_node):
    S = [start_node]
    marked = {start_node: None}  # Predecessor dictionary, initialized with None for the start node
    while S:
        current_node = S.pop()
        for neighbor in G.adj[current_node]:
            if neighbor not in marked:
                marked[neighbor] = current_node
                S.append(neighbor)
    return marked


#has_cycle
""" def has_cycle(G):
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
    return False """

""" def is_connected(G):
    visited = set()
    stack = [G[0]]
    while stack:
        current_node = stack[-1]
        if current_node not in visited:
            visited.add(current_node)
            stack.pop()
            for neighbor in self.adj[current_node]:
                stack.append(neighbor)
    return len(visited) == len(G) """

def has_cycle(G):
    visited = [False] * len(G.adj)
    
    for node in G.adj:
        if not visited[node]:
            if _has_cycle_helper(G, node, visited, -1):
                return True
                
    return False

def _has_cycle_helper(G, node, visited, parent):
    visited[node] = True

    for neighbor in G.adj[node]:
        if not visited[neighbor]:
            if _has_cycle_helper(G, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True

    return False

def is_connected(G):
    """
    Function to check if the graph is connected.
    """
    visited = [False] * len(G.adj)

    # Start DFS from the first node
    dfs(G, list(G.adj.keys())[0], visited)

    # If all nodes are visited then the graph is connected
    return all(visited)
#created my own to use for has_cycle, I think there may be an issue with BFS2 I couldn't get it to work
def dfs(G, node, visited):
    """
    Recursive function to perform DFS.
    """
    visited[node] = True

    for neighbor in G.adj[node]:
        if not visited[neighbor]:
            dfs(G, neighbor, visited)

#approx1:
def approx1(G):
    G_copy = copy.deepcopy(G)
#start with empty set C
    C = []
    while True:

        #Find the vertex with the highest degree in G, call this vertex v
        v = max(G_copy.adj, key=lambda x: len(G_copy.adj[x]), default=None)
        if v is None or len(G_copy.adj[v]) == 0:
            break

        #Add v to C
        C.append(v)

        #Remove all edges incedent to node v from G
        for w in G_copy.adjacent_nodes(v):
            G_copy.adj[w].remove(v)
        G_copy.adj[v] = []    

        #If C is a Vertex Cover return C, else go to step 2
        if is_vertex_cover(G_copy, C):
            return C
    return C

#approx2: 
def approx2(G):
    G_copy = copy.deepcopy(G)
    #Start with an empty set C = {}
    C = set()
    while True:
        #Select a vertex randomly from G which is not already in C, call this vertex v
        available_vertices = [v for v in G_copy.adj if v not in C]
        if not available_vertices:
            #ensures empty graphs will not pass
            return None
        v = random.choice(available_vertices)

        #Add v to C
        C.add(v)

        #If C is a Vertex Cover return C, else go to Step 2
        if is_vertex_cover(G_copy, C):
            return C
        
#approx3
def approx3(G):
    G_copy = copy.deepcopy(G)

    #Start with an empty set C = {}
    C = []
    while G_copy.adj:

        #Select an edge randomly from G, call this edge (u,v)
        u = random.choice(list(G_copy.adj.keys()))
        if not G_copy.adj[u]:
            del G_copy.adj[u]
            continue
        v = random.choice(G_copy.adj[u])

        #Add u and v to C
        C.append(u)
        C.append(v)

        #Remove all edges incident to u or v from G
        for n in G_copy.adj[u][:]:
            G_copy.adj[n].remove(u)
            if not G_copy.adj[n]:
                del G_copy.adj[n]
        del G_copy.adj[u]

        #If C is a Vertex Cover return C, else go to Step 2
    if is_vertex_cover(G, C):
        return C
    else:
        return []
