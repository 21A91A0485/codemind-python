s=input()
s1=list(s.lower())
l=[]
for i in s:
    f=s.count(i)
    if f==1:
        l.append(i)
if len(l)>0:
    print(l[0])
else:
    print("-1")