def heapify(a,n,i):
    max = i
    left = 2*i+1
    right = 2*i+2
    if(left<n and a[left]>a[max]):
        max = left
    if(right<n and a[right]>a[max]):
        max = right
    if(max!=i):
        a[i],a[max] = a[max],a[i]
        heapify(a,n,max)
a = list(map(int,input("Enter the elements : ").split()))
n=len(a)
for i in range(n//2,-1,-1):
        heapify(a, n, i)
print("maxheap")
print(a)