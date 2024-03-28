def solve_cryptarithmetic(puzzle):
    from itertools import permutations

    # Extract unique letters from the puzzle
    letters = set(char for word in puzzle for char in word if char.isalpha())
    
    # If there are more than 10 unique letters, return an error
    if len(letters) > 10:
        return "Invalid input: More than 10 unique letters."

    # Generate all permutations of digits from 0 to 9
    digit_permutations = permutations(range(10))
    
    # Iterate through each permutation
    for perm in digit_permutations:
        # Create a dictionary to map letters to digits
        mapping = dict(zip(letters, perm))
        
        # Convert the puzzle words to integers based on the mapping
        word1 = int("".join(str(mapping[char]) for char in puzzle[0] if char.isalpha()))
        word2 = int("".join(str(mapping[char]) for char in puzzle[1] if char.isalpha()))
        result = int("".join(str(mapping[char]) for char in puzzle[2] if char.isalpha()))
        
        # Check if the equation holds true
        if word1 + word2 == result:
            return mapping
    
    # If no solution is found, return an error message
    return "No solution found."

# Get input from the user
puzzle = []
for i in range(3):
    word = input(f"Enter word {i+1}: ").upper()  # Convert input to uppercase
    puzzle.append(word)

# Example usage
solution = solve_cryptarithmetic(puzzle)
print("Cryptarithmetic Puzzle:", puzzle)
print("Solution:", solution)
