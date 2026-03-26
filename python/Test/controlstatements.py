#if
mark=2
if(mark>=35):
    print("pass")

#if else
mark=60
if mark>=35:
    print("pass")
else:
    print("fail")

#nested if
age=40
weight=65
if age<=35:
    if weight<=60:
       print("able to donate due to weight")
else:
    print("not able to donate due to age")

#and operator
age=34
weight=67
if age>=35 and weight>=60:
    print("able to donate")
else:
    print("not able to donate");

#or operator
age=29
height=50
if age<=5 or height<=18:
    print("half ticket")
else:
    print("full ticket")
