from collections import deque

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
    possible_items = ['leopard', 'goat', 'grass']

    # Determine which side the missionary is on
    other_side = 'right' if missionary == 'left' else 'left'

    # Missionary crosses alone (optional, but speeds up the solution)
    new_state = (other_side, leopard, goat, grass)
    if is_valid(new_state):
        moves.append((new_state, "Missionary crosses alone"))

    # Missionary takes one item at a time
    for item in possible_items:
        if locals()[item] == missionary:  # Item is on the same side as missionary
            new_state = list(current_state)
            new_state[0] = other_side  # Missionary moves
            new_state[{'leopard': 1, 'goat': 2, 'grass': 3}[item]] = other_side  # Item moves
            new_state = tuple(new_state)
            if is_valid(new_state):
                moves.append((new_state, f"Missionary takes {item} to {other_side}"))
    return moves

def solve_river_crossing():
    """Solve the puzzle using BFS and return the sequence of moves."""
    initial_state = ('left', 'left', 'left', 'left')  # All start on the left
    target_state = ('right', 'right', 'right', 'right')

    visited = set()
    queue = deque([(initial_state, [])])  # (state, path)

    while queue:
        current_state, path = queue.popleft()
        if current_state == target_state:
            return path

        if current_state not in visited:
            visited.add(current_state)
            for next_state, action in get_next_states(current_state):
                queue.append((next_state, path + [action]))

    return None  # No solution found (though this puzzle has one)

solution = solve_river_crossing()
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