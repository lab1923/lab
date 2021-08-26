def sequential():
    global mem,b,blocks,n
    f=int(input("enter no.of files to be allocated "))
    for i in range(f):
        s=int(input("enter start block "))
        l=int(input("enter length of the file "))
        for j in range(s,s+l):
            if(mem[j]==1):
                print("file no.",i,"can't be allocated")
                return
            else:
                mem[j]=1
        print("file no.",i,"is allocated")

def indexed():
    global mem,b,blocks,n
    f=int(input("enter no.of files to be allocated "))
    for i in range(f):
        index_block=int(input("enter the index block "))
        if(mem[index_block]==0):
            bl=int(input("enter no.of blocks to be allocated "))
            i=0
            count=0
            string=""
            mem[index_block]=1
            while(count<bl and i<n):
                if(mem[i]!=1):
                    mem[i]=1
                    
                    string+=str(index_block)+"-->"+str(i)+" -- for -- file's-block"+str(count)+"\n"
                    count+=1
                i+=1
            
            if(count!=bl):
                print("entire file couldn't be allocated ")
            else:
                print(string)
        else:
            if(mem[i]==1 for i in range(n)):
                print("no blocks available")
            else:
                print("index block not available, enter another block")
                indexed()


def linked():
    global mem,b,blocks,n
    f=int(input("enter no.of files to be allocated "))
    for k in range(f):
        s=int(input("enter start block for file "))
        bl=int(input("enter length of the file for file "))
        i=s
        count=0
        string=""
        if(mem[i]==0):
            while(count<bl and i<n):
                if(mem[i]!=1):
                    mem[i]=1
                    if(count>0):
                        #print("i",i,"prev",prev)
                        string+="block "+str(prev)+"-->"+str(i)+" -- for -- file's-block"+str(count-1)+"\n"
                        prev=i
                    if(count==bl-1):
                        string+="block "+str(i)+"-->"+"null"+" -- for -- file's-block"+str(count)+"\n"
                    count+=1
                    prev=i

                i+=1
            
            if(count!=bl):
                print("entire file couldn't be allocated ")
            else:
                print(string)
        else:
            print("file can't be allocated")




n=int(input("enter total no.of blocks "))
mem=[0 for i in range(n)]
b=int(input("enter no.of blocks already allocated "))
print("enter the blocks which are already allocated")
blocks=[int(input()) for i in range(b)]
for i in range(n):
    if i in blocks:
        mem[i]=1 
    else:
        mem[i]=0


print("1.Sequential\n2.Indexed\n3.Linked")
ch=int(input("enter your choice "))
if(ch==1):
    sequential()
elif(ch==2):
    indexed()
elif(ch==3):
    linked()
