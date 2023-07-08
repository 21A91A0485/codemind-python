r,c=map(int,input().split())
mat=[]
csum=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
for i in range(c):
    c=0
    for j in range(r):
        c+=mat[j][i]
    csum.append(c)
print(max(csum))    