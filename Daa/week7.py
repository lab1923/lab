import sys
def shortest_path(d,v,n):
    size = sys.maxsize
    for i in range(0,n):
        if v[i] == False and size > d[i]:
            size = d[i]
            ind = i
    return ind

def dijkstras(n,g,s):
    is_visited = [False]*n
    distance = [sys.maxsize]*n
    distance[s] = 0
    path = []
    for j in range(n):
        min_distance = shortest_path(distance,is_visited,n)
        path.append(min_distance)
        is_visited[min_distance] = True
        for i in range(n):
            if g[min_distance][i] > 0 and is_visited[i] == False and distance[i] > distance[min_distance]+graph[min_distance][i]:
                distance[i] = distance[min_distance]+graph[min_distance][i]
    print("path : ",path)
    print("Distance of individual distances :")
    for i in range(n):
        print("Node : ",i,"  Distance : ",distance[i])
        
    
nodes = int(input("Enter no of nodes : "))
graph = []
for i in range(nodes):
    x = list(map(int,input().split(",")))
    graph.append(x)
source_node = int(input("Enter the source node : "))
dijkstras(nodes,graph,source_node)