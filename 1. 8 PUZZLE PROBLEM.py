import heapq


class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.calculate_cost()
        self.total_cost = self.depth

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_cost(self):
        # Manhattan distance heuristic
        cost = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_pos = divmod(self.state[i][j] - 1, 3)
                    cost += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
        return cost + self.depth

    def get_children(self):
        children = []
        zero_pos = None
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    zero_pos = (i, j)
                    break
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_pos = (zero_pos[0] + move[0], zero_pos[1] + move[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_pos[0]][zero_pos[1]], new_state[new_pos[0]][new_pos[1]] = \
                    new_state[new_pos[0]][new_pos[1]], new_state[zero_pos[0]][zero_pos[1]]
                children.append(PuzzleNode(new_state, self, move, self.depth + 1))
        return children

    def is_goal(self, goal_state):
        return self.state == goal_state

    def get_path(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node.total_cost += node.parent.total_cost if node.parent else 0
            node = node.parent
        return path[::-1]


def solve_8_puzzle(initial_state):
    open_list = []
    closed_list = set()
    initial_node = PuzzleNode(initial_state)
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.is_goal([[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
            solution_path = current_node.get_path()
            return list(solution_path), current_node.cost
        closed_list.add(tuple(map(tuple, current_node.state)))
        children = current_node.get_children()
        for child in children:
            if tuple(map(tuple, child.state)) not in closed_list:
                heapq.heappush(open_list, child)

    return None


def print_puzzle(state):
    for row in state:
        print(row)


def get_user_input():
    print("Enter the initial state of the 8-Puzzle (use 0 torepresent the blank space):")
    initial_state = []
    for i in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)
    return initial_state

# Main function
if __name__ == "__main__":
    initial_state = get_user_input()
    print("Initial state:")
    print_puzzle(initial_state)

    solution, total_cost = solve_8_puzzle(initial_state)
    if solution:
        
        print("Solution:")
        for step, state in enumerate(solution):
            print(f"\nStep {step + 1}:")
            print_puzzle(state)
        print(f"\nTotal cost: {total_cost}")
    else:
        print("\nNo solution found.")
