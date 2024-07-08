# 1)
# n=int(input("enter a number:"))

# def fac(n):
#     if (n==1 or n==0):
#         return  n
# x=list(map(fac,n))
# print(x)


#2)
# def fac(n):
#     if n==0:
#         return 1
#     else :
#         return n * fac(n-1)
# # m=float(input("enter a num:"))
# y=fac(5)
# print(y)


#3)

# num=17

# for i in range(1,num):
#     if num%i!=0:
#         print("not prime",num)
#         break
        
#     else :
#         print("prime")



  #######------------------------------reduce  question
# from functools import reduce
# my_list=(1,2,3,4,5,6,7,8,9,10)
# def max(x,y):     #  max
#     if x>y:
#         return x
   
#     else:
#         return x
    
    
# def min(m,n):    # min
#     if m>n:
#         return m
#     else :
#         return n
    
# def total(a,b):   # total 
#     return a-b
    
    

# x=reduce(max,my_list)
# y=reduce(min,my_list)
# total=reduce(total,my_list)
# print("max:",x)
# print("min:",y)
# print("total:",total)

#---------------reduce end -----------




####################   Map question ----------
# 1) 
# my_list=(13,42,53,64,57,6,87,89,94,10)
# print(my_list)

# def sqr(val):
#   return val*val
# x=map(sqr,my_list)
# print(list(x))


# ## 2)
# my_list=(13,42,53,64,57,6,87,89,94,10)
# print(my_list)

# def sq(val):
#     return val+5


# y=map(sq,my_list)
# print(y)
# print(list(y))



#  3)

# my_list=(13,42,53,64,57,6,87,89,94,10)
# print(my_list)

# def even(n):
#    if n%2==0:
#       return "even"
#    else :
#       return "odd"
   

# x=map(even,my_list)
# print(list(x)) 

### 4)

# name="BHopal"

# def car(n):
#     b=ord(n)
#     return b+6
# x=map(car,name)
# print((list(x)))


#5)

# name="BHopal"

# def car(n):
#     b=ord(n)
#     return chr(b+2)
# x=map(car,name)
# print((list(x)))





###################------------------------- Filter question ----

### 2)

# my_list=(13,42,53,64,57,6,87,89,94,10)
# print(my_list)

# def even(n):
#     if n%2==0:
#         return n
# def odd(n):
#     if n%2!=0:
#         return n
    
# x=filter(even,my_list)
# y=filter(odd,my_list)
# print(list(x))
# print(list(y))

 ####  2)

# my_list=(13,42,53,64,57,6,87,89,94,10)
# print(my_list)

# def even(n):
#     if n>=50:
#         return n
# x=filter(even,my_list)
# print(list(x))




#### -------------- lambda function question--


# a=lambda x,y,z:2*x+5*y+9*z 
# print(a(10,20,30))

# n=lambda name: print("hye i am :",name)
# n("ankitttt")
# new=input("enter your second name:")
# n(new)


# a=lambda x,y,z:2*x+5*y+9*z 
# x=int(input(" "))
# y=int(input(" "))
# z=int(input(" "))
# sum=a(x,y,z)
# print("total sum",sum)


from functools import reduce

my_list=[10,2,23,5,3,85,38,94]
x=reduce(lambda a,b : a+b  ,my_list)
print(x)



my_list=[10,2,23,5,3,85,38,94]
x=reduce(lambda a,b : a if a>b else b  ,my_list)
print(x)


my_list=[10,2,23,5,3,85,38,94]
x=list(filter(lambda a : a%2==0  ,my_list))
print(x)

my_list=[10,2,23,5,3,85,38,94]
x=list(filter(lambda a : a%2!=0  ,my_list))
print(x)

my_list=[10,2,23,5,3,85,38,94]
x=list(map(lambda a : a+10  ,my_list))
print(x)







