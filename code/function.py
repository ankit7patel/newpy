#reusevilit krta hai     iko cll krna padta h
# def add(x,y): #1  types
#     z=x+y
#     return z
# z=add (10,20)
# print(z)



# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def multi(x, y):
#     return x * y 

# def div(x, y):
#     if y != 0:  # Corrected to check if y is not zero
#         return x / y
#     else:
#         return "Division by zero is not allowed"

# while True:
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     n = input("Enter (1, 2, 3, 4, 5):")

#     if n == '5':
#         break

#     x = int(input("Enter 1st number:"))
#     y = int(input("Enter 2nd number:"))

#     if n == '1':
#         print(f"Result: {add(x, y)}")
#     elif n == '2':
#         print(f"Result: {sub(x, y)}")
#     elif n == '3':
#         print(f"Result: {multi(x, y)}")
#     elif n == '4':
#         print(f"Result: {div(x, y)}")
#     else:
#         print("Invalid input, please enter a number between 1 and 5")


# def add(x,y):   #4 types
#     z=x+y
#     print(z)  #print(print(add(10,20)))
# print(add (10,20))   


# def add(x,y):   #2  types
#     z=x+y
#     print(z)
# z=add (10,20)

 # 2 bar prnt krra hai isi liye retune ka use krege ye value ko retune krt hai print ni krta 2 baar 


# def add(x,y): #3 
#     z=x+y
#     sub=x-y
#     multi=x*y
#     return z , sub , multi 
# p=int(input("enter f no"))
# s=int(input("enter s no"))
# z=add (p,s)
# print(z)


# def add(x=0,y=0): #5
#     z=x*x
#     return z
# p=int(input("enter f no"))
# # s=int(input("enter s no"))
# z=add (p)   # aruments
# print(z)


# def add(x,y): #3 
#     z=x*y
#     return z
# # p=int(input("enter f no"))
# # s=int(input("enter s no"))
# z=add (x=10,y=5)   # aruments
# print(z)


# def squ(x): #3 
#     z=x*x
#     return z
# p=int(input("enter f no"))
# # s=int(input("enter s no"))
# z=squ(p)   # aruments
# print("squ:", z)



# def add(*x):    #VALUE DETA HAI
#     add=0
#     for i in x:
#         add+=i
#         # return add
#     print("add:",add)
# add(10,20)
# add(10,20,30,40,50,4,3,3,333,2636,61)


# def add(*x):    #NONE RETURN KREGA
#     add=0
#     for i in x:
#         add+=i
#     print("add:",add)

# z = add(10,20,2,3,22,23,34)
# y=add(55,55)
# print(z,y)


# def emply_data(**data):      # dict ki values acces krna ho
#     for i,j in data.items():
#         print(i,"=",j)

# emply_data(name="ankittt" ,city="bhopal")

  



#============================  [  scopes  ]---- local,global==================
#type 1



# def add(x):    
#     y=10    # y local varivale   body ke andr hi acces kr skte hai
#     sum=x+y   # local ko pehle rkhta hai
#     print(sum)
# n=int(input("enter a no:"))
# add(n)
# # print(y) 



# z=10        #z globle varible hai  isko sb jghe use kr skte hai 
# def add(x):
#     sum=x+z
#     print(sum)
# m=int(input("enter a no:"))
# add(m)
# print(z)


# z=30      #z globle varible hai  isko sb jghe use kr skte hai 
# def add(x):
#     z=10         # local varible ko pehle kega uske baad globale 
#     sum=x+z
#     print(sum)
# m=int(input("enter a no:"))
# add(m)
# print(z)



# in blud global func()===globals['']



# z=1000      #z globle varible hai  isko sb jghe use kr skte hai 
# def add(x):
#     # global z     # local varible bahr acces krna ho to global ka use krte hai
#     z=10
#     sum=x+z
#     sum=x+globals()['z']   # globals ka use local acces me krna ho  
#     print(sum)
# m=int(input("enter a no:"))
# add(m)
# print(z)


# z=10000000000
# print(z)




# y=20     #z globle varible hai  isko sb jghe use kr skte hai 
# def add(x):
#     # global y     # local varible bahr acces krna ho to global ka use krte hai
#     y=50     #------>local values deta hai
#     sum=x+globals()['y']   # globals ka use local acces kr skte hai 
#     sum=x+y
#     print(sum)
# # m=int(input("enter a no:"))
# # y=50    ##### ===========globle ki values ko overwrite krta hai ye local value ko hi dega 
# add(100)
# print(y)   #-----> 


# y=1111    #  y last value print krega 
# print(y)







# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def multi(x, y):
#     return x * y 

# def div(x, y):
#     # if y != 0:
#     #     return x / y
#     if x != 0:
#         return x/y

# while True:
#     print("1 - Add")
#     print("2 - Subtract")
#     print("3 - Multiply")
#     print("4 - Divide")
#     print("5 - Exit")

#     n = int(input("Enter (1,2,3,4,5): "))

#     if n >  5:
#         break
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))

#     if n == 1:
#         print("addition:", add(x, y))
#     elif n == 2:
#         print("subtract:", sub(x, y))
#     elif n == 3:
#         print("multiply:", multi(x, y))
#     elif n == 4:
#         print("divide:", div(x, y))
#     else:
#         print("back")






# x=int(input("enter "))
# y=int(input("enter "))
# add=x+y
# sub=x-y
# multi=x*y
# divi=x/y
# print(add)
# print(sub)
# print(multi)
# print(divi)







