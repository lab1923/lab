
total=[]
max=[]
alloc=[]
need=[]
avail=[]
p=int(input("enter no.of processes "))
r=int(input("enter no.of resources "))

print("enter total no.of instances of each resource ")
for i in range(r):
    total.append(int(input()))

print("enter max. no.of resources of each process ")
for i in range(p):
    a=[]
    print("for process ",i)
    for j in range(r):
        a.append(int(input()))
    max.append(a)

print("enter allocated no.of resources of each process ")
for i in range(p):
    a=[]
    print("for process ",i)
    for j in range(r):
        a.append(int(input()))
    alloc.append(a)

need=[[max[i][j]-alloc[i][j] for j in range(r)] for i in range(p)]
for i in range(p):
    for i in range(r):
        if(need[i][j]<0):
            need[i][j]=0

print("max = ",max)
print("alloc = ",alloc)
print("need = ",need)

for i in range(r):
    sum=0
    for j in range(p):
        sum+=alloc[j][i]
    avail.append(total[i]-sum)

print("avail = ",avail)

finish=[]
for i in range(p):
    finish.append(int(0))
ss=[]
for i in range(p):
    for j in range(p):
        if(finish[j]==0):
            check=0
            for k in range(r):
                if(need[j][k]>avail[k]):
                    check=1
                    break
            if(check==0):
                for k in range(r):
                    avail[k]=avail[k]+alloc[j][k]
                finish[j]=1
                ss.append(j)
sum=0
for i in range(p):
    if(finish[i]==1):
        sum+=1
if(sum==p):
    print("safe sequence --")
    print(ss)
else:
    print("the system is in unsafe condition")