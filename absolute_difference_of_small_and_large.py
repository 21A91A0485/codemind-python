s=input()
b=s.split()
for i in b:
    print(ord(max(i))-ord(min(i)),end=" ")