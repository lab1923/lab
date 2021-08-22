def Gcd(n1,n2):
    while n2 != 0:
        (n1,n2) = (n2,n1%n2)
    return n1

n1,n2 = map(int,input("Enter n1,n2 :").split())
print(Gcd(n1,n2))