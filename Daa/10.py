method 2
import numpy as np
def floyd(graph ,v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
        print("After Step",k+1,"Matrix A: ")
        printsol(graph,v)
        
def printsol(graph,v):
    for i in range(v):
        for j in range(v):
            if(graph[i][j]==INF):
                print(" %7s " %("INF"),end=" ")
            else :
                print(" %7d " %(graph[i][j]),end=" ")
        print()
V = 4
INF = np.inf
graph = [[0, 3, INF, 7],
         [3, 0, 2, INF],
         [3, INF, 0, 1],
         [2, INF, INF, 0]]
floyd(graph,V)
