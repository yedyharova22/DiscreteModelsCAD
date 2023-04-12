import numpy as np


def min_hamiltonian_path(inp):
    num_nodes = len(inp)
    visited = [False] * num_nodes
    visited[0] = True
    curr_path = [0]
    curr_bound = 0

    min_path = [0] * (num_nodes + 1)
    path_weight = float('inf')

    stack = [(curr_path, visited, curr_bound)]

    while stack:
        curr_path, visited, curr_bound = stack.pop()
        curr_node = curr_path[-1]
        if len(curr_path) == num_nodes:
            curr_path_cost = sum(inp[curr_path[i]][curr_path[i + 1]] for i in range(num_nodes - 1))
            curr_path_cost += inp[curr_path[-1]][curr_path[0]]
            if curr_path_cost < path_weight:
                path_weight = curr_path_cost
                min_path = curr_path + [0]
        else:
            for i in range(num_nodes):
                if not visited[i] and inp[curr_node][i] > 0:  # exclude edges with weight 0
                    new_path = curr_path + [i]
                    new_visited = visited.copy()
                    new_visited[i] = True
                    new_bound = curr_bound + inp[curr_node][i]
                    for j in range(num_nodes):
                        if not new_visited[j]:
                            new_bound += min(inp[j])
                    if new_bound < path_weight:
                        stack.append((new_path, new_visited, new_bound))

    return min_path, path_weight


def load_matrix(fileName):
    return np.loadtxt(fileName, dtype='i', delimiter=' ')


if __name__ == '__main__':
    mt = load_matrix("matrix1.txt")

    path, weight = min_hamiltonian_path(mt)
    print("Найменший Гамільтонів контур:", [x + 1 for x in path])
    print("Його довжина:", weight)
