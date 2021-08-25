x = int(input())
y = int(input())
def gcd(x,y):
      if x==0 :
          return y
      return gcd(y%x,x)
g = gcd(x,y)
print("gcd is ",g)
