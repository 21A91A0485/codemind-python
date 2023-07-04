n=int(input())
s=list(map(int,input().split()))
count=0
for i in s:
    count+=i
res="{:.2f}".format(count/n)
print(res)