import sys
def shortest_path(d,v,n):
    min_key = sys.maxsize
    index = 0
    for i in range(0,n):
        if d[i] < min_key and v[i] == False:
            min_key = d[i]
            index = i
    return index
    
def prims(n,g):
    mst_set = [False]*n
    key = [sys.maxsize]*n
    key[0] = 0
    path = [None]*n
    path[0] = -1
    for j in range(n):
        min_key = shortest_path(key,mst_set,n)
        mst_set[min_key] = True
        for i in range(n):
            if g[min_key][i] > 0 and mst_set[i] ==False and key[i] > g[min_key][i]:
                key[i] = g[min_key][i]
                path[i] = min_key
    for i in range(1,n):
        print(path[i]," - ",i," = ",g[i][path[i]])

nodes = int(input("Enter no of nodes : "))
graph = []
for _ in range(nodes):
    x = list(map(int,input().split(",")))
    graph.append(x)
prims(nodes,graph)