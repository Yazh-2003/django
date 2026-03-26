def Sample():
    print("hello")
Sample()
# 1.function without arguments
def Sum():
    a=2
    b=3
    c=a+b
    print(c)
Sum()

# 2.functions with arguments
def Sum(a,b):
    c=a+b
    print(c)
Sum(1,3)

# 3.function without return type
# def add(a,b):
#     c=a+b
#     print(c)
#   result=add(2,4)
# print(result)

# 4.function with return type
def add(a,b):
    c=a+b
    return c
result=add(1,2)
print(result)

def add(a,b):
    c=a+b
    return 100
result=add(1,2)
print(result+50)

# 5.function with multiple returntype
def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
result=cal(1,2)
print(result)

a,b,c,d=cal(1,2)
print(a,b,c,d)

# 6.function with multiple var length
def Sample(*n):
    print(n)
Sample(1,2,3,4)


def employeedetails():
    print("employee id is 100")
    print("employee name is yaazh")
employeedetails()

# 7.function without keyword arguments
def employeedetails(eid,ename):
    print("employee id is",eid)
    print("employee name is",ename)
employeedetails(100,"Eniya")
employeedetails(10,"abi")

# 8.function with keyword arguments
def employeedetails(eid,ename):
    print("employee id is",eid)
    print("employee name is",ename)
employeedetails(eid=100,ename="Eniya")
employeedetails(eid=1,ename="abi")

# 9.function without default value
# def employeedetails(eid,ename):
#     print("employee id is",eid)
#     print("employee name is",ename)                 //error
# employeedetails(eid=100)
# employeedetails(ename="abi")

# 10.function with default value
def employeedetails(eid=100,ename="yaazh"):
    print("employee id is",eid)
    print("employee name is",ename)
employeedetails(ename="Eniya")
employeedetails(eid=2)


# 11.function with default value -----none
def employeedetails(eid=None,ename=None):
    print("employee id is",eid)
    print("employee name is",ename)
employeedetails(eid=10)
#
# def employeedetails(eid=None,ename):
#     print("employee id is",eid)                        //error
#     print("employee name is",ename)
# employeedetails()

# 12.function with multiple keyword length
def sample(**n):
    print(n)
sample(age=22,name="yaazh",email="yalini@gmail.com")