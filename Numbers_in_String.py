s=input()
d=[]
for i in s:
    if i.isdigit():
        d.append(int(i))
print(sum(d))        