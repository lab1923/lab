import random as r
import timeit
import matplotlib.pyplot as plt
import math
com = 0
def quick_sort(a,l,h):
    if l < h:
        p = partition(a,l,h)
        quick_sort(a,l,p-1)
        quick_sort(a,p+1,h)
def partition(a,l,h):
    # pivot_index=h
    # pivot = a[pivot_index]
    pivot = max(a[l:h+1])
    pivot_index = a.index(pivot)
    a[l],a[pivot_index] = a[pivot_index],a[l]
    pivot_index = l
    
    while l < h:
        global com
        while l < len(a) and a[l] <= pivot:
            com += 1
            l+=1
        while a[h] > pivot:
            com+=1
            h-=1
        
        if l < h:
            
            a[l],a[h]=a[h],a[l]
            com+=1
    a[pivot_index],a[h]=a[h],a[pivot_index]
    return h
a = []
comList = []
print("N Time")
for i in range(1,101):
  a =[]
  com =1
  for j in range(0,i):
    n = r.randint(1,100)
    a.append(n)
  start = timeit.default_timer()
  quick_sort(a,0,len(a)-1)
  end = timeit.default_timer()
  if(i%10==0):
      print(i,(end-start))
  comList.append(com)
  
  
#print(comList)
n = [*range(1, 101, 1)]
nn=[]
for x in n:
		nn.append(x*math.log(x,2))
nn1 = []
for x in n:
    nn1.append(x*x)
plt.plot(comList,n,color='green', linewidth=3,label='Quicksort time')
plt.plot(nn,n,color='red', linewidth=3,label='nlogn')
plt.plot(nn1,n,color='blue', linewidth=3,label='n^2')
plt.title('Quick Sort Running time')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()