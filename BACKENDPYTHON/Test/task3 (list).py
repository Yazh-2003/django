# list
#to find the length
print("Question-1")
l=[10,20,30,90,10,10,40,50]
print(len(l))

print("Question-2")
l=[105,205,305,405,505,605,705,805]
print(len(l))

print("Question-3")
l=["Java","Python","selenium","java","python","selenium"]
print(len(l))

#get the index value
print("Question-4.1")
# l=[10,20,30,90,10,50]
# print(l.index(10))

print("Question-4.2")
l=[10,20,30,90,10,10,40,50]
print(l.index(10,2))

print("Question-4.3")
l=[10,20,30,90,10,10,40,50]
print(l.index(50))

print("Question-4.4")
l=[10,20,30,90,10,10,40,50]
print(l.index(90))

print("Question-4.5")
l=[10,20,30,90,10,10,40,50]
x=l.index(10)
print(x)

print("Question-4.6")
# l=[10,20,30,90,10,10,10,40,50]
# print(l.index(70))

#add values
print("Question-4.7")
l=[10,20,30,90,10,10,10,40,50]
l.append([100,200,300])
print(l)
# print(l.index(200))

print("Question-4.8")
l=[10,20,30,90,10,10,10,40,50]
l.extend([100,200,300])
print(l)

#using index to get a value
print("Question-5.1")
l=[10,20,30,40,50,60]
print(l[2])

print("Question-5.2")
l=[100,200,300,400,500,600,700]
print(l[4])

print("Question-5.3")
l=[105,205,305,405,505,605,705,805]
print(l[-2])

#remove values using index position with some methods
print("Question-6.1")
l=[10,20,30,40,50,60]
l.remove(10)
print(l)

print("Question-6.2")
l=[10,20,30,90,10,10,40]
l.pop()
print(l)

print("Question-6.3")
l=[10,20,30,90,10,10,40]
del l[5]
print(l)

print("Question-6.4")
l=[10,20,30,90,10,10,40]
l.pop()
print(l)

print("Question-6.5")
l=[10,20,30,90,10,10,40,60,80,100]
l.remove(80)
print(l)

print("Question-6.6")
# l=[10,20,30,90,10,10,40,60,80,100]
# l.remove(50)
# print(l)

print("Question-6.7")
l=[10,20,30,90,10,10,10,40,60,80,100]
del l[-5:-1]
print(l)

print("Question-6.8")
l=[10,20,30,90,10,10,10,40,60,80,100]
del l[2:]
print(l)

print("Question-6.9")
# l=[10,20,30,90,10,10,10,40,60,80,100]
# l.clear()
# print(l)

print("Question-7.1")
l=[100,200,300,400,500,600,700]
l[2]=350
print(l)

print("Question-7.2")
l=[10,20,30,90,10,10,40,50,10]
l[7]=90
print(l)

print("Question-7.3")
l=[10,20,30,90,10,10,10,40,50,30]
l[0]=100
print(l)

#add value with use of index
print("Question-8.1")
l=[10,20,30,90,10,10,40,50]
l.insert(2,50)
print(l)

print("Question-8.2")
l=[10,20,30,90,10,10,10,40,50]
l.append(70)
print(l)

print("Question-8.3")
l=[10,20,30,90,10,10,10,40,50]
l.insert(30,80)
print(l)

print("Question-8.4")
l=[10,20,30,90,10,10,40,50]
l.insert(6,100)
print(l)

print("Question-9.1")
# l=[10,20,30,90,10,10,40,50]
# l.append(100,200,300)
# print(l)

print("Question-9.2")
l=[10,20,30,90,10,10,40,50]
l.append([100,200,300])
print(l)

print("Question-10.1")
l=[10,20,30,90,10,10,40,50]
l.extend([100,200,300])
print(l)

print("Question-10.2")
l=[10,20,30,90,10,10,40,50]
print(l.count(10))

#find min and max
print("Question-10.3")
l=["java","python","selenium","Java","Python","Selenium"]
print(max(l))

print("Question-10.4")
l=[10,20,30,90,10,10,10,40,50]
print(min(l))

print("Question-10.5")
l=["java","python","selenium","Java","Python","Selenium"]
print(min(l))

print("Question-10.6")
l=[10,20,30,90,10,10,10,40,50]
print(max(l))

print("Question-11.1")
l=[10,20,30,50,90,40,100,60,10,70]
l.reverse()
print(l)

print("Question-11.2")#ascending order
l=[10,20,30,50,90,40,100,60,10,70]
l.sort()
print(l)

print("Question-11.2")#descending order
l=[10,20,30,50,90,40,100,60,10,70]
l.sort(reverse=True)
print(l)

print("Question-12.1")
l=[10,20,30,90,10,10,40,50]
c=l.copy()
print(c)

print("Question-12.2")
l1=[10,20,30,90,10,10,10,40,50]
l2=[30,40,50,60,80]
if(l1==l2):
    print("both list are same")
else:
    print("both list are different")

print("Question-12.3")
l1=[10,20,30,90,10,10,40,50]
l2=[10,20,30,90,10,10,40,50]
if(l1==l2):
    print("both list are same")
else:
    print("both list are different")

print("Question-13.1")
l=[105,205,305,405,505,605,705,805]
for x in l:
    print(x)

print("Question-13.2")
l=[105,205,305,405,505,605,705,805]
for x in enumerate(l):
    print(x)

print("Question-13.3")
l=[105,205,305,405,505,605,705,805]
for index,value in enumerate(l):
    if(index%2!=0):
        print(value)










