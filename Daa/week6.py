objects = list(map(int,input("Enter objects :").split()))
weights = list(map(int,input("Enter weights :").split()))
profits = list(map(int,input("Enter profits :").split()))
capacity = int(input("Enter the capacity of bag :"))
bag = []
pw_ratio = []
profit = weight = 0
wt = [0]*len(objects)
for i in weights:
    index = weights.index(i)
    if i > capacity:
        objects.remove(objects[index])
        weights.remove(weights[index])
        profits.remove(profits[index])
        
for i in range(len(objects)):
    pw_ratio.append(profits[i]/weights[i])

while weight < capacity:
    index = pw_ratio.index(max(pw_ratio))
    wt[index] = 1
    weight += weights[index]
    pw_ratio[index] = -1
    bag.append(objects[index])
if weight > capacity:
    weight -= weights[index]
    rem = capacity - weight
    wt[index] = rem/weights[index]

for i in range(len(objects)):
    profit += profits[i]*wt[i]
print("Items in bag is :",bag)
print("Total profits :",profit)