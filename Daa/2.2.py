l = list(map(int,input().split()))
s = int(input())
low = 0
high = len(l)-1
while(low<=high) :
    mid = int((low+high)/2)
    if(l[mid]>s):
        high = mid-1
    elif(l[mid]<s):
        low = mid+1
    else :
        print("element found at index ",mid)
        break
if(low>high):
    print("element not found")