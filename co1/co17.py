import operator
d = {7: 2, 3: 4, 9: 3, 2: 12, 0: 0}
print("orginal list",d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1)) 
print('Dictionary in ascending order by value ',sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value :',sorted_d)
