'''
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def add_edge(graph, u, v):
    graph[u].append(v)
    return [(u, v)]

def dfs(graph, s):
    visited = []
    stack = []
    stack.append(s)
    visited.append(s)
    traversal_order = []
    while len(stack) != 0:
        s = stack.pop()
        traversal_order.append(s)
        for i in graph[s]:
            if i not in visited:
                stack.append(i)
                visited.append(i)
    return traversal_order
graph = defaultdict(list)
picture = []

edges = [("A", "B"),("B","Z"), ("A", "C"), ("C", "D"), ("C", "E"), ("C", "G"),
         ("G", "M"), ("G", "N"), ("M", "P"), ("M", "Q")]

for u, v in edges:
    print(u, v)
    picture += add_edge(graph, u, v)
G = nx.DiGraph()
G.add_edges_from(picture)
fig, ax = plt.subplots()
nx.draw_networkx(G)
plt.show()

print("*******************************************")
print("Your graph in dictionary form is given below:")
print(graph)
print("*******************************************")


start_vertex = "A"
print(f"Depth First Traversal of this graph starting from vertex {start_vertex} is as follows:")
print("*******************************************")
traversal_order = dfs(graph, start_vertex)
print(" -> ".join(traversal_order))
'''


