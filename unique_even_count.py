n=int(input())
arr=list(map(int,input().split()))
b=set(arr)
c=0
for i in b:
    if i%2==0:
        c+=1
print(c)        