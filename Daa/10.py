import numpy as np
def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    printSolution(dist)
def printSolution(dist):
    print("The shortest distances are : ")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                 print("%7s" % ("∞"),end =" ")
            else:
                print("%7d" % (dist[i][j]),end= " ")
            if j == V-1:
                print("")
V = 4
INF = np.inf
graph = np.array([[0, 3, INF, 7],
         [3, 0, 2, INF],
         [3, INF, 0, 1],
         [2, INF, INF, 0]])
floydWarshall(graph)