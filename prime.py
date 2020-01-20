n=int( input("ener no"))
if n>1:
   for i in range(2,n):
       if (n%i==0) :
        print("not prime")
        break
   else:
        print("prime")
else:
   print("enter no greater than 1")