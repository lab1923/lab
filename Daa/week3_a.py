def merge_sort(arr,left,right):
    i = j = k =0
    arr = [0]*(len(left)+len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
           arr[k] = left[i]
           i+=1
           k +=1
        else:
           arr[k] = right[j]
           j+=1
           k +=1
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr
        
arr = []
list1 = list(map(int,input("Enter list1").split()))
list2 = list(map(int,input("Enter list2").split()))

print(merge_sort(arr,list1,list2))