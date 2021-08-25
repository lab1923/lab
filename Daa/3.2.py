import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1;k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1;k+=1 

n = int(input("Enter no of elements to be sorted : "))
arr = []
for _ in range(n):
    x = random.randint(0,100)
    arr.append(x)
print(arr)
merge_sort(arr)
print(arr)
