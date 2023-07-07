n=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
flag=0
l=[]
for i in a:
    if i>=n and i<=m:
        flag=1
        l.append(i)
        d=max(l)
if(flag==1):
    print(d)
else:
    print("-1")