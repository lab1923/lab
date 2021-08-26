
t_m=int(input("enter total memory size "))
part=int(input("enter no.of partitions "))
print("enter each block size")
b_size=[]
for i in range(part):
    b_size.append(int(input()))

proc=int(input("enter no.of processes "))
print("enter each process size ")
p_size=[]
for i in range(proc):
    p_size.append(int(input()))
"""
t_m=1000
part=4
b_size=[300,300,300,100]
proc=5
p_size=[275,400,290,293,100]
"""
int_frag=[]
ext_frag=0

p_alloc=[]
b_free=[]
for i in range(proc):
    p_alloc.append(0)
for j in range(part):
    b_free.append(1)
for i in range(proc):
    for j in range(part):
        if(b_free[j]==1 and p_size[i]<=b_size[j]):
            b_free[j]=0
            p_alloc[i]=1
            print("internal fragmentation for block",j,"is",b_size[j]-p_size[i])
            ext_frag+=p_size[i]
            print("process no. ",i,"process size ",p_size[i],"block no. ",j,"block size ",b_size[j])
            break
        else:
            continue
    if(p_alloc[i]!=1):
        print("process ",i," size ",p_size[i]," not allocated")

print("external fragmentation is",t_m-ext_frag)