class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(self, assignment):
        unassigned = [var for var in self.variables if var not in assignment]
        return unassigned[0]

    def order_domain_values(self, variable, assignment):
        return self.domains[variable]

def get_input():
    num_variables = int(input("Enter the number of variables (regions): "))
    variables = [input(f"Enter variable {i+1}: ") for i in range(num_variables)]

    domains = {}
    for var in variables:
        domain = input(f"Enter domain values for variable {var} (separated by space): ").split()
        domains[var] = domain

    num_constraints = int(input("Enter the number of constraints: "))
    constraints = {}
    for _ in range(num_constraints):
        var1, var2 = input("Enter constraint (variable1 variable2): ").split()
        if var1 not in constraints:
            constraints[var1] = []
        if var2 not in constraints:
            constraints[var2] = []
        constraints[var1].append(var2)
        constraints[var2].append(var1)

    return variables, domains, constraints

if __name__ == "__main__":
    variables, domains, constraints = get_input()
    csp = CSP(variables, domains, constraints)
    assignment = csp.backtrack({})
    if assignment:
        print("Solution found:")
        for var, value in assignment.items():
            print(f"{var}: {value}")
    else:
        print("No solution found.")
