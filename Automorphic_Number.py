n=int(input())
num=len(str(n))
sq=n**2
last=sq%pow(10,num)
if(last==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')