def merge(a,b,m,n):
  i = j = k = 0
  c = []
  while(i < m and j < n):
    if(a[i] < b[j]):
      c.append(a[i])
      i+=1
    else:
      c.append(b[j])
      j+=1
  while(i < m):
    c.append(a[i])
    i+=1
  while(j < n):
    c.append(b[j])
    j+=1
  print("The merged sorted List is : ",c)
x = list(map(int,input().split()))
y = list(map(int,input().split()))
merge(x,y,len(x),len(y))
