s=input()
m=s.split()
s=[]
for i in m:
    s.append(len(str(i)))
print(min(s))    