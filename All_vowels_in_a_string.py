s=input()
v='aeiou'
a=[]
b=[]
c=0
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    if i in v:
        b.append(i)
if len(b)==5:
    print("True")
else:
    print("False")