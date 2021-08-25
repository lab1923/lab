def knapSack(c, wt, val, n):
    if n == 0 or c == 0:
        return 0
    if (wt[n-1] > c):
        return knapSack(c, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(c-wt[n-1], wt, val, n-1),
            knapSack(c, wt, val, n-1))

val = list(map(int,input("Enter the values : ").split()))
wt = list(map(int,input("Enter the weights : ").split()))
wt.sort()
c = int(input("enter the maximum capacity : "))
n = len(val)
print( knapSack(c, wt, val, n))
