
dict={}
n=int(input("no of elements"))
for i in range(n):
    k=input("enter key")
    v=int(input("enter value"))
    dict.update({k:v})

def sortByKey():
    keydict=sorted(dict.items(), key=lambda t:t[0] )
    print("sorted by key:",keydict)
sortByKey()

def lenOfValues():
    s=sum(dict.values())
    print("sum of value:",s)
lenOfValues()

def reverse():
     b={y:x for x,y in dict.items()}
     print(b)

reverse()