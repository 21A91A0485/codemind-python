n=int(input())
lst=list(map(int,input().split()))
e=0
for i in range(n-2):
    if lst[i]%2==0 and lst[i+2]%2==0:
        e=e+1
print(e)        
