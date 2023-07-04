n=int(input())
s=list(map(int,input().split()))
count=0
for i in range(n):
    if i%2==0:
        count+=s[i]
print(count)        