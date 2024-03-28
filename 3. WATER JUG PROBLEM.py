from collections import defaultdict

def waterJugSolver(amt1, amt2, aim): 
    visited = defaultdict(lambda: False)

    def dfs(amt1, amt2):
        if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
            print(amt1, amt2)
            return True
        
        if visited[(amt1, amt2)] == False:
            print(amt1, amt2)
            visited[(amt1, amt2)] = True
            
            return (dfs(0, amt2) or
                    dfs(amt1, 0) or
                    dfs(jug1, amt2) or
                    dfs(amt1, jug2) or
                    dfs(amt1 + min(amt2, (jug1-amt1)), amt2 - min(amt2, (jug1-amt1))) or
                    dfs(amt1 - min(amt1, (jug2-amt2)), amt2 + min(amt1, (jug2-amt2))))
        
        else:
            return False
    
    print("Steps:")
    return dfs(amt1, amt2)

# Function to get user input for jug capacities and target amount
def get_user_input():
    jug1 = int(input("Enter the capacity of jug 1: "))
    jug2 = int(input("Enter the capacity of jug 2: "))
    aim = int(input("Enter the target amount of water: "))
    return jug1, jug2, aim

# Main function
if __name__ == "__main__":
    jug1, jug2, aim = get_user_input()
    if waterJugSolver(0, 0, aim):
        print("Solution Found")
    else:
        print("No solution exists.")
o
