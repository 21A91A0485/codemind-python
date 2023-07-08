r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
d=[]
for i in range(1,r-1):
    for j in range(1,c-1):
        d.append(mat[i][j])
print(sum(d))