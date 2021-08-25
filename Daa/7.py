import numpy as np
def min_path(distance,visited,n):
    size = np.inf
    index = 0
    for i in range(0,n):
        if(size>distance[i] and visited[i]==False):
            size = distance[i]
            index = i
    return index
def dijktras(n,graph,s):
    visited = [False]*n
    distance = [np.inf]*n
    distance[s] = 0
    for i in range(n):
        min = min_path(distance,visited,n)
        visited[min] = True
        for j in range(0,n):
            if(graph[min][j]>0 and visited[j]==False and distance[j]>distance[min]+graph[min][j]):
                distance[j] = distance[min]+graph[min][j]
    return distance
n = int(input("Enter no of nodes : "))
print("enter the Adjancency Matrix")
graph = np.zeros([n,n],dtype=int)
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(n):
        graph[i][j] = l[j]
s = int(input("enter the source vertice : "))
print("shortest distance from node ",s)
l = dijktras(n,graph,s)
print("Nodes : Distance")
for i in range(n):
    print("  "+str(i)+"  :    "+str(l[i]))
'''
5
0 2 3 0 0
2 0 15 2 0 
3 15 0 0 13
0 2 0 0 9
0 0 13 9 0
0
'''