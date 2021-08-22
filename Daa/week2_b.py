def binary_search(a,key):
    low= 0;high = len(a)-1;
    while low<=high:
        mid = (low+high)//2;
        if key == a[mid]:
            return "element found at "+str(mid)
        elif key > a[mid]:
            low = mid+1
        elif key < a[mid]:
            high = mid-1
    return "element not found";
    
a = list(map(int,input("Enter the array :").split()))
key = int(input("Enter the key element :"))

print(binary_search(a,key))