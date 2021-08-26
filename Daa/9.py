def knapsnack(objects,weights,profits,capacity):
    n = len(objects)
    v = [[0 for i in range(capacity+1)] for j in range(len(objects)+1)]
    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0 or w == 0:
                v[i][w] = 0
            if weights[i-1] <= w:
                v[i][w] = max(v[i-1][w],v[i-1][w-weights[i-1]]+profits[i-1])
            else:
                v[i][w] = v[i-1][w]
    print("The maximum profit is :",v[i][w])
    p = v[i][w]
    bag = []
    for j in range(i-1,-1,-1):
        if p in v[j]: 
            continue
        else:
            bag.append(j+1)
            p -= profits[j]
    print("The objects in the bag are : ",bag)

objects = list(map(int,input("Enter the objects : ").split()))
weights = list(map(int,input("Enter the weights : ").split()))
profits = list(map(int,input("Enter the profits : ").split()))
capacity = int(input("Enter the maximum capacity : ")) 
knapsnack(objects,weights,profits,capacity)


#method 2
# import numpy as np
# items = int(input("Enter no of items : "))
# capacity = int(input("Enter Capacity : "))
# pi =[0]+ list(map(int,input("Enter Profits : ").split()))
# w = [0]+list(map(int,input("Enter weights : ").split()))
# item = list(i for i in range(items+1))
# p = np.zeros([items+1, capacity+1],dtype=int)
# for i in range(1,items+1):
#     for j in range(1,capacity+1):
#         a = p[i-1,j]
#         if(j<w[i]):
#             b = -1
#         else:
#             b = p[i-1,j-w[i]]+pi[i]
#         p[i,j] = int(max(a,b))
# m = p[items,capacity]
# print(p) 
# print("maximum profit that can be obtained is ",p[items,capacity])
