a=int(input())
m=list(map(int,input().split()))
max=0
for i in m:
    l=len(str(i))
    if l>max:
        max=l
c=0
for i in m:
    l=len(str(i))
    if l==max:
        print(i,end=" ")