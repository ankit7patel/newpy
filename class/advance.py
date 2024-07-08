# map()------> (function ,collenction)--->  same logic lgna ho tb  === map me sabi pr same itretion krta hai 

################### higher order function ()  ------->>>>>> collection pr kamm krta hai jaha coll. rehta hai heiger order func. ka use krege 
#filter()----->  filter me total object se kam nikna ho to 



# my_list=[10,20,30,40,50]
# print(my_list)
# new_list=[]
# for i in my_list:
#     sum=i+5
#     new_list.append(sum)
# print(new_list)






# my_list=[10,20,30,40,50]
# print(my_list)

# def add(n):
#     return n*n

# x=map(add,my_list)

# print(x)
# print(list(x))
# print(list(x))
# print(type(x))





# my_list=[10,20,30,40,50]
# print(my_list)

# def add(n):
#     return n**2

# x=map(add,my_list)

# # print(x)
# # print(tuple(x))
# print(list(x))
# # print(type(x))






# n=input("enter your name:")
# print(n)
# def name(i):
#     return  ord(i)
# x=map(name,n)
# # print(x)
# print(list(x))







# my_list=[10,20,30,25,15]     # ( ----even oddd ----) flter ka use krke 
# def even(n):
#      if (n %2 == 0) :
#         return True
# def odd(n):
#      if (n %2 != 0) :
#         return True
     
# x=filter(even,my_list)
# y=filter(odd,my_list)

# print(x)
# print(list(x))
# print(list(y))
     


# my_list=[10,21,33,25,16]
# def even(n):
#      if (n %2 == 0) :
#         return "even"
#      else :
#          return "odd"

# # def odd(n):
# #      if (n %2 != 0) :
# #         return odd

# x=list(map(even,my_list))  
# print(x)   






# my_list=[10,21,33,25,16]   # else part htne se None values return krta hai jitni value leta hai utni value hai return krega 
# def even(n):
#      if (n %2 == 0) :
#         return "even"
    
# x=list(map(even,my_list))  
# print(x)   


  #=================filter =============


# my_list=[12,34,35,54,45,25,36]   # even number
# print(my_list)

# def even(n):
#     if n%2 == 0:
#         return True
# x=list(filter(even,my_list))
# print("even number:",x)


# my_list=[12,34,35,54,45,25,36]   # even number
# print(my_list)

# def odd(n):
#     if n%2 != 0:
#         return True
# x=list(filter(odd,my_list))
# print("odd number:",x)


# my_list=[1,0,35,54,45,25,36]   # prime number
# print(my_list)

# def prime(n):
#       if n%2==0:
#         return True
# x=list(filter(prime,my_list))
# print(x)



# ==============================lambda function ===> asa function jiska koinamm ni  h isko ek baar use krte hai



# x=lambda name:print("hello i am :", name)
# x("Summitttt")


# m=input("enter name :")
# x(m)

# # y=lambda x,y:x*y
# # print(y(10,20))



# y=lambda x,y:x*y
# p=int(input("enter name :"))
# q=int(input("enter name :"))
# print(y(q,p))





# my_list=[2,3,4,5,10]     # opreter
# x=list(map(lambda x : x**2 ,my_list))
# print(x)

# my_list=[2,3,4,5,10]    # even nymber 
# x=list(filter(lambda x : x%2==0 ,my_list))
# print(x)

# my_list=[2,3,4,5,10]    # odd nymber 
# x=list(filter(lambda x : x%2!=0 ,my_list))
# print(x)



# #  reduce()---->  ek value ko print krega 
# from functools import reduce      # reduce import krna pdta hai iske bina code excute ni hoga 

# my_list=[115,223,35,4,52,366,167]
# def max (x,y):
#     if x>y:
#         return x
#     else :
#         return y
# x=reduce(max,my_list)
# print("max:",x)




# my_list=[115,223,35,4,52,366,167]
# def min (x,y):
#     if x<y:
#         return x
#     else :
#         return y
# x=reduce(min,my_list)
# print("min:",x)





# my_list=[115,223,35,4,52,366,167]
# def sum (x,y):
#         return  x+y
# def sub (x,y):
#      return x*y

# x=reduce(sum,my_list)
# y=reduce(sub,my_list)
# print(x,y)
    



# my_list=[1,4,23,34,25,6,8,58,86]
# print(my_list)
# new_list=[]
# for i in my_list:
#     sum=i+5
#     new_list.append(sum)
# print(new_list)



# from functools import reduce

# my_list=[1,4,23,34,25,6,8,58,86]
# def min(x,y):
#     if x>y:
#         return x
#     else :
#         return y
# x=reduce(min,my_list)
# print(x)


# x=lambda name : print(name)
# x("ankittt")

# my_list=[1,4,23,34,25,6,8,58,86]
# def min(x,y):
#     if x<y:
#         return x
    
#     else:
#         return y
# x=reduce(min,my_list)
# print(x)



# n=int(input("enter a number:"))

# def fac(n):
#     if (n==1 or n==0):
#         return  n
# x=list(map(fac,n))
# print(x)



# def fac(n):
#     if n==0:
#         return 1
#     else :
#         return n * fac(n-1)
# # m=float(input("enter a num:"))
# y=fac(5)
# print(y)








#======-----------000000


# def suq(num):
#     for i in range(1,num+1):
#         print(i*i)

# suq(10)





# def sqr(num):     # output 1 
#     for i in range(1,num+1):
#         return i

# data=sqr(10)
# print(data)

 
  # genrater  function bna deta hai -> 

# def sqr(num):   
#     for i in range(1,num+1):
#         yield i*i

# data=sqr(10)
# for i in data:
#     print(i)




# def sqr(num):   
#     for i in range(1,num+1):
#         yield i

# data=sqr(10)
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))

# for i in data:
#     print(i*i)



# def sqr(num):   
#     for i in range(1,num+1):
#         yield i

# data=sqr(10)
# for i in data:
#     print(i+5)

    
# print(data)
# data=sqr(10)
# for i in data:
#     print(i*i)

# data=sqr(10)
# for i in data:
#     print(i-2)


# data=sqr(10)
# for i in data:
#     print(i+32)




#-----------

# def sqr(num):
#     for i in range(1, num + 1):
#         yield i

# data_list = list(sqr(10))

# for i in data_list[1:3]:
#         print(i + 5)

# for i in data_list[3:6]:
#         print(i * i)


# for i in data_list:
#     print(i - 2)


# #---------


# def sqr(num):
#     for i in range(1, num + 1):
#         yield i

# data = sqr(10)
# for i in data:
#     if i in range(1,4):
#         print(i + 50)

# data = sqr(10)

# for i in data:
#     if i in range(3,6):
#         print(i-2 )


# data = sqr(10)

# for i in data:
#     if i in range(6,8):
#         print(i * 100)


# data = sqr(10)

# for i in data:
#     if i in range(8,11):
#         print(i ** 2)



# #==============================


# for i in range(1,21):
#     if i%2==0:
#         print(i)


# def sqr(num):
#     for i in range(2,num,2):
#         print(i) 
# data = sqr(10)



# def sqr(num):
#     for i in range(2,num,6):
#         print(i)
# data = sqr(24)


# def sqr(num):
#     for i in range(1, num + 1):
#         yield i

# data=sqr(10)
# print(next(data))

# for i in data:
#     if i<=4:
#         print(i*5)
   
#     elif 4<=  i <=6:
#         print(i*i)
    
#     elif 6<= i <=8:
#         print(i-1)

#     elif 8<= i <=10:
#         print(i*50)
#     else:
#         print(i)



