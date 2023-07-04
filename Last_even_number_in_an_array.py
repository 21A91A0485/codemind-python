n=int(input())
l=list(map(int,input().split()))
for i in l:
    l.reverse()
for  j in l:
    if j%2==0:
        print(j)
        break