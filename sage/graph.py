from sage.graphs.graph import Graph
from sage.graphs.dfs import dfs_iterator
from itertools import combinations

# Define the initial state and actions
initial_state = [0, 1, 0, 1, 0, 1, 0, 1, 0]
actions = [[0, 1, 3], [1, 2, 4]]

# Create a graph
G = Graph()

# Add nodes (states) to the graph
G.add_vertex(tuple(initial_state))

# Generate all possible states after applying actions
all_states = set()
for action in actions:
    for k in range(len(initial_state)):
        new_state = initial_state.copy()
        for index in action:
            new_state[(k + index) % len(initial_state)] ^= 1  # Apply the action
        all_states.add(tuple(new_state))

# Add edges to the graph based on state transitions
for state in all_states:
    G.add_vertex(state)
    G.add_edge(initial_state, state)

# Depth-First Search to find a cycle
def dfs_cycle(graph, start, depth):
    for vertex in dfs_iterator(graph, start, max_depth=depth):
        if vertex == start:
            return True, []
        elif vertex != initial_state:
            new_depth = depth - 1
            found, path = dfs_cycle(graph, vertex, new_depth)
            if found:
                path.append(vertex)
                return True, path
    return False, []

# Find a cycle using DFS
found_cycle, cycle_path = dfs_cycle(G, initial_state, depth=len(actions))

# Print the result
if found_cycle:
    print("Cycle found:")
    for state in cycle_path:
        print(state)
else:
    print("No cycle found within the specified depth.")

