f1 = open("firstfile.txt","r")
for x in f1:
    print(x)
print("---------------")
f1.seek(0,0)    
ff=f1.readlines()
print("Looping through the file using Readline\n")
print("---------------")
