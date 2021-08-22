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
        print(m1[i][j]+m2[i][j] , end = " ")
    print()