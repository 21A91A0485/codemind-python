s=input()
r=[]
for i in range(0,len(s)):
    r.append(ord(s[i]))
print(chr(max(r)))    