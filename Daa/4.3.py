#pivot as random

import random

def partition(arr,low,high):
    pivot_index = random.randint(low,high)
    pivot = arr[low]
    arr[high],arr[pivot_index] = arr[pivot_index],arr[high]
    pivot_index = low
    for i in range(low,high):
        if pivot >= arr[i]:
            arr[pivot_index],arr[i] = arr[i],arr[pivot_index]
            pivot_index+=1
    arr[pivot_index],arr[high] = arr[high],arr[pivot_index]
    return pivot_index

def quick_sort(arr,low,high):
    
    if low < high :
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)        

arr = []
n = int(input("Enter no of values :"))
for _ in range(n):
    x = random.randint(0,100)
    arr.append(x)
print(arr)
quick_sort(arr,0,len(arr)-1)
print(arr)
