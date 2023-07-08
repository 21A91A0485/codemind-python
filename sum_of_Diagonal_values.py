r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
di=[]
for i in range(r):
    for j in range(c):
        if(i==j or i+j==r-1):
            di.append(mat[i][j])
print(sum(di))            