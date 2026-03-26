#type conversion
#int-----round off numbers
a=10
print(a)
print(type(a))
print("----------------------------------------------------")

#float----decimal values
a=1.8
print(a)
print(type(a))
print("--------------------------------------------------------")
#complex-----real part + imaginary part(1+8j)
a=3+7j
print(a)
print(type(a))
print("---------------------------------------------------------")

#boolean---True/False
#True
a=True
print(a)
print(type(a))
#False
a=False
print(a)
print(type(a))
print("----------------------------------------------------------")

#string----''/""
a="yazhini"
print(a)
print(type(a))
print("-----------------------------------------------------------------")


#Exampeles
#1 with integers
a=3
b=3
print(a+b)
print("-----------------------------------------")

#2 with strings
a="hi"
b="yazhini"
print(a+b)
print("---------------------------------------------")

#adding int and str (use comma only)
a="yazhini"
b=2003
#print(a+b)#TypeError
print(a,b)
print("------------------------------------------------")

#input----get the i/p from user at runtime
# age=input()
#print(age)
print("--------------------------------------------------------")

a=3
b=3
c=a+b
print(c)
print("----------------------------------------------------")

# using input method
#a=input()
#print(type(a))
#b=input()
#print(type(b))
#c=a+b
#print(c)
print("------------------------------------------------------")
#type conversion
#1.integer
print(int(3))
print(int(3.3))
#print(int(3+8j))#TypeError
print(int(True))
print(int(False))
print(int("3"))
#print(int("yazhini"))#ValueError
print("--------------------------------------------------------")

#2.float
print(float(3))
print(float(3.3))
#print(float(3+8j))#TypeError
print(float(True))
print(float(False))
print(float("3"))
#print(float("yazhini"))#ValueError
print("--------------------------------------------------------")

#3.complex
print(complex(3))
print(complex(3.3))
print(complex(3+8j))#TypeError
print(complex(True))
print(complex(False))
print(complex("3"))
#print(complex("yazhini"))#ValueError
print("--------------------------------------------------------")

#4.bool
print(bool(3))
print(bool(3.3))
print(bool(3+8j))#TypeError
print(bool(True))
print(bool(False))
print(bool("3"))
print(bool("yazhini"))#ValueError
print("--------------------------------------------------------")

#5.string----str
print(str(3.3))
print(str(3+8j))#TypeError
print(str(True))
print(str(False))
print(str("3"))
print(str("yazhini"))#ValueError
print("--------------------------------------------------------")

#examples
#1
#a=int(input())
#b=int(input())
#c=a+b
#print(c)

#2.
a=int(input("enter a value"))
b=int(input("enter b value"))
c=a+b
print(c)











