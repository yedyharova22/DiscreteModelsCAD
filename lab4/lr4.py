class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def FordFulkerson(self, source, sink):

        parent = [-1] * (self.ROW)

        max_flow = 0

        while self.BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            path = []
            while v != source:
                path.append(str(v))
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            path.append(str(source))
            path.reverse()
            print("Path:", "->".join(path), "Flow:", path_flow)

        return max_flow


def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        matrix = [[int(x) for x in line.split()] for line in lines[1:]]
        return n, matrix


if __name__ == '__main__':
    n, matrix = read_matrix_from_file('matrix1.txt')
    g = Graph(matrix)

    source = 0
    sink = 7

    print("The maximum possible flow from " + str(source) + " to " + str(sink) +
          " is " + str(g.FordFulkerson(source, sink)))


