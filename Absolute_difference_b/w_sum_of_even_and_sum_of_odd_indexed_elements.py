n=int(input())
s=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es+=s[i]
    else:
        os+=s[i]
if es>os:
    print(es-os)
else:
    print(os-es)