import sys
def floyd(g,n):
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j],g[i][k]+g[k][j])
    
    print(g)
    
inf = sys.maxsize
g = [
    [0,3,inf,7],
    [3,0,2,inf],
    [3,inf,0,1],
    [2,inf,inf,0]
]
floyd(g,4)
                
