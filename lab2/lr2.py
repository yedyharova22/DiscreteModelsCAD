from collections import defaultdict
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.visited_edges = defaultdict(bool)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def isConnected(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if len(self.graph[i]) != 0:
                break
        if i == self.V - 1:
            return True
        self.DFSUtil(i, visited)
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True

    def isEulerian(self):
        if self.isConnected() == False:
            return 0
        else:
            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0

    def test(self):
        res = self.isEulerian()
        if res == 0:
            print("graph is not Eulerian")
        elif res == 1:
            print("graph has an Euler path")
            self.printEulerPath()
        else:
            print("graph has an Euler cycle")
            self.printEulerCycle()

    def printEulerCycle(self):
        cycle = []
        stack = [0]
        visited_edges = defaultdict(bool)
        while len(stack) > 0:
            v = stack[-1]
            if len(self.graph[v]) > 0:
                u = self.graph[v][0]
                if visited_edges[(v, u)] == False:
                    visited_edges[(v, u)] = True
                    visited_edges[(u, v)] = True
                    stack.append(u)
                    self.graph[v].remove(u)
                    self.graph[u].remove(v)
                else:
                    self.graph[v].remove(u)
                    self.graph[u].remove(v)
            else:
                cycle.append(stack.pop() + 1)
        print(cycle[::-1])

    def printEulerPath(self):
        start_vertex = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                start_vertex = i
                break
        path = []
        stack = [(start_vertex, None)]
        visited_edges = set()
        while len(stack) > 0:
            v, prev = stack[-1]
            if len(self.graph[v]) > 0:
                u = self.graph[v][0]
                edge = tuple(sorted((v, u)))
                if edge not in visited_edges:
                    stack.append((u, edge))
                    self.graph[v].remove(u)
                    self.graph[u].remove(v)
                    visited_edges.add(edge)
            else:
                path.append(stack.pop()[0] + 1)
        print(path[::-1])


def get_edges(matrix):
    edges = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            if matrix[i][j] != 0:
                edges.append((i, j))
    return edges


def load_matrix(fileName):
    return np.loadtxt(fileName, dtype='i', delimiter=' ')


def draw_matrix(matrix):
    G = nx.Graph(matrix)

    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    maxST1 = load_matrix("matrix3.txt")
    # print(maxST1)
    edges = get_edges(maxST1)
    g = Graph(8)
    for edge in edges:
        g.addEdge(edge[0], edge[1])
    g.test()
    draw_matrix(maxST1)

    # maxST2 = load_matrix("matrix1.txt")
    # edges2 = get_edges(maxST2)
    # g2 = Graph(8)
    # for edge in edges2:
    #     g2.addEdge(edge[0], edge[1])
    # g2.test()
    # draw_matrix(maxST2)
