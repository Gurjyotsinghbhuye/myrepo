s = set()
s= {1,'karan',1.2,1}
print(s)

s2 = {1,1.2,4,5,'guru'}
print(s2)

print(s.union(s2)) # prints all elements but not duplicating ones

print(s.intersection(s2)) # prints all common elements