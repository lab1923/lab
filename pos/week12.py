def fcfs():
    global n,s,l,req_que
    head_seq=[]
    total_head=0
    head_seq=[s]
    for i in range(l):
        if(i==0):
            total_head+=abs(req_que[i]-s)
        else:
            total_head+=abs(req_que[i]-req_que[i-1])

        head_seq.append(req_que[i])
    print("total head position sequence --")
    print(head_seq)
    print("total head movement = ",total_head)

def scan():
    global n,s,l,req_que
    head_seq=[s]
    total_head=0
    dir=int(input("enter 0 for left and 1 for right "))
    req_que+=[s]
    req_que.sort()
    k=req_que.index(s)
    initial=s
    if(dir==0):
        for i in range(k-1,-1,-1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

        head_seq.append(0)
        total_head+=abs(0-initial)
        initial=0

        for i in range(k+1,l+1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

    if(dir==1):
        for i in range(k+1,l+1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

        head_seq.append(n-1)
        total_head+=abs(n-1-initial)
        initial=n-1

        for i in range(k-1,-1,-1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

    print("total head position sequence --")
    print(head_seq)
    print("total head movement = ",total_head)



def c_scan():
    global n,s,l,req_que
    head_seq=[s]
    total_head=0
    dir=int(input("enter 0 for left and 1 for right "))
    req_que+=[s]
    req_que.sort()
    k=req_que.index(s)
    initial=s
    if(dir==0):
        for i in range(k-1,-1,-1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

        head_seq.append(0)
        total_head+=abs(0-initial)
        initial=0

        head_seq.append(n-1)
        total_head+=abs(n-1-initial)
        initial=n-1

        for i in range(l,k,-1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

    if(dir==1):
        for i in range(k+1,l+1):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

        head_seq.append(n-1)
        total_head+=abs(n-1-initial)
        initial=n-1

        head_seq.append(0)
        total_head+=abs(0-initial)
        initial=0

        for i in range(k):
            head_seq.append(req_que[i])
            total_head+=abs(req_que[i]-initial)
            initial=req_que[i]

    print("total head position sequence --")
    print(head_seq)
    print("total head movement = ",total_head)


stop=0

n=int(input("enter total no.of tracks "))
s=int(input("enter starting head position "))
l=int(input("enter request queue length "))
print("enter request queue")
req_que=[]
for i in range(l):
    req_que.append(int(input()))
'''
n=200
s=53
l=8
req_que=[98,183,37,122,14,124,65,67]
'''
while(stop!=1):
    print("1.FCFS\t2.SCAN\t3.C-SCAN")
    ch=int(input("enter choice"))
    if ch==1:
        fcfs()
    elif ch==2:
        scan()
    elif ch==3:
        c_scan()
    cont=int(input("do you want to continue 1/0 "))
    if(cont==0):
        stop=1