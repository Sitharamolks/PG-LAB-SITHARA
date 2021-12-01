n=int(input("enter the limit"))
x=0
y=1
s=0
print("fibonancci series:")
for i in range(1,n):
   x=y
   y=s
   s=x+y
   print(s)
