import math
import random
import matplotlib.pyplot as plt
import time
def mergeSort(arr):
    global com
    if len(arr) > 1:
 
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
 
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                com+=1
            else:
                arr[k] = right[j]
                j += 1
                com+=1
            k += 1
 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
no = int(input("Enter no of values :"))
arr = []
comlist = []
timelist = []
for p in range (200):
    com=1
    for i in range(no):
        x = random.randint(0,100)
        arr.append(x)
    print("Given array is", end="\n")
    print(arr)  
    star_time = time.time()
    mergeSort(arr)
    end_time = time.time() - star_time
    comlist.append(com)
    timelist.append(end_time)
    print("Sorted array is: ", end="\n")
    print(arr)
    
n = [*range(1,201,1)]
nm = []
m = [*range(1,201,1)]
mm = []
print(timelist)
for x in n:
    nm.append(x*math.log(x,2))
plt.plot(comlist,n,color = 'green',linewidth = 3 , label = 'Merge sort time')
plt.plot(nm,n,color = 'red' , linewidth = 3 , label = 'nlogn')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()