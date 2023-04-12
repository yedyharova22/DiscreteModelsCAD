import itertools

import numpy as np


def are_graphs_isomorphic(adj_mat1, adj_mat2):
    if adj_mat1.shape != adj_mat2.shape:
        return False

    if np.sum(adj_mat1) != np.sum(adj_mat2):
        return False

    n = adj_mat1.shape[0]
    perms = np.array(list(itertools.permutations(range(n))))

    for perm in perms:
        perm_mat = adj_mat1[np.ix_(perm, perm)]
        if np.array_equal(perm_mat, adj_mat2):
            return True

    return False


def load_matrix(fileName):
    return np.loadtxt(fileName, dtype='i', delimiter=' ')


if __name__ == '__main__':
    mt1 = load_matrix("matrix1.txt")
    mt2 = load_matrix("matrix2.txt")

    print("Графи ізоморфні" if are_graphs_isomorphic(mt1, mt2) else "Ізоморфізм не встанослено")