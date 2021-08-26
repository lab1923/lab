#roundrobin and roundrobin

def turnarroundtime(p,n,bt,wt,tat) :
   for i in range(0,n):
       tat[i] = bt[i] + wt[i]
 
def waitingtime(p, bt, wt, quantum,l,r,rem_bt,t):
    for i in range(l,r):
       rem_bt.append(bt[i])
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
    return t
 
def findavgTime(p, n,bt):
    wt=[]
    tat=[]
    rem_bt=[]
    tq1=int(input("enter time quantum for first queue"))
    tq2=int(input("enter time quantum for second queue"))
    for i in range(0,n):
       tat.append(0)
       wt.append(0)
    total_wt = 0
    total_tat = 0
    for i in range(0,n):
        if(q[i]==2):
           n1=i
           break
    timer=0
    timer=waitingtime(p, bt, wt, tq1,0,n1,rem_bt,timer)
    waitingtime(p, bt, wt, tq2,n1,n,rem_bt,timer)
    turnarroundtime(p, n, bt, wt, tat)

    for i in range(0,n):
       total_wt += wt[i]
       total_tat += tat[i]
    print("Gantt chart processes")
    print(gt)
  
    for i in range(0,n):
       print("p= ",p[i],"bt= ",bt[i],"tat= ",tat[i],"wt= ",wt[i])
 
 
    print("Average waiting time = ", float(total_wt) / float(n))
    print("\nAverage turnaround time = \n", float(total_tat) / float(n))


p=[]
bt=[]
rem_bt=[]
n=int(input("enter no.of processes "))
print("enter burst time process")
for i in range(0,n):
   p.append(int(i+1))
   bt.append(int(input()))
print("enter queue no. 1 or 2")
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
findavgTime(p, n, bt)