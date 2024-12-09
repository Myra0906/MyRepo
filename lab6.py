import random
from collections import deque
import time

VERTICES = 500
MAX_DEGREE = 10

class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * (vertices + 1) for _ in range(vertices + 1)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def bfs(self, start):
        visited = [False] * (self.vertices + 1)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for i in range(1, self.vertices + 1):
                if self.matrix[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, start):
        visited = [False] * (self.vertices + 1)
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        visited[node] = True
        for i in range(1, self.vertices + 1):
            if self.matrix[node][i] == 1 and not visited[i]:
                self._dfs_helper(i, visited)

class GraphAdjList:
    def __init__(self, vertices):
        self.adj_list = [[] for _ in range(vertices + 1)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = [False] * len(self.adj_list)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start):
        visited = [False] * len(self.adj_list)
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        visited[node] = True
        for neighbor in self.adj_list[node]:
            if not visited[neighbor]:
                self._dfs_helper(neighbor, visited)

class GraphArrayList:
    def __init__(self, vertices):
        self.array_list = [[] for _ in range(vertices + 1)]

    def add_edge(self, u, v):
        self.array_list[u].append(v)
        self.array_list[v].append(u)

    def bfs(self, start):
        visited = [False] * len(self.array_list)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in self.array_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start):
        visited = [False] * len(self.array_list)
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        visited[node] = True
        for neighbor in self.array_list[node]:
            if not visited[neighbor]:
                self._dfs_helper(neighbor, visited)

def measure_time(function, description):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f"{description}: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    graph_matrix = GraphMatrix(VERTICES)
    graph_adj_list = GraphAdjList(VERTICES)
    graph_array_list = GraphArrayList(VERTICES)

    for i in range(1, VERTICES + 1):
        for _ in range(MAX_DEGREE):
            neighbor = random.randint(1, VERTICES)
            if i != neighbor:
                graph_matrix.add_edge(i, neighbor)
                graph_adj_list.add_edge(i, neighbor)
                graph_array_list.add_edge(i, neighbor)

    measure_time(lambda: graph_matrix.bfs(1), "BFS with Adjacency Matrix")
    measure_time(lambda: graph_adj_list.bfs(1), "BFS with Adjacency List")
    measure_time(lambda: graph_array_list.bfs(1), "BFS with Array List")

    measure_time(lambda: graph_matrix.dfs(1), "DFS with Adjacency Matrix")
    measure_time(lambda: graph_adj_list.dfs(1), "DFS with Adjacency List")
    measure_time(lambda: graph_array_list.dfs(1), "DFS with Array List")