n=input()
l=list(map(int,input().split()))
b=[]
for i in l:
    b.append(len(str(i)))
print(b.count(max(b)))