l = list(map(int,input().split()))
s = int(input())
for i in range(len(l)):
    if l[i]==s:
        print("search element found at the index ",i)
        break
else:
 if i+1==len(l):
    print("search element not found")
