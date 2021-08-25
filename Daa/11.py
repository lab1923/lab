import numpy as np
def print_brackets(i,j,brackets,c) :
    global h 
    h = c
    if(i == j) :
        print('M'+str(h),end=" ")
        h += 1
    else :
        print("(",end=" ")
        print_brackets(i,brackets[i][j],brackets,h)
        print_brackets(brackets[i][j]+1, j, brackets, h)
        print(")",end=" ")
    return h
n = int(input("Enter no of Matrices : "))
dim = list()
for i in range(n) :
    print("Enter Matrix "+str(i+1)+" Dimensions : ")
    a,b = map(int,input().split())
    dim.append([a,b])
count = 0
for i in range(n-1):
    if(dim[i][1]==dim[i+1][0]):
        count += 1
if count == n-2 :
    print("Cannot perform Multiplication")
    exit(0)
d = list()
for i in range(n):
    d.append(dim[i][0])
d.append(dim[n-1][1])
c = np.zeros((n+1,n+1),dtype=int)
ki = np.zeros((n+1,n+1),dtype=int)
for i in range(1,n+1):
    for j in range(1,n+1-i):
       min_list = list()
       if j==j+i :
           min_list.append(0)
       for k in range(j,j+i):
           min_list.append(c[j][k]+c[k+1][j+i]+d[j-1]*d[k]*d[j+i])
       c[j][j+i] = min(min_list)
       ki[j][j+i] = min_list.index(min(min_list))+j-1
minimum = c[1][n]
brackets = np.zeros((n,n),dtype=int)
for i in range(1,n+1):
    for j in range(1,n+1):
        brackets[i-1][j-1] = ki[i][j]
a = 1
print("Minimum no of multiplications that are possible : ",minimum)
print("Order of Multiplication : ")
print_brackets(0,n-1,brackets,a)

'''
4
3 2 
2 4 
4 2
2 5
'''
