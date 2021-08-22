import sys
def floydwarshall(graph,n):
    a=list(map(lambda i: list(map(lambda j:int(j),i)),graph))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j]=min(a[i][j],a[i][k]+a[k][j])
    print("All pair shortest path:")
    for i in a:
        for j in i:
            if j==sys.maxsize:
                print("infinity",end="\t")
            else:
                print(j,end="\t\t")
        print()
n=int(input("Enter the no. of vertices:"))
graph=[]
for i in range(n):
    row=list(map(str,input().split()))
    graph.append(row)
for i in range(len(graph)):
    for j in range (len(graph)):
        if graph[i][j]=="infinity":
            graph[i][j]=sys.maxsize
floydwarshall(graph,n)