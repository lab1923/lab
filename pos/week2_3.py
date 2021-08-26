#roundrobin and fcfs

def fcfs(p,l,r,bt,t,wt,tat):

    tat[l]=t+bt[l]
    t=t+bt[l]
    gt.append(p[l])
    for i in range(l+1,r):
        tat[i]=tat[i-1]+bt[i]
        t=t+bt[i]
        gt.append(p[i])
    for i in range(l,r):
        wt[i]=tat[i]-bt[i]
    return t


 
def rr(p,l,r, bt,t, wt, tat,rem_bt):
    for i in range(l,r):
       rem_bt[i]=(bt[i])
    quantum=int(input("enter time quantum for round robin"))
    while (1):
        done = 1
        for i in range(l,r):
            if (rem_bt[i] > 0):
                done = 0
                if (rem_bt[i] > quantum):
                   t += quantum
                   rem_bt[i] -= quantum
                else:
                   t = t + rem_bt[i]
                   wt[i] = t - bt[i]
                   rem_bt[i] = 0
                gt.append(p[i])
        if (done == 1):
            break
    for i in range(l,r):
        tat[i] = bt[i] + wt[i]
    return t
    

p=[]
bt=[]
rem_bt=[]
n=int(input("enter no.of processes "))
print("enter burst time process")
for i in range(0,n):
   p.append(int(i+1))
   bt.append(int(input()))
q1=int(input("enter queue no. for round robin "))
q2=int(input("enter queue no. for fcfs "))
print("enter queue no.s for each process")
q=[]
for i in range(0,n):
   q.append(int(input()))
gt=[]
for i in range(0,n):
    for j in range(i+1,n):
        if q[i]>q[j]:
           temp = bt[i]
           bt[i] = bt[j]
           bt[j] = temp
 
           temp = p[i]
           p[i] = p[j]
           p[j] = temp
 
           temp = q[i]
           q[i] = q[j]
           q[j] = temp

wt=[]
tat=[]
rem_bt=[]
for i in range(0,n):
    tat.append(0)
    wt.append(0)
    rem_bt.append(0)
for i in range(0,n):
    if(q[i]==2):
        n1=i
        break

t=0
if(q1<q2):
    t=rr(p,0, n1, bt,t,wt,tat,rem_bt)
    fcfs(p, n1,n, bt,t,wt,tat)
else:
    t=fcfs(p,0, n1, bt,t,wt,tat)
    rr(p,n1, n, bt,t,wt,tat,rem_bt)


print("Gantt chart processes")
print(gt)


total_wt = 0
total_tat = 0

for i in range(0,n):
    total_wt += wt[i]
    total_tat += tat[i]
  
for i in range(0,n):
    print("p= ",p[i],"bt= ",bt[i],"tat= ",tat[i],"wt= ",wt[i],"queue no. = ",q[i])
 
 
print("Average waiting time = ", float(total_wt) / float(n))
print("\nAverage turnaround time = \n", float(total_tat) / float(n))
