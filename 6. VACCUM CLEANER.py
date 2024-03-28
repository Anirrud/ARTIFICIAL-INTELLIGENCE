class VacuumCleaner:
    def __init__(self, environment):
        self.position = 0  # Position of the vacuum cleaner (0: Left, 1: Right)
        self.environment = environment  # Environment with dirty cells (0: Clean, 1: Dirty)

    def sense(self):
        return self.environment[self.position]

    def move(self):
        self.position = (self.position + 1) % len(self.environment)

    def clean(self):
        self.environment[self.position] = 0

    def run(self, steps):
        for _ in range(steps):
            current_state = self.sense()
            if current_state == 1:  # Dirty cell
                self.clean()
                print(f"Cleaned cell {self.position}")
            else:
                print(f"Cell {self.position} is already clean.")
            self.move()


if __name__ == "__main__":
    # Get the initial environment as input from the user
    initial_environment = input("Enter the initial environment (e.g., 1,1,0,0,1): ")
    initial_environment = [int(x) for x in initial_environment.split(',')]

    vacuum_cleaner = VacuumCleaner(initial_environment.copy())
    steps = 5
    print("Initial environment:", vacuum_cleaner.environment)
    vacuum_cleaner.run(steps)
    print("Final environment:", vacuum_cleaner.environment)
