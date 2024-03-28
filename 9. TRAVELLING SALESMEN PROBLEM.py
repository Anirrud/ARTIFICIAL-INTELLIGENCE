import itertools

def calculate_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distance(points[order[i]], points[order[i+1]])
    total_distance += distance(points[order[-1]], points[order[0]])  # Return to the starting point
    return total_distance

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def traveling_salesman(points):
    min_distance = float('inf')
    min_order = None
    all_orders = itertools.permutations(range(len(points)))

    for order in all_orders:
        current_distance = calculate_distance(points, order)
        if current_distance < min_distance:
            min_distance = current_distance
            min_order = order

    return min_order, min_distance

def get_points():
    points = []
    num_points = int(input("Enter the number of points: "))
    for i in range(num_points):
        x, y = map(float, input(f"Enter the coordinates of point {i+1} (x y): ").split())
        points.append((x, y))
    return points

if __name__ == "__main__":
    points = get_points()
    order, min_distance = traveling_salesman(points)
    print("Optimal Order:", order)
    print("Minimum Distance:", min_distance)

