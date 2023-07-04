n=int(input())
s1=list(map(int,input().split()))
c=0
s=len(s1)
m=0
for i in range(s):
    if s1[i]%2==0:
        if i%2==0:
            c+=1
        m=m+1
if m==c:
    print("True")
else:
    print("False")