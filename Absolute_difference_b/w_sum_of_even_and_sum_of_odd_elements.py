n=int(input())
s=list(map(int,input().split()))
es=0
os=0
for i in s:
    if i%2==0:
        es+=i
    else:
        os+=i
if es>os:
    print(es-os)
else:
    print(os-es)