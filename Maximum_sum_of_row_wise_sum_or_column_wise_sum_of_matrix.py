n,m=map(int,input().split())
mat=[]
for i in range(n):
    b=list(map(int,input().split()))
    mat.append(b)
rsum=[]
for i in range(n):
    rsum.append(sum(mat[i]))
print(max(rsum))    