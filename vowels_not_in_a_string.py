s=input()
v='aeiou'
a=[]
for i in v:
    if i not in s:
        a.append(i)
if len(a)==0:
    print(0)
else:
    print(*a)
        
