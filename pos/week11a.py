files=[]
root_dir=input("enter root directory ")
print("1.Create files\n2.Delete file\n3.Display files\n4.Search a file")
stop=0
while(stop!=1):
    ch=int(input("\nenter choice "))
    if ch==1:
        n=int(input("enter no.of files to be created "))
        for i in range(n):
            f=input("enter file name ")
            if(f in files):
                print("filename already exists ")
                continue
            files.append(f)
    elif ch==2:
        files.remove(input("enter the filename to be deleted"))
    elif ch==3:
        #print((len(files)//2)*" "+root_dir+" ")
        for i in range(len(files)):
            print(files[i],end=" ")
    elif ch==4:
        search=input("enter the filename to be searched : ")
        if(search in files):
                print("search file "+search+" found ")
        else:
            print("search element not found ")
    cont=int(input("\ndo you want to continue 1/0 "))
    if(cont==0):
        stop=1

    