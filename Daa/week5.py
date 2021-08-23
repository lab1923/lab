def maxheap(arr,n,i):
    max = i
    l = 2*i +1
    r = 2*i+2
    if l < n and arr[l] > arr[i]:
        max = l
    if r < n and arr[r] > arr[max]:
        max = r
    if max != i:
        arr[i],arr[max] = arr[max],arr[i]
        maxheap(arr,n,max) 
def maxheapsort(arr):
    n = len(arr)
    for i in range((n//2)-1,-1,-1):
        maxheap(arr,n,i)
    print('max heap = ',arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        maxheap(arr,i,0)
    print('max sorted heap = ',arr)

def minheap(arr,n,i):
    min = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] < arr[min]:
        min = left
    if right < n and arr[right] < arr[min]:
        min = right
    if min != i:
        arr[left],arr[min] = arr[min],arr[left]
        minheap(arr,n,min)
def minheapsort(arr):
    n = len(arr)
    for i in range((n//2) - 1 , -1 , -1 ):
        minheap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        minheap(arr,i,0)
    print("heap sort :",arr)
    
        
arr = list(map(int,input("Enter list to be sorted").split()))
maxheapsort(arr)
minheapsort(arr)

# def maxheapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     if l < n and arr[i] < arr[l]:
#         largest = l
#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         maxheapify(arr, n, largest)
  
  
# def heapSort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         maxheapify(arr, n, i)
  
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         maxheapify(arr, i, 0)
  
  
# arr = list(map(int,input("Enter the list :").split()))
# heapSort(arr)
# print(arr)