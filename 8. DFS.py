from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=' ')

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

# Function to take user input for the graph
def create_graph():
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

    return g

# Function to take user input for the starting node for DFS
def dfs_input():
    start_node = int(input("Enter the starting node for DFS: "))
    return start_node

if __name__ == "__main__":
    g = create_graph()
    start_node = dfs_input()

    print("DFS Traversal:")
    g.dfs(start_node)
