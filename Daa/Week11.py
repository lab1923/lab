import sys
def inorder(s,i,j,n):
    if s[i][j]!=0:
        print("(",end="")
        inorder(s,i,s[i][j],n)
    if(s[i][j]==0):
        if(i==(n-1) and j==(n-1)):
            print("M"+str(n-1),end=" ")
        else:
            print("M"+str(s[i][j+1]),end=" ")
    if s[i][j]!=0:
        inorder(s,s[i][j]+1,j,n)
        print(")",end="")
def MatrixChainMultiplication(d,n):
    m=[[0 for i in range(n)]for j in range(n)]
    s=[[0 for i in range(n)]for j in range(n)]
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=sys.maxsize
            for k in range(i,j):
                r=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                if r<m[i][j]:
                    s[i][j]=k
                    m[i][j]=r
    print("The minimum cost is:",m[1][n-1])
    print("The order of matrix multiplication is:")
    inorder(s,1,n-1,n)
dimension=list(map(int,input("Enter the dimensions:").split()))
MatrixChainMultiplication(dimension,len(dimension))