files = [[-1]*1 for _ in range(20)]
direc = []
root_dir=input("enter root directory ")
print("1.Create directory\n2.Create files\n3.Delete file\n4.Display files\n5.Search a file")
stop=0
while(stop!=1):
    ch=int(input("\nenter choice "))
    if ch==1:
        dirname=input("enter directory ")
        direc.append(dirname)
    elif ch==2:
        dirname=input("enter the directory in which file is to be created ")
        filename=input("enter filename ")
        d=direc.index(dirname)
        files[d].append(filename)
    elif ch==3:
        dirname=input("enter the directory ")
        filename=input("enter the filename to delete ")
        d=direc.index(dirname)
        if filename in files[d]:
            files[d].remove(dirname)
        else:
            print("no such file found ")
    elif ch==4:
        print(root_dir)
        for i in range(len(direc)):
            print(direc[i],end="--")
            for j in range(len(files[i])):
                if files[i][j]!=-1:
                    print(files[i][j],end=" ")
            print("")
    elif ch==5:
        filename=input("enter the filename to search ")
        dirname=input("enter the directory ")
        r=direc.index(dirname)
        if filename in files[r]:
            print("search file "+filename+" found ")
        else:
            print("not found")
    cont=int(input("\ndo you want to continue 1/0 "))
    if(cont==0):
        stop=1