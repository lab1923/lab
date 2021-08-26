#FIFO, LRU, Optimal, LFU
'''
n=int(input("enter length of page reference string "))
print("enter page reference string")
ref_str=[int(input()) for i in range(n)]
f=int(input("enter no.of frames "))'''
n=20
ref_str=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
f=3
p=[-1 for i in range(f)]

print("reference string")
print(ref_str)
print("no.of frames - ",f)

def fifo():
    global n,ref_str
    j=0
    pg_fault=0
    for i in range(f):
        p[i]=ref_str[i]
        pg_fault+=1
    for i in range(n):
        if(ref_str[i] in p):
            print("for",ref_str[i],p)
            continue
        else:
            p[j]=ref_str[i]
            pg_fault+=1
            j+=1
            if(j>=f):
                j=0
        print("for",ref_str[i],p)
    print("no.of page faults",pg_fault)

def lru():
    global n,ref_str
    j=0
    pg_fault=0
    for i in range(f):
        p[i]=ref_str[i]
        pg_fault+=1
    for i in range(n):
        if(ref_str[i] in p):
            print("for",ref_str[i],p)
            continue
        else:
            least=[-1 for l in range(f)]
            for m in range(f):
                for k in range(i-1,0,-1):
                    if(ref_str[k]==p[m]):
                        least[m]=k
                        break
            j=least.index(min(least))
            p[j]=ref_str[i]
            pg_fault+=1
            j+=1
            if(j>=f):
                j=0
        print("for",ref_str[i],p)
    print("no.of page faults",pg_fault)


def optimal():
    global n,ref_str
    j=0
    pg_fault=0
    for i in range(f):
        p[i]=ref_str[i]
        pg_fault+=1
    for i in range(n):
        if(ref_str[i] in p):
            print("for",ref_str[i],p)
            continue
        else:
            most=[n+1 for l in range(f)]
            for m in range(f):
                for k in range(i+1,n):
                    if(ref_str[k]==p[m]):
                        most[m]=k
                        break
            j=most.index(max(most))
            p[j]=ref_str[i]
            pg_fault+=1
            j+=1
            if(j>=f):
                j=0
        print("for",ref_str[i],p)
    print("no.of page faults",pg_fault)

stop=0
while(stop!=1):
    print("1.FIFO\t2.LRU\t3.Optimal")
    ch=int(input("enter choice "))
    if ch==1:
        fifo()
    elif ch==2:
        lru()
    elif ch==3:
        optimal()
    cont=int(input("do you want to continue 1/0 "))
    if(cont==0):
        stop=1