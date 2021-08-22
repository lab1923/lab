n = int(input("Enter no of rows and columns :"))
m1 = []
m2 = []

for i in range(n):
    x =[]
    x = list(map(int,input().split()))
    m1.append(x)

print(m1)
for i in range(n):
    x =[]
    x = list(map(int,input().split()))
    m2.append(x)

print(m2)
for i in range(n):
    for j in range(n):
        val = 0
        for k in range(n):
            val += m1[i][k]*m2[k][j]
        print(val,end = " ")
    print()