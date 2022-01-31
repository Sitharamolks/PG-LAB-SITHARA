f1=open("firstfile.txt","w")
f1.write("This is my first file in python.\nWant to work with files\nThis is my third line")
f1.close()

f1=open("firstfile.txt","r")
print("Name of file:",f1.name)
print("Close of file:",f1.close)
print("Mode of file:",f1.mode)

print(f1.read())
print("------------------")

f1.seek(0,0)
print(f1.read(15))

print(f1.readline())
print(f1.readline())

f1.seek(0,0)
ff=f1.readlines()
print(ff)

print("No of lines : ",len(ff))
print("------------------")

#import os
#os.rename("firstfile.txt","secfile.txt")
#print(f1.name)
#f1.close()


