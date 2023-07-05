n=int(input())
a=len(str(n))
sqrt=n**2
last=sqrt%pow(10,a)
if(last==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")