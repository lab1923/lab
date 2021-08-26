def firstfit():
    global p,p_size,b,b_size
    p_alloc=[]
    b_free=[]
    for i in range(p):
        p_alloc.append(0)
    for j in range(b):
        b_free.append(1)
    for i in range(p):
        for j in range(b):
            if(b_free[j]==1 and p_size[i]<=b_size[j]):
                b_free[j]=0
                p_alloc[i]=1
                print("process no. ",i,"process size ",p_size[i],"block no. ",j,"block size ",b_size[j])
                break
            else:
                continue
        if(p_alloc[i]!=1):
            print("process ",i," size ",p_size[i]," not allocated")

def bestfit():
    global p,p_size,b,b_size,pr,bl
    p_alloc=[]
    b_free=[]
    for i in range(0,b):
        for j in range(i+1,b):
            if b_size[i]>b_size[j]:
                temp = b_size[i]
                b_size[i] = b_size[j]
                b_size[j] = temp
 
                temp = bl[i]
                bl[i] = bl[j]
                bl[j] = temp
    for i in range(p):
        p_alloc.append(0)
    for j in range(b):
        b_free.append(1)
    for i in range(p):
        for j in range(b):
            if(b_free[j]==1 and p_size[i]<=b_size[j]):
                b_free[j]=0
                p_alloc[i]=1
                print("process no. ",i,"process size ",p_size[i],"block no. ",bl[j],"block size ",b_size[j])
                break
            else:
                continue
        if(p_alloc[i]!=1):
            print("process ",i," size ",p_size[i]," not allocated")


def worstfit():
    global p,p_size,b,b_size,pr,bl
    p_alloc=[]
    b_free=[]
    for i in range(0,b):
        for j in range(i+1,b):
            if b_size[i]<b_size[j]:
                temp = b_size[i]
                b_size[i] = b_size[j]
                b_size[j] = temp
 
                temp = bl[i]
                bl[i] = bl[j]
                bl[j] = temp
    for i in range(p):
        p_alloc.append(0)
    for j in range(b):
        b_free.append(1)
    for i in range(p):
        for j in range(b):
            if(b_free[j]==1 and p_size[i]<=b_size[j]):
                b_free[j]=0
                p_alloc[i]=1
                print("process no. ",i,"process size ",p_size[i],"block no. ",bl[j],"block size ",b_size[j])
                break
            else:
                continue
        if(p_alloc[i]!=1):
            print("process ",i," size ",p_size[i]," not allocated")


p=int(input("enter no.of processes "))
b=int(input("enter no.of blocks "))
pr=[]
bl=[]
p_size=[]
b_size=[]

print("enter size of each process ")
for i in range(p):
    pr.append(i)
    p_size.append(int(input()))

print("enter size of each block ")
for i in range(b):
    bl.append(i)
    b_size.append(int(input()))


print("1.first fit\n2.best fit\n3.worst fit\n4.stop")
ch=int(input("enter choice "))
if ch==1:
    firstfit()
if ch==2:
    bestfit()
if ch==3:
    worstfit()
