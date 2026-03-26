#looping
#for loop
for i in range(0,5,1):
    print(i)
print("-------------------")

#nested for loop
for i in range(0,3,1):
    for j in range(0,3,1):
        print(j)
print(i)
print("-------------")

#increment by 2
for i in range(0,5,2):
    print(i)
print("----------------------")

for i in range(0,10,-1):
    print(i)
print("----------------------")
#while loop
a=10
while(a<14):
    print(a)
    a=a+1

#jumpstatements
#break-- stops the entire loop
for i in range(0,5,1):
    if i==2:
        break
    print(i)

#continue--- skips the condition
for i in range(0, 5, 1):
    if i == 2:
        continue
    print(i)

#exit()
for i in range(0, 5, 1):
    if i == 2:
        exit()
    print(i)
print("end")




