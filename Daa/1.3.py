m = int(input())
n = int(input())
p = int(input())
q = int(input())

m1 = [[int(input()) for i in range(n) ] for j in range(m)]
print(m1)
m2 = [[int(input()) for i in range(p) ] for j in range(q)]
print(m2)

for i in range(m):
    for j in range(p):
        val = 0
        for k in range(n):
            val += m1[i][k]*m2[k][j]
        print(val,end = " ")
    print()
