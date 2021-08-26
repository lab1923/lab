#producer-consumer problem using semaphores

def wait(s):
    s-=1
    return s

def signal(s):
    s+=1
    return s

def producer():
    global empty,mutex,full,item
    empty=wait(empty)
    mutex=wait(mutex)
    item+=1
    print("producer producing item ",item)
    mutex=signal(mutex)
    full=signal(full)

def consumer():
    global empty,mutex,full,item
    full=wait(full)
    mutex=wait(mutex)
    print("consumer consuming item ",item)
    item-=1
    mutex=signal(mutex)
    empty=signal(empty)
    
n=int(input("enter no.of buffers"))
mutex=1
full=0
empty=n
item=0
print("1.Producer\n2.Consumer\n3.stop")
while(1):
    choice=int(input("enter your choice "))
    if(choice==1):
        if((empty!=0) and (mutex==1)):
            producer()
        else:
            print("buffer is full")
    elif(choice==2):
        if((full!=0) and (mutex==1)):
            consumer()
        else:
            print("buffer is empty")
    else: break