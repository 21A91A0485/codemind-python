x,y = map(int,input().split())
l = (map(str,input().split()))
b=[]
for i in l:
    if int(i)<0:
        i = int(i)*-1
        b.append(len(str(i)))
    else:
        b.append(len(i))
print(b.count(y))