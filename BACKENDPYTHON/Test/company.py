# import employee
# print(employee.x)
# employee.add()
#
# # # modulename can be changed in import
# import employee as e
# print(e.x)
# e.add()
#
# import client
# print(client.z)
# client.mul()

import employee,client
print(employee.x)
print(client.z)
employee.add()
client.mul()

import employee as e,client as c
print(e.x)
print(c.z)
e.add()
c.mul()


# another way to access variable and function from another module
#from
from employee import x,add
print(x)
add()

from client import z,mul
print(z)
mul()

from employee import x as d,add as sum
print(d)
print(sum)

from employee import *
print(x)
add()


