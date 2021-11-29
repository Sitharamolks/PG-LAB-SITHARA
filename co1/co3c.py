c=str(input("enter a word"))
print("orginal word",c)
print("vowels are")
for i in c:
    if i in "aeiouAEIOU":
        print([i])
