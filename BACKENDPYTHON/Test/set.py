#set - {}
#random order
#ignore duplicate values
#methds uses in set are
#len(),add(),update(),remove(),discard(),pop(),copy(),clear(),sorted(),,union(),intersection(),difference(),
# symmetric_difference()

s={10,20,30,40,50,60}
print(s)

# to find the length
print(len(s))

#we can't get a particular value ,but we can add values
#add---update
#add--add only one value in a set
s.add(100)
print(s)

# s.add(200,300)
# print(s)

#update----adding more than one values
s.update({200,300,400})
print(s)

#changing list to set
s={10,20,33,40}
l=[1,2,3,4]
s.update(l)
print(s)

#delete the values
#remove
s.remove(1)
print(s)

#discard
# s.discard(200)
# print(s)

#pop---delete the 1st value in a set
s.pop()
print(s)

#clear---clear all values in a set
# s.clear()
# print(s)

#min and max
print(min(s))
print(max(s))

#contains
print(s.__contains__(10))
print(s.__contains__(20))

# in
print(10 in s)

# not in
print(11 not in s)

# copy
a=s.copy()
print(a)

#print all values
for x in s:
    print(x)

#using enumerate
for x in enumerate(s):
    print(x)


s1={1,2,3,4}
s2={3,4,5,6}
#union
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

#by using symbols
print(s1 &s2)
print(s1 ^s2)
print(s1 - s2)
print(s1 | s2)
