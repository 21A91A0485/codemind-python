n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
for i in a:
    if i in b:
        if i not in s:
            s.append(i)
print(*s)            