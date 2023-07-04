n=int(input())
m=n
sum=0
l=len(str(n))
while n:
    d=n%10
    sum=sum+d**l
    n=n//10
    l=l-1
if(sum==m):
    print("True")
else:
    print("False")