def turnarroundtime(p,n,bt,wt,tat) :
   for i in range(0,n):
       tat[i] = bt[i] + wt[i]
 
def waitingtime(p,n, bt, wt, quantum):
 
   rem_bt=[]
   for i in range(0,n):
       rem_bt.append(bt[i])
   t = 0
   while (1):
 
       done = 1
       for i in range(0,n):
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
 
def findavgTime(p, n,bt,quantum):
   wt=[]
   tat=[]
   for i in range(0,n):
       tat.append(0)
       wt.append(0)
   total_wt = 0
   total_tat = 0
   waitingtime(p, n, bt, wt, quantum)
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
n=int(input("enter no.of processes "))
print("enter burst time process")
for i in range(0,n):
   p.append(int(i+1))
   bt.append(int(input()))
 
quantum=int(input("enter time quantum "))
gt=[]
findavgTime(p, n, bt, quantum)
