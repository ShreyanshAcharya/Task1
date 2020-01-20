#import numpy
#import array

#from array import*
n1=int(input("enter first no"))
n2=int(input("enter second no"))
a=[1]
b=[1]
for el in range(2,n1+1):
    if n1 % el == 0:
     a.append(el)
for e2 in range(2,n2+1):
    if n2 % e2 == 0:
     b.append(e2)
print(set(a)& set(b))


