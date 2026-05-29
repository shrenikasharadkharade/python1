# a=int(input("Enter number : "))
# b=int(input("Enter number : "))
# sum=a+b
# print("Sum : ",sum)
# if sum%2==0:
#     print("even")
# else:
#     print("odd")
# for i in range(1,6):
#     print(i)

# a=10
# b=20.5
# c=2+3j
# d="hey"
# e=[1,2,3,4]
# f=(1,2,3,4)
# g={1,2,3,4}
# h={"name":"Shrenika","age":21}
# i=True
# print("a : ",a," Type : ",type(a))
# print("b : ",b," Type : ",type(b))
# print("c : ",c," Type : ",type(c))
# print("d : ",d," Type : ",type(d))
# print("e : ",e," Type : ",type(e))
# print("f : ",f," Type : ",type(f))
# print("g : ",g," Type : ",type(g))
# print("h : ",h," Type : ",type(h))
# print("i : ",i," Type : ",type(i))

# print("Simple calculator")
# print("1.Addition")
# print("2.Substraction")
# print("3.Multiplication")
# print("4.Division")
# op=int(input("Enter operator: "))
# a=int(input("Enter number : "))
# b=int(input("Enter number : "))
# if op==1:
#     result=a+b
#     print("Result : ",result)  
# elif op==2:
#     result=a-b
#     print("Result : ",result)  
# elif op==3:
#     result=a*b
#     print("Result : ",result) 
# elif op==4:
#     result=a/b
#     print("Result : ",result) 
# else:
#     print("Input valid operator")

# num=int(input("Enter number : "))
# temp=num
# sum=0
# n=len(str(num))

# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if sum==num:
#     print(num," is armstrong number")
# else:
#     print(num," is not armstrong number")

# mylist=[1,2,3,4,5,6,7]
# print("My list : ",mylist)
# mylist.append(10)
# print("Appended list : ",mylist)
# mylist.insert(3,100)
# print("Inserted list : ",mylist)
# mylist.remove(5)
# print("Removed list : ",mylist)
# print("Accessing value : ",mylist[4])
# mylist[6]=900
# print("list: ",mylist)
# print("Length of list : ",len(mylist))

# dict={
#     "name":"Shrenika",
#     "age":22,
#     "abc":1
# }
# print("Dictionary : ",dict)
# print("Accessing : ",dict["age"])
# dict["marks"]=90
# print("Added dictionary : ",dict)
# dict["age"]=21
# print("updated dictionary : ",dict)
# dict.pop("abc")
# print("removed : ",dict)
# print("keys :",dict.keys())
# print("values :",dict.values())

set1={1,2,3,4}
set2={3,4,5,6}
print("set 1 : ",set1)
print("set 2 : ",set2)
print("Union : ",set1.union(set2))
print("Intersection : ",set1.intersection(set2))
print("Difference : ",set1.difference(set2))
print("Symmetric difference : ",set1.symmetric_difference(set2))
