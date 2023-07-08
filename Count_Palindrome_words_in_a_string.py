def reverse(s):
    s=s[::-1]
    return s
m=input()
c=0
n=m.split()
for i in n:
    if i.upper()==reverse(i).upper():
        c+=1
print(c)        