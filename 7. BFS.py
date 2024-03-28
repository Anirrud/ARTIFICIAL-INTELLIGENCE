from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Function to take user input for the graph
def create_graph():
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        edge = input("Enter edge (u v): ")
        u, v = map(int, edge.split())
        g.add_edge(u, v)

    return g

# Function to take user input for the starting node for BFS
def bfs_input():
    start_node = int(input("Enter the starting node for BFS: "))
    return start_node

if __name__ == "__main__":
    g = create_graph()
    start_node = bfs_input()

    print("BFS Traversal:")
    g.bfs(start_node)

