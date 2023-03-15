import sys

import numpy as np


class Graph():
    def __init__(self, vertices):
        self.n = vertices
        self.graph = [[0 for _column in range(vertices)]
                      for _row in range(vertices)]

    def print_res(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.n):
            print(parent[i] + 1, "-", i + 1, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):

        min = -sys.maxsize

        for v in range(self.n):
            if key[v] >= min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prim(self):
        key = [-sys.maxsize] * self.n
        parent = [None] * self.n

        key[0] = 0
        mstSet = [False] * self.n

        parent[0] = -1

        for cout in range(self.n):

            u = self.minKey(key, mstSet)

            mstSet[u] = True
            for v in range(self.n):

                if self.graph[u][v] > key[v] and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_res(parent)


def load_matrix(fileName):
    return np.loadtxt(fileName, dtype='i', delimiter=' ')


if __name__ == '__main__':
    maxST1 = Graph(8)
    maxST1.graph = load_matrix("matrix1.txt")
    maxST1.prim()

    maxST2 = Graph(8)
    maxST2.graph = load_matrix("matrix2.txt")
    maxST2.prim()