from graph import Graph
import pytest

#   0 -> 1 <- 2
#   | \  | \  A 
#   v  v v  v |
#   5    4 <- 3

# Adjacency list:
# {0:[1,4,5], 1:[3,4], 2:[1], 3:[2,4], 4:[], 5:[]}

graph = Graph()
graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(0,5)
graph.addEdge(1,3)
graph.addEdge(1,4)
graph.addEdge(3,2)
graph.addEdge(3,4)
graph.addEdge(2,1)
graph.printGraph()

def test_add():
    result = graph.printGraph()
    assert result[0] == [1,4,5]
    assert result[1] == [3,4]
    assert result[2] == [1]
    assert result[3] == [2,4]
    assert result[4] == []
    assert result[5] == []

def test_DFS():
    visited = []
    result = graph.DFS(0, visited)
    assert result == [0,1,3,2,4,5]

def test_DFS2():
    visited = []
    result = graph.DFS(3, visited)
    assert result == [3,2,1,4]

def test_DFS3():
    visited = []
    result = graph.DFS(5, visited)
    assert result == [5]

def test_BFS():
    result = graph.BFS(0)
    assert result == [0,1,4,5,3,2]
    
def test_BFS2():
    result = graph.BFS(1)
    assert result == [1,3,4,2]
    
def test_BFS3():
    result = graph.BFS(5)
    assert result == [5]
    
def test_findRoute():
    assert graph.findRoute(0,2) == True
    assert graph.findRoute(2,5) == False
    assert graph.findRoute(1,4) == True
    assert graph.findRoute(5,0) == False