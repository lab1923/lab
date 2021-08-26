p=[]
bt=[]
n=int(input("enter no.of processes "))
print("enter burst time process")
for i in range(0,n):
   p.append(int(i+1))
   bt.append(int(input()))
 
gt=[]
 
for i in range(0,n):
   for j in range(i+1,n):
       if bt[i]>bt[j]:
           temp = bt[i]
           bt[i] = bt[j]
           bt[j] = temp
 
           temp = p[i]
           p[i] = p[j]
           p[j] = temp
 
ct=[]
for i in range(0,n):
   ct.append(0)
ct[0]=bt[0]
gt.append(p[0])
for i in range(1,n):
       ct[i]=ct[i-1]+bt[i]
       gt.append(p[i])
 
tat=[]
wt=[]
for i in range(0,n):
   tat.append(0)
   wt.append(0)
for i in range(0,n):
   tat[i]=ct[i]
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
   print("p= ",p[i],"bt= ",bt[i],"ct= ",ct[i],"tat= ",tat[i],"wt= ",wt[i])
 
 
print("Average Waiting time is: "+str(avgwt))
print("Average Turn Around Time is: "+str(avgtat))
