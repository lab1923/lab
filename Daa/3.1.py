def merge_sort(list1,list2):
    arr = [0]*(len(list1)+len(list2))
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            arr[k] = list1[i]
            i+=1
        else:
            arr[k] = list2[j]
            j+=1
        k+=1
    while i < len(list1):
        arr[k] = list1[i]
        k+=1;i+=1
    while j < len(list2):
        arr[k] = list2[j]
        k+=1;j+=1    
    return arr

list1 = list(map(int,input("Enter the list 1").split()))
list2 = list(map(int,input("Enter the list 2").split()))
print(merge_sort(list1,list2))
