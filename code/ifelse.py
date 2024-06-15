

# x=input("enter a no:")   # input function bydef--string return krta hai 
# print(type(x))   # <class 'str'> 


# y=int(input("enter your age:"))   #int() se typecasting krte hai  int(),float,complex() use kr skte hai
# # print(type(y)) #<class 'int'>

# n=input("enter")
# if n =="rent":
#     print("rent")
# if n ==  "bill":
#     print("bill")
# if n == "bike":
#     print("bike ")
# else:
#     print("note allow in room ")


# n=int(input("age"))
# if n>=18:
#     print("vote")
# else:
#     print("don't for vote")



# n=int(input("age"))
# if n>=16:
#     if n>=18:
#         print("for vote")
#     elif n<=18:
#         print("child")
# else:
#     print("not a vote")



# ====if -if -if ise bhi pr kr skte hai

# y=int(input("enter your age:"))
# if y>=60 :
#     print("you can vote")
#     print("wlcm to first py progm")
# if y>=18 :
#     print("second  if ")
# print("thnk u for visiting")


#=========if else ==========

# y=int(input("enter your age:"))
# if y>=18 :
#     print("you can vote")
# else :
#     print(print("you can't vote"))


#========if elif else =====

#===== pehle if lgte hai uske baad elif lgte hai bina if ke hm elif ni lga skte 


# x=int(input("enter your age:"))
# if x>=60:
#     print("counter no 1:" )
# elif x>=40:
#     print("counter no 2:")
# elif x>=20:
#     print("counter no 3:")
# else:
#     print("no counter")

# light=input("light:")
# if light == "red":
#     print("stop")
# elif light == "green":
#     print("go")
# elif light== "yello":
#     print("look")


##########################################= =========================---------##############################
# num=int(input("enter a no for table:"))
# i=1
# while i<=10:
#     print(i*num,end=",")
#     i+= 1




# num = int(input("enter table:"))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1


# n=int(input("enter a no "))
# i=1
# while i<=n:
#     print(i*i,end=",")
#     i=i+1


# n=int(input("enter a no "))
# i=1
# while i<=n:
#     if i<=n:
#         print(i,end=",")
#     else:
#         print(i)
#     i=i+1




# n=int(input("enter a no "))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i)
#     i=i+1





# n=int(input("enter no total summmmmmm "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)


#===========================================================================

# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         if i < n:  
#             print(i, end=",")
#         else:
#             print(i, end="")
#     i += 1


# n=int(input("enter a no "))
# i=1
# while i <= n:
#     if i % 2 != 0:
#         if i < (n-1):
#             print(i, end=",")
#         else:
#             print(i, end=" ")
#     i += 1






# n = int(input("Enter a number: "))
# i = 1
# sum=0
# while i <= n:
#     if i % 2 == 0:
#         if i < (n):  
#             print(i, end="+")
#         else:
#             print(i, end="=")
#         sum=sum+i
#     i += 1
# print(sum)    



# n=int(input("enter a no "))
# i=1
# sum=0
# while i <= n:
#     if i % 2 != 0:
#         if i < n:
#             print(i, end=",")
#         else:
#             print(i)
#         sum=sum+i
#     i += 1
# print(sum)



# n=int(input("enter a no of total sum  "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i < n:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     i+=1
# print(sum)

#_________________________________________________________


# n=int(input("enter a no:"))  
# i=10
# sum=0
# while i>=1:
#     if i < n :
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     sum=sum+i  
#     i-=1
# print(sum)


# n=int(input("enter a no:"))  
# i=1
# sum=0
# while i<=n:
#     print(i)
#     sum=sum+i
#     i+=1
# print(sum)




#============for loop=======

# 



# for i in range (1,11):
#     print(i)
#     print("hello")
#     print("welcome")


# ==========for loop in hr line print if else total sum ==========> 



# n=int(input("while table "))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1

    

# print("table")
# n=int(input("number of for table"))
# for i in range(1,11):
#     print(i*n)
# print("table")



# n=int(input("enter a even no :"))
# for i in range (2,n,2):
#     if i<(n-2):
#         print(i,end=",")
#     else:
#         print(i)



# n=int(input("enter a odd no:"))
# for i in range (1,n,2):
#     if i<(n-2):
#         print(i,end=",")
#     else:
#         print(i)


