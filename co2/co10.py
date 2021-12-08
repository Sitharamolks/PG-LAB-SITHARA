def factor(a):
   print("the factor of",a)
   for i in range(1,a+1):
     if a%i==0:
      print(i)
a=int(input("enter a number"))     
factor(a)     
