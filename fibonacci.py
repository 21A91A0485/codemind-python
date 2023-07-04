n=int(input())
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
    s=a+b
    a=b
    b=s
    print(s,end=" ")