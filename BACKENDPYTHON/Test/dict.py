# to store multiple values
# {key:value}
# key does not allow dupilcates
# values allows duplicates
d={1:"yaazh",2:"durga",3:"vincy"}
print(d)

#len---to find length of the dict using len
print(len(d))

#get a value
print(d[2])

# or use get() method
pv=d.get(4)
print(pv)

#to add values
#update
d.update({4:"java"})
print(d)
          # or
g={5:"python",6:"sql"}
d.update(g)
print(d)

#to delete value
#pop---pop key onl
d.pop(6)
print(d)

#popitem----delete last value
d.popitem()
print(d)

#to access keys alone
k=d.keys()
print(k)
print(type(k))

# to access values
v=d.values()
print(v)

# contains
print(d.__contains__(4))
print(d.__contains__(3))

#in
print( 4 in d)
print(3 in d)

#not in
print(4 not in d)
print(3 not in d)

#items ----to get both keys and values
i=d.items()
print(i)

for x in d.items():
    print(x)

# max and min
print(min(d))
print(max(d))

# copy
c=d.copy()
print(c)

# replace
d[3]="selenium"
print(d)