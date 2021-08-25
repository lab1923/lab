import numpy as np
def knapsack(profit,weigths,capacity,n):
    if(n==-1 or capacity == 0):
        return 0
    if(weigths[n]>capacity):
        return knapsack(profit,weigths,capacity,n-1)
    else :
        return max(knapsack(profit,weigths,capacity,n-1),profit[n]+knapsack(profit,weigths,capacity-weigths[n],n-1))
items = int(input("Enter no of items : "))
capacity = int(input("Enter Capacity : "))
pi = list(map(int,input("Enter Profits : ").split()))
w = list(map(float,input("Enter weights : ").split()))
print(knapsack(pi,w,capacity,items-1))


'''
sample input
7
15
10 5 15 7 6 18 3
2 3 5 7 1 4 1

3
50
60 100 120
10 20 30

5
10
40 50 100 95 30
2 3.14 1.98 5 3
'''