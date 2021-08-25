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
        if(l[i]<r[j]):
            a[k] = l[i]
            i += 1
        else :
            a[k] = r[j]
            j += 1
        k += 1
    while(i<len(l)):
        a[k] = l[i]
        i += 1
        k += 1
    while(j<len(r)):
        a[k] = r[j]
        j += 1
        k += 1
print("n","time")
for i in range(100,1100,100):
    a = []
    for j in range(i):
       a.append(random.randint(1,100))
    start = timeit.default_timer()
    merge(a)
    end = timeit.default_timer()
    print(i,end-start)

