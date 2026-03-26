# lambda exppression is also called as anonymous function (or) nameless function
def even(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
even(20)

# lambda exp gives o/p in T or F for condition only
e=lambda a:a%2==0
print(e(8))


def square(a):
    print(a*a)
square(3)

e=lambda a:a*a
print(e(3))



