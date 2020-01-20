str=input()
u=0
l=0
for c in str:
    if c.isupper():
        u+=1
    else:
        l+=1
print("upper case",u)
print("lower case",l)