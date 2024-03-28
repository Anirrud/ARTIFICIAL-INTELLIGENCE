import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate from current node to goal node

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def astar(start_state, goal_state, heuristic, get_successors):
    open_list = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        closed_set.add(current_node.state)

        for successor, cost in get_successors(current_node.state):
            if successor in closed_set:
                continue

            g = current_node.g + cost
            h = heuristic(successor, goal_state)
            new_node = Node(successor, current_node, g, h)

            heapq.heappush(open_list, new_node)

    return None  # No path found

def get_successors(state):
    successors = []
    if isinstance(state, tuple):
        x, y = state
        # Define the possible movements: right, down, left, up
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in movements:
            new_x, new_y = x + dx, y + dy
            if new_x >= 0 and new_y >= 0:  # Ensure the successor is within the grid
                successors.append(((new_x, new_y), 1))  # Assume uniform cost for movement
    return successors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

def manhattan_distance(state, goal_state):
    if isinstance(state, tuple):
        x1, y1 = state
    else:
        x1, y1 = state, 0  # Assume state is a single coordinate
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

# Function to get user input for states
def get_input():
    start_state = tuple(map(float, input("Enter start state (x y): ").split()))
    goal_state = tuple(map(float, input("Enter goal state (x y): ").split()))
    return start_state, goal_state

if __name__ == "__main__":
    start_state, goal_state = get_input()
    path = astar(start_state, goal_state, manhattan_distance, get_successors)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
