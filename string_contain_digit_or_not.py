s=input()
w=[]
for i in s:
    if i.isdigit():
        w.append(i)
b=(len(w))
if b==0:
    print("Doesn't contain digit")
else:
    print("Contains %d digit"%b)