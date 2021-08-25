def heapify(a,n,i):
    min = i
    left = 2*i+1
    right = 2*i+2
    if(left<n and a[left]<a[min]):
        min = left
    if(right<n and a[right]<a[min]):
        min = right
    if(min!=i):
        a[i],a[min] = a[min],a[i]
        heapify(a,n,min)
a = list(map(int,input("Enter the elements : ").split()))
n=len(a)
for i in range(n//2,-1,-1):
        heapify(a, n, i)
print("minheap")
print(a)