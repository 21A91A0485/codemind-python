s=input()
s1="AEIOUaeiou"
c=0
s3=[]
s4=[]
for i in s:
    if i in s1:
        s3.append(i)
for i in s3:
    if i not in s4:
        s4.append(i)
print(*s4)        
        