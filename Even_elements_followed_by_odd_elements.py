n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2 == 0:
        e.append(i)
    if i%2!=0:
        o.append(i)
print(*e,*o)        
    
        
    
    