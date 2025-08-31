import random

# Objective function: a simple quadratic
def objective_function(x):
    return -x**2 + 5

# Hill Climbing algorithm
def hill_climb():
    # Start from a random point
    current_x = random.uniform(-10, 10)
    step_size = 0.01
    max_iterations = 1000

    for _ in range(max_iterations):
        # Check neighbors
        next_x = current_x + step_size
        if objective_function(next_x) > objective_function(current_x):
            current_x = next_x
        else:
            # Try the other direction
            next_x = current_x - step_size
            if objective_function(next_x) > objective_function(current_x):
                current_x = next_x
            else:
                # No better neighbor found
                break

    return current_x, objective_function(current_x)

# Run the algorithm
best_x, best_value = hill_climb()
print("Best x:", best_x)
print("Best value:", best_value)
