#list[]
#methods:
#sliceoperators,len(),insert(),remove(),pop(),index(),count(),max(),min(),append(),extend(),sort(),sorted(),
#reverse(),copy(),del(),clear()

#l=[1,"python",2.4,True]
#print(l)
#print(type(l))

l=[10,20,30,40,50,10]
print(l)

#len
print(len(l))#5

#get a particular value
print(l[0])#10
#print(l[9])#indexerror

#index
print(l.index(50))#4
print(l.index(20))#1
print(l.index(10,2))
print(l.index(10,2,8))

#sliceoperator
print(l[0:4:1])
print(l[::])

#add values by using methods
#1)append 2)insert 3)extend

#append()----add value in list
l.append(100)
print(l)

# l.append([100,200])
# print(l)

#extend()
#to add multiple values use extend method
l.extend([300,200,100])
print(l)

#insert()---works with position
l.insert(0,200)
print(l)

l.insert(1,[12,2])
print(l)


#delete
#to delete the values in the list just use the methods
#1)remove 2)del 3)pop 4)del 5)clear()

#remove()
l.remove(200)
print(l)

#pop--delete the last value in a list
l.pop()
print(l)    #if we don't give a value inside a parentheses --pop will delete the last value

l.pop(2)
print(l)

#del---works based on index
del l[3]
print(l)


#clear()-----clear everything
# l.clear()
# print(l)

#contains
print(l.__contains__(100))
print(l.__contains__(10))

#in
print(4 in l)
print(50 in l)

#not in
print(4 not in l)
print(300 not in l)

#copy
a=l.copy()
print(a)

#count
print(l.count(10))

#repalce
l[3]=1000
print(l)

#min and max
l=[1,2,3,4,5]
print(min(l))
print(max(l))

#sort
l.sort()
print(l)

#sort with reverse
l.sort(reverse=True)
print(l)


#sorted
e=sorted(l)
print(e)

l=[10,20,30,40,50,60,70]
#print all values using for loop
for i in range(0,9):
    print(i)

#enhanced loop
for i in l:
    print(i)


#enumerate
for x in enumerate(l):
    print(x)

    for index ,value in enumerate(l):
        print(value)

