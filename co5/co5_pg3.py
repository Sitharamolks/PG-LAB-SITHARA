import csv
 # csv file name
filename = "username.csv"
 # initializing the titles and rows list
fields = []
rows = []
 # reading csv file
cf=open(filename, 'r')
 # creating a csv reader object
csvreader = csv.reader(cf)
 
 # extracting field names through first row
fields = next(cf)
print(fields)
 
 # extracting each data row one by one
for r in csvreader:
 rows.append(r)
 #print the list containing the rows of csv file
print(rows)
print("...............")
print('\nFirst 3 rows are:\n')
for r in rows[:3]:
 print(*r)
 print()
print("The file content")
for sl in rows:
 for l in sl:
  print(l),
 #print(l,end=" ")
  print()
cf.close()
