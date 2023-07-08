a=int(input())
m=list(map(int,input().split()))
min=max(m)
for i in m:
    l=len(str(i))
    if l<min:
        min=l
    c=0
for i in m:
    l=len(str(i))
    if l==min:
        c+=1
print(c)            