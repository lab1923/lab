def linear_search(a,key):
    for i in range(len(a)):
        if a[i] == key:
            return "Element found at "+str(i)
    return "Element not found";

a = list(map(int,input("Enter the array :").split()))
key = int(input("Enter the key element :"))

print(linear_search(a,key))