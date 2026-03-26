print("1--------------------------------")
#question-1
for x in range(1,100):
    if x==5:
       print(x)
print("2------------------------------------")
#Question-2
for x in range(1,100):
    if x==5:
        break
    print(x)
print("3------------------------")
#Question-3
for x in range(1,100):
    if x==5:
        continue
    print(x)
print("4-------------------------------------")
#Question-4
for x in range(1,4):
    for y in range(1,4):
     print(y)
print(x)

print("5-----------------------")
#question 5
for x in range(1,4):
    for y in range(1,4):
        print(x)

print("6---------------------------")
#question6
for x in range(1,4):
    for y in range(1,x):
        print(y)

print("7---------------------------")
for x in range(1,4):
    for y in range(x+1,4):
        print(y)

print("8---------------------------")
for x in range(1,4):
    for y in range(x+1,x):
        print(y)

print("9----------------------------------")
# i=5
# if i==5:
#     continue

print("10-------------------------------")
# i=5
# if i==5:
#     break

print("11---------------------")
for x in range(1,100):
    if(x==5):
        print(x)
#PROGRAMS
print("Question-1")
age=10
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")

print("Question-2")
i=10
if(i%2==0):
    print("Even")
else:
    print("Odd")

print("Question-3")
# for i in range(1,101):
#     if(i%2==0):
#         print(i)

print("Question-4")
sum=0
for i in range(1,101):
    if(i % 2 !=0):
     sum=sum+i
print(sum)

print("Question-5")
count=0
for i in range(1,101):
    if(i%2==0):
        count=count+1
print(count)

print("Question-6")
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)

print("Question-7")
a=0
b=1
while a<=100:
    print(a)
    c=a+b
    a=b
    b=c

