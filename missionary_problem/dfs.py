def is_valid(state):
    """Check if the current state is valid (no conflicts)."""
    missionary, leopard, goat, grass = state
    # Leopard can't be left with goat without missionary
    if leopard == goat and leopard != missionary:
        return False
    # Goat can't be left with grass without missionary
    if goat == grass and goat != missionary:
        return False
    return True

def get_next_states(current_state):
    """Generate all possible valid next states from the current state."""
    moves = []
    missionary, leopard, goat, grass = current_state
    other_side = 'right' if missionary == 'left' else 'left'

    # Missionary crosses alone (optional but helps in some cases)
    new_state = (other_side, leopard, goat, grass)
    if is_valid(new_state):
        moves.append((new_state, "Missionary crosses alone"))

    # Missionary takes one item at a time
    for item, idx in [('leopard', 1), ('goat', 2), ('grass', 3)]:
        if current_state[idx] == missionary:  # Item is on the same side as missionary
            new_state = list(current_state)
            new_state[0] = other_side  # Missionary moves
            new_state[idx] = other_side  # Item moves
            new_state = tuple(new_state)
            if is_valid(new_state):
                moves.append((new_state, f"Missionary takes {item} to {other_side}"))
    return moves

def solve_river_crossing_dfs():
    """Solve the puzzle using DFS and return the sequence of moves."""
    initial_state = ('left', 'left', 'left', 'left')
    target_state = ('right', 'right', 'right', 'right')
    visited = set()
    stack = [(initial_state, [])]  # (state, path)

    while stack:
        current_state, path = stack.pop()
        if current_state == target_state:
            return path

        if current_state not in visited:
            visited.add(current_state)
            for next_state, action in reversed(get_next_states(current_state)):  # Reverse to explore in order
                stack.append((next_state, path + [action]))

    return None  # No solution found (though this puzzle has one)

solution = solve_river_crossing_dfs()
if solution:
    for i, step in enumerate(solution, 1):
        print(f"Step {i}: {step}")
else:
    print("No solution found!")

"""OUTPUT"""
# Step 1: Missionary takes goat to right
# Step 2: Missionary crosses alone
# Step 3: Missionary takes leopard to right
# Step 4: Missionary takes goat to left
# Step 5: Missionary takes grass to right
# Step 6: Missionary crosses alone
# Step 7: Missionary takes goat to right