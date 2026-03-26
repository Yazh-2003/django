#control statements
#Decision making
#if condition
mark=60
if mark>=35:
    print("pass")

#if else
mark=30
if mark>=35:
    print("pass")
else:
    print("fail")

#nested if
age=5
weight=120
if age>=18:
    if weight>=50:
     print("able to donate the blood")
    else:
        print("not able to donate the blood due to weight")
else:
    print("not able to donate the blood due to age")

#and operator
age=10
weight=50
if(age>=18 and weight>=50):
    print("able to donate the blood")
else:
    print("next person")

#or operator
age=7
height=150
if age<=5 or height<=120:
    print("half ticket")
else:
    print("full ticket")

#elif
a=10
b=20
c=30
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
        print("B is greater")
else:
        print("C is greater")


#