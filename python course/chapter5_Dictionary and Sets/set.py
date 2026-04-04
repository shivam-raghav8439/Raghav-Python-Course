a={2,4,5,7,8,12,23}
print(a)
print(type(a))

e=set() # empty set make like this 
print(type(e))

# Set Methods 
a.add(13)
print(a)
a.remove(7)
print(a,type(a))
a.clear()
print(a)
# Set union 
r1={4,5,8,54,29,10}
r2={23,45,8,29,34,54,234}
print(r1.union(r2))

# intersectiion ( Which VAlue are common < They will bhe print )
print(r1.intersection(r2))
print({8,5}.issubset(r1))
print({5,8}.issuperset(r1))

# Union 
print(r2.union(r1))