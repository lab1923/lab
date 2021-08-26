p=[]
bt=[]
n=int(input("enter no.of processes "))
print("enter burst time process")
for i in range(0,n):
   p.append(int(i+1))
   bt.append(int(input()))
at=[]
gt=[]
print("enter arrival time process")
for i in range(0,n):
   at.append(int(input()))
for i in range(0,n):
   for j in range(i+1,n):
       if at[i]>at[j]:
           temp = bt[i]
           bt[i] = bt[j]
           bt[j] = temp
 
           temp = p[i]
           p[i] = p[j]
           p[j] = temp
 
           temp = at[i]
           at[i] = at[j]
           at[j] = temp
k=at.index(min(at))
ct=[]
for i in range(0,n):
   ct.append(0)
ct[k]=at[k]+bt[k]
for i in range(0,n):
   if at[i]>ct[i-1]:
       ct[i]=at[i]+bt[i]
   else:
       ct[i]=ct[i-1]+bt[i]
   gt.append(p[i])
tat=[]
wt=[]
for i in range(0,n):
   tat.append(0)
   wt.append(0)
for i in range(0,n):
   tat[i]=ct[i]-at[i]
   wt[i]=tat[i]-bt[i]
avgtat=0
avgwt=0
for i in range(0,n):
   avgwt=avgwt+wt[i]
   avgtat=avgtat+tat[i]
 
avgwt=float(avgwt)/n
avgtat=float(avgtat)/n
print("Gantt chart")
for i in range(0,n):
   print("p",gt[i],end=" ")
print("\n")
for i in range(0,n):
   print("p= ",p[i],"at= ",at[i],"bt= ",bt[i],"ct= ",ct[i],"tat= ",tat[i],"wt= ",wt[i])
 
 
print("Average Waiting time is: "+str(avgwt))
print("Average Turn Around Time is: "+str(avgtat))
