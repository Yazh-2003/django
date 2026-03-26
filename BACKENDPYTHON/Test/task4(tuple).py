#tuple
print("Question-1.1")
t=(10,20,30,90,10,10,40,50)
print(t)
print(len(t))

print("Question-1.2")
t=(100,200,300,400,500,600,700)
print(t)
print(len(t))

print("Question-1.3")
t=("python","selenium","sql","java")
print(t)
print(len(t))

print("Question-1.4")
t=(10,20,30,90,10,10,40,50)
print(t)
print(len(t))

print("Question-2.1")
t=(10,20,30,90,10,10,40,50)
print(t)
print(t.index(50))

print("Question-2.2")
t=(10,20,30,90,10,10,40,50)
last_index=len(t)-1 - t[::-1].index(10)
print(last_index)

print("Question-2.3")
t=(10,20,30,90,10,10,40,50)
print(t.index(50))

print("Question-2.4")
# t=(10,20,30,90,10,10,40,50)
# print(t.index(200))

print("Question-2.5")
t=(10,20,30,90,10,10,40,50)
for index,value in enumerate(t):
    if value==10:
        print(index)

print("Question-3.1")
t=(10,20,30,40,50,60)
print(t[2])

print("Question-3.2")
t=(100,200,300,400,500,600,700)
print(t[4])

print("Question-3.3")
# t=(105,205,305,405,505,605,705,805)
# print(t[12])

print("Question-3.4")
t=(105,205,305,405,505,605,705,805)
print(t[-3])

print("Question-3.5")
t=(105,205,305,405,505,605,705,805)
print(t[-8])

print("Question-4.1")
t=(10,20,30,90,10,10,10,40,50)
a=list(t)
print(a)
a.append(100)
print(a)

print("Question-4.2")
t=(10,20,30,90,10,10,10,40,50)
t=t+("python",)
print(t)

print("Question-4.3")
t=(10,20,30,90,10,10,10,40,50)
t=t+(100,200,300)
print(t)

print("Question-4.4")
t=(10,20,30,90,10,10,10,40,50)
t=t+("java","python")
print(t)

print("Question-5.1")
t=(10,20,30,90,10,10,10,40,50)
print(t.count(10))

print("Question-5.2")
t=(10,20,30,90,10,10,10,40,50)
print(max(t))

print("Question-5.3")
t=("python","selenium","sql","java")
print(max(t))

print("Question-5.4")
t=(10,20,30,90,10,10,10,40,50)
print(min(t))

print("Question-5.5")
t=("python","selenium","sql","java")
print(min(t))

print("Question-6.1")
a="python"
b=tuple(a)
print(b)

print("Question-6.2")
list=["java","python","selenium",20,10,60]
tuple=tuple(list)
print(tuple)

print("Question-7.1")
# t=(105,205,305,405,505,605,705,805)
# print(t.__contains.__(200))

print("Question-7.2")
t=(105,205,305,405,505,605,705,805)
print(t.__contains__(505))

print("Question-7.3")
t1=(10,20,30,40,50,60)
t2=(60,20,30,40,50,60)
if t1==t2:
    print("both are same")
else:
    print("both are different")

print("Question-8.1")
t=(105,205,305,405,505,605,705,805)
for i in t:
    print(i)

print("Question-8.2")
for x in enumerate(t):
    print(x)

print("Question-8.3")
for index,value in enumerate(t):
    if index%2==0:
        print(value)