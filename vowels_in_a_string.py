s=input()
n=input()
v="AEIOUaeiou"
for i in s:
    if i==n and i in v:
        print("True")
        print(s.index(i))
        break
else:
    print("False")