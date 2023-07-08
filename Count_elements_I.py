n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
s1=[]
for i in a:
    if i in b:
        s.append(i)
for j in a:
    if j in b:
        s1.append(j)
s3=s+s1
s4=set(s3)
print(len(s4))    