#functions
#sliceoperator,len(),index(),find(),startswith(),endswith(),count(),capitalize(),upper(),lower(),isupper(),
#islower(),strip(),lstrip(),rstrip(),replace(),isalnum(),isnumeric(),isalpha(),split()

#eg1:
str="python"
print(str)

#1 len
l=len(str)
print(l) #6
print(str[5]) #n
print(str[-3]) #h

#index----to get index value
print(str.index("n")) #5
#to check in reverse order
print(str.rindex("o"))

#find
print(str.find("n"))#5
print(str.find("m"))#-1

#eg:
s="welcome to greens technology"
print(s)
#startswith------returns true or false
print(s.startswith("greens"))#false
print(s.startswith("welcome"))#true

#endswith-----------------
print(s.endswith("technology"))#true
print(s.endswith("to"))#false

#contains--------checks if the word is present or not
print(s.__contains__("technology"))
print(s.__contains__("hello"))#false

#isupper
s="pYthOn"
print(s)
print(s.isupper())#false

#upper ---- change to uppercase
print(s.upper())#PYTHON

#islower
print(s.islower())#false

#lower---change to lowercase
print(s.lower())#python

#captitalize---only 1st letter is changed into capital
print(s.capitalize())#Python

#title------changes 1st letter in two words
a="hello world"
print(a.title())#Hello World

#count
print(a.count("l"))#3
print(a.count("m"))#0

#sliceoperator
print(s[2:4:1])#th
print(s[0:4:1])#pYth
print(s[::1])#pYthOn

#strip------removes extra space
b="                     greens  technology           "
print(b.strip())

#lstrip--left strip
print(b.lstrip())

#rstrip-----right strip
print(b.rstrip())

#replace
print(a.replace("hello","java"))
print(a.replace("l","*"))

#isalpha
s1="Python"
s2="2026"
s3="Python2026"
print(s1.isalpha())#true
print(s2.isalpha())#False
print(s3.isalpha())#False

#isnumeric
print(s1.isnumeric()) #False
print(s2.isnumeric())#true
print(s3.isnumeric())#false

#isalnum
print(s1.isalnum())#True
print(s2.isalnum())#True
print(s3.isalnum())#True












