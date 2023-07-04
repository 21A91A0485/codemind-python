n=int(input())
a=list(map(int,input().split()))
d=sum(a)//n
if d in a:
    print("True")
else:
    print("False")
    
    