# n=int(input("enter a even no total sum :"))
# sum=0
# for i in range (2,n,2):
#     if i < (n-2) :
#         print(i,end="+")
#     else:
#         print(i,end="=") 
#     sum=sum+i
# print(sum)



# n=int(input("enter a odd total sum :"))
# sum=0
# for i in range (1,n,2):
#     if i < (n-2):
#         print(i,end="+")
#     else:
#         print(i,end="=") 
#     sum=sum+i
# print(sum)


# n=int(input("enter a  total sum :"))
# sum=0
# for i in range(1,(n+1)):
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     sum=sum+i
# print(sum)



#=================

# n=int(input("enter num:"))
# sum=0
# for i in range(1,(n+1)):
#     print(i)
#     sum=sum+i
# print(sum)




# n=int(input("enter a no:"))
# sum=0
# for i in range(1,(n+1)):
#     sum=sum+i
#     print(sum,end="  ")      #output enter a no:10--1  3  6  10  15  21  28  36  45  55


    

# n=int(input("enter num:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i 
#     if i<=(n):
#         # print(i,end=" ")
#         print(sum , end=" ")   #output enter a no:10--1  3  6  10  15  21  28  36  45  55
  


# x=int(input("enter a num"))
# for i in range(1,x):
#     num=i
#     length=len(str(num))
#     sum=0
#     while num>0:
#         last=num%10
#         sum=sum+last**length
#         num=num//10
#     if sum==i:
#         print (i)





# n=int(input("enter prime number :"))
# for i in range(1,(n+1)):
#     if n%i==0:
#        print(i,"prime number")
# if n%i==1:
#     print(i)
# else:
#     print(i)
    



# n=int(input("enter prime number :"))
# i=1
# count=0
# while i<=10:
#     if n%i==0:
#         count=count+1
#     i+=1
# if count<2:
#     print("prinme number:")
# else:
#     print("not a prime number:")


# n=int(input("Enter Any No."))
# a,b,c,i=0,1,0,1
# print(a)
# print(b)
# while i<=n:
#     c=a+b
#     a=b
#     b=c
#     i=i+1
#     print(c) 


# x=int(input("Enter any no : "))
# sum=0
# i=1
# while i<=x:
#     sum=sum+i
#     if i<x:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     i=i+1
# print(sum)


#print("continue")
# list=[10,20,600,60,70]
# for i in list:
#     if i>500:
#         print("no need to print this object")
#         continue
#     print(i)




# num = float(input('Enter a number: '))
# # num_sqrt = num * num
# num_sqrt = num ** 2
# print('The square root of Num :', num_sqrt)




# num = int(input('Enter a number: '))
# for i in range (1,11):
#     print(num*i)


# num = int(input('Enter a number: '))
# num_sqrt = num ** 2
# print('The square root of Num :', num_sqrt)


# x = input('Enter value of x: ')
# y = input('Enter value of y: ')

# temp=x
# x=y
# y=temp

# print(x)
# print(y)

    

    
    
# n=int(input("Enter Any No."))
# a,b,c,i=0,1,0,1
# print(a)
# print(b)
# while i<=n:
#     c=a+b
#     a=b
#     b=c
#     i=i+1
#     print(c) 



# n=int(input("Enter Anu Number"))
# i=0
# sum=0
# m=n
# count = len(str(n))
# while m>0:
#     r=m%10
#     k=r**count
#     sum=sum+k
#     m=m//10
# if(sum==n):
#     print("Number is armstrong")
# else:
#     print("Number is not armstrong")

# n=int(input("Enter Any Nomber: "))
# i=1
# count=0
# while i<=n:
#         if n%i==0:
#             count+=1
#         i+=1
# if count<2:
#     print("Number is prime")
# else:
#     print("Not Prime Number")
# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1): 
# #     print((n-i)* " ","*"*i)




# n=int(input("Enter the number of rows: ")) 
# for i in range(0,n+1): 
#     print("* "*i)
# m=n-1
# for i in range(m,0,-1): 
#     print("* "*i)


# my_tuple=(10,20,30,40,50,60,10,10)
# print(my_tuple.index(30))
# print(my_tuple.count(10))






print(list(range(11,1,-1)))     #(end-1)=== +ve direction     #(end+1)===-ve direction
print(list(range(5)))
print(list(range(-1,-11,-1)))

