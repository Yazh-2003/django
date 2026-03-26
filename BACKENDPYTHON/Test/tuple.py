#tuple
#methods
#sliceoperator
#count
#min
#max
#index

t=(1,2,3,4,5)
print(t)
print(type(t))

#to find length-----use len()
print(len(t))

#get a particular value
print(t[3])

#slice operator
print(t[::])
print(t[0:2])

#in tuple ---can't add values in tuple
# print(t+100)
g=(3,4,5)
print(t+g)

#delete
print(t[0:3:1])

# contains
print(t.__contains__(1))
print(t.__contains__(2))

#in
print(3 in t)
print(1 in t)

#not in
print(7 not in t)
print(1 not in t)

#count
t=(1,1,3,2,4,5)
print(t.count(1))

#min and max
print(min(t))
print(max(t))

#print all values using range
for i in range(1,6):
    print(i)

#using enhanced loop to iterate each value in tuple
for x in t:
    print(x)

#enumerate
for x in enumerate(t):
    print(x)
