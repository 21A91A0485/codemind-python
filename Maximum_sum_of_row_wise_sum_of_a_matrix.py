r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
rsum=[]
for i in range(r):
    rsum.append(sum(mat[i]))
print(max(rsum))  