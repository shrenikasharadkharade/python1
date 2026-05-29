
#funtion
def add(a,b):
    """ adding 2 numbers """
    c=a+b
    print(c)

add(10,2)

#list 

list=[1,2,3,4,5]
print(list)
list[0]=0
print(list[0:2])

#tuple

tup=(1,2,3,4,5)
print(tup)

print(tup[1])

#set

set={1,2,3,4,4}
print(set)


#dictionary

dict={"name":"Shrenika","age":20,"address":"Gaurgaon"}

print(dict)
print(dict['name'])

print(dict.keys())

print(dict.values())

#string

name="my name is Shrenika"
print(name)

print(type(name))
print(name)
print(name[0:5])

#module

import math

print(math.sqrt(25))

print(math.ceil(5.4))

print(math.floor(5.2))

print(math.pow(2,3))


#operators

def operators(a,b):

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)  
    print(a^b)

    if a>b:
        print('a is greater')
    else:
        print('a is smaller')


operators(10,20)