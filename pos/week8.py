
mem_size=int(input("enter total memory size "))
page_size=int(input("enter page size "))
p=int(input("enter no.of processes "))
'''
mem_size=1000
page_size=100
p=2
'''
print("no.of pages available - ",int(mem_size/page_size))
pg_tab=[]
for i in range(p):
    print("enter page table for process",i)
    pgs=int(input("enter no.of pages "))
    pg=[]
    print("enter page table")
    for i in range(pgs):
        pg.append(int(input()))
    pg_tab.append(pg)


for i in range(p):
    print(pg_tab[i])
stop=0
while(stop!=1):
    print("enter logical address")
    p_no=int(input("enter process no. "))
    pg_no=int(input("enter page no. "))
    offset=int(input("enter offset "))
    print("physical address is ",pg_tab[p_no][pg_no]*page_size+offset)
    cont=int(input("do you want to continue 1/0 "))
    if(cont==0):
        stop=1
