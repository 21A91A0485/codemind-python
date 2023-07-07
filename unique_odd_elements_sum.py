n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
s1=0
for i in s:
    if(i%2!=0):
        s1+=i
print(s1)        