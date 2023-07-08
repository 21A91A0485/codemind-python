r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
s=0
for i in range(r):
    if mat[i]==sorted(mat[i]) or mat[i]==sorted(mat[i],reverse=True):
        s+=1
print(s)        
        