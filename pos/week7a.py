
t_m=int(input("enter total memory size "))
proc=int(input("enter no.of processes "))
print("enter each process size")
p_size=[]
for i in range(proc):
    p_size.append(int(input()))
"""
t_m=1000
proc=3
p_size=[400,275,550]
"""
p_alloc=[]
for i in range(proc):
    p_alloc.append(0)
avail=t_m
for i in range(proc):
    if(p_size[i]<=avail):
        p_alloc[i]=1
        print("process no. ",i,"process size ",p_size[i],"is allocated")
        avail=avail-p_size[i]
        
    else:
        print("process ",i," size ",p_size[i]," not allocated")
print("total memory allocated is ",t_m-avail)
print("external fragmentation is",avail)