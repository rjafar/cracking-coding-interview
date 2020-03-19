# Implementation of a graph using an adjacency list

class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
    
    def addEdge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)

    def DFS(self, v, visited):
        visited.append(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFS(neighbor, visited)
        return visited

    def BFS(self, v):
        visited = [v]
        queue = [v]
        while queue:
            vert = queue.pop(0)
            for neighbor in self.graph[vert]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

    # Algorithm to find if a path exists between 2 nodes
    def findRoute(self, start, end):
        if start == end: return True
        result = self.BFS(start)
        if end in result:
            return True
        else: 
            return False

    def printGraph(self):
        return self.graph
