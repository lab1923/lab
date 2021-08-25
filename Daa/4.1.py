# pivot at low
import random
def partition(arr,start,end):
    pivot = arr[start]
    low = start+1
    high = end
    pivot_index = low+1
    while low < high:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[start], arr[high] = arr[high], arr[start]
    return high

def quick_sort(arr,low,high):
    if low < high :
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
arr = []
n = int(input("Enter the no of values to sort : "))
for _ in range(n):
    x = random.randint(0,100)
    arr.append(x)
print(arr)
quick_sort(arr,0,len(arr)-1)
print(arr)
