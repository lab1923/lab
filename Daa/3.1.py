import random
import timeit
import matplotlib.pyplot as plt
import math
def merge(a) :
  if(len(a)>1):
    m = int(len(a)/2)
    l = a[:m]
    r = a[m:]
    merge(l)
    merge(r)
    mergesort(a,l,r)
def mergesort(a,l,r):
    i=j=k=0
    while(i<len(l) and j<len(r)):
        global com
        if(l[i]<r[j]):
            a[k] = l[i]
            i += 1
        else :
            a[k] = r[j]
            j += 1
        k += 1
        com += 1
    while(i<len(l)):
        a[k] = l[i]  
        i += 1
        k += 1
    while(j<len(r)):
        a[k] = r[j]
        j += 1
        k += 1
comList = []
print("N Time")
for i in range(1,201):
    a = []
    com = 1
    for j in range(i):
       a.append(random.randint(1,100))
    
    start = timeit.default_timer()
    merge(a)
    end = timeit.default_timer()
    if(i%10==0):
      print(i,(end-start))
    comList.append(com)
n = [*range(1, 201, 1)]
nn=[]
for x in n:
		nn.append(x*math.log(x,2))
plt.plot(comList,n,color='green', linewidth=3,label='Mergesort time')
plt.plot(nn,n,color='red', linewidth=3,label='nlogn')
plt.title('Merge Sort Running ime')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()