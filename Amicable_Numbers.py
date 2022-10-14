n=int(input())
m=int(input())
s=0
ss=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
for j in range(1,m):
    if(m%j==0):
        ss=ss+j
if(n==ss and m==s):
    print('Amicable')
else:
    print('Not Amicable')
    