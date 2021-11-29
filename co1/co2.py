a=int(input("enter start year"))
b=int(input("enter end year"))
if(a<b):
  print("leap year are:",end="")
for i in range(a,b):
    if i%4==0 and i%100!=0:
        print(i,end=" ")
