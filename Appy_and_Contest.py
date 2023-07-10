t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    x=(n//a and n//b)
    a=n//a
    b=n//b
    k1=(a+b-x)
    if k1>=k:
        print('Win')
    else:
        print('Lose')