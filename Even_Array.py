n=int(input())
s=list(map(int,input().split()))
c=0
k=len(s)
for i in s:
    if i%2==0:
        c+=1
if k==c:
    print("True")
else:
    print("False")