# def sample():
#     print("hello")
#     sample()
# sample()

#types of variable
# local and global
#local
def add():
     a=8
     print(a)
add()

#global
b=2
def add():
    print(b)
add()
print(b)

def sub():
    print(b)
sub()
print(b)

#note
c=4
def sample():
    c=5
    print(c)                   #accepts only local variable value
sample()

#to access global variable
c=4
def sample():
    c=3
    print(globals()["c"])
    print(globals().get("c"))
sample()


# to convert local variable to global variable
def cal():
    global d
    d=3
    print(d)
cal()
def sample():
    print(d)
sample()

# examples
count=0
# def sample():
#     global count
#     print("hello")
#     count=count+1
#     sample()
# sample()

# another way to get only 100 times of hello
count=0
def sample():
    global count
    print("hello")
    count=count+1
    if(count<=100):
        sample()
sample()