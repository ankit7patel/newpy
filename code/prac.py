n= int(input("num"))
i=1
sum=0
while i<=n:
    if i<n:
          print(i,end="+")
    else :
         print(i,end="=")
    sum=sum+i
    i+=1
print(sum)


# n= int(input("num"))
# i=1
# sum=0
# while i<=n:
#     if i%2!=0:
#          if i<n:
#              print(i,end="+")
#          else :
#              print(i,end="=")
#     sum=sum+i
#     i+=1
# print(sum)



# n= int(input("num"))
# i=1
# # sum=0
# while i<=n:
#     if i%2!=0:
#          if i<(n-1):
#              print(i,end="+")
#          else :
#              print(i,end=" ")
#     # sum=sum+i
#     i+=1
# # print(sum)

# n= int(input("num"))
# for i in range (1,(n+1)):
#     if i<n:
#         print(i , end=(","))
#     else:
#         print(i)
         
# n= int(input("num"))
# sum=0
# for i in range (1,(n+1)):
#     if i<n:
#         print(i , end=("+"))
#     else:
#         print(i ,end="=")
#     sum=sum+i
# print(sum)
         
# n= int(input("num"))
# sum=0
# for i in range (2,(n+1)):
#     if i%2 ==0:
#         if i<(n-1):
#             print(i , end=("+"))
#         else:
#             print(i ,end="=")
#         sum=sum+i
# print(sum)

# n= int(input("num"))
# sum=0
# for i in range (1,n):
#     if i%2 !=0:
#         if i<(n-2):
#             print(i , end=("+"))
#         else:
#             print(i ,end="=")
#         sum=sum+i
# print(sum)



# n= int(input("num"))
# sum=0
# for i in range (1,n,2):
#     if i<(n-1):
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     sum=sum+i
# print(sum)



# n= int(input("num"))
# sum=0
# for i in range (2,n,2):
#     if i<(n-2):
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     sum=sum+i
# print(sum)


# n=int(input("Enter any Netural No:"))
# i=1
# sum=0
# while(i<=n):
#  sum=sum+i
#  i=i+1
#  print("",sum)

# n=int(input("Enter any Netural No2:"))
# sum=0
# for i in range(1,n):
#     if i<n:
#         # print(i)
#         sum=sum+i
#         print(sum,end=" ")
#     print(i)


# n=int(input("Enter any Netural No2:"))
# a,b,c,i=0,1,0,1
# print(a)
# print(b)
# while i<=n:
#     c=a+b
#     a=b
#     b=c
#     i+=1
#     print(c)



# list = [1, 2, 3, 4, 5, 6, 3, 8, 9, 3]
# # element = 3
# print(list.index(3,3))


# var = "I love python"
# # print(len(var))
# print(var[-1:-11:-1])

# # print(var[-6:])
# print(var[-4:-2])


# var = "WELCOME TO MY BLOG"
# print(var[3:18]) 
# print(var[2:14:2]) 
# print(var[:7]) 
# print(var[8:-1:1])
# print(var[-6:-9:-3]) 
# print(var[-9:-9:-1])


# str="123"
# x=int(str)
# print(type(x))

# str1=12.4
# y=int(str1)
# print(type(y))


# intt=256
# z=float(intt)
# print(type(z))

# list=[1,2,3,4,5,6,7,8,9]
# x=tuple(list)
# print(type(x))
# print(x)

# tuple=(1,2,3,4,5,6,7,8,9)
# y=list(tuple)
# print(type(y))
# print(y)
# m=y.append(23)
# n=y.insert(3,555)
# print(y)
# modified_tuple = tuple(y)
# print(type(modified_tuple)) 
# print(modified_tuple)

# var=100
# # list=[1,2,3,4,1,2,3,4,5,1,4,2,3,1]
# y=ord(var)
# print(type(y))
# print(y)



# char = 'A'
# ascii_value = ord(char)
# print(ascii_value)

# integer_value = 255
# hex_value = hex(integer_value)
# print(hex_value)

# oct_value = oct(integer_value)
# print(oct_value)

# ascii_value = 65
# char = chr(ascii_value)
# print(char)


# a = "Python Programming"
 
# x=a.split()
# print(x)


# d={1: 'Neeraj', 2: 'Rahul', 3: 'Ravi',4:'Jai',5:'Santosh'}
# # print(d.popitem())
# print(d.pop(2))
# print(d)

# list=[10,120,20,30]
# print(list.pop())
# print(list)



# s = {400,10,30,20}

# print(s.pop())
# print(s)


# list=[10,100,20,30]
# list[1]=1000
# print(list)
# list.append(4000)
# print(list)

# tuple=(10,20,30,40)
# print(tuple)


# my_dict = {"name":"Neeraj","age":37,"Quali":"M.tech"}
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())


# my_dict={"name":"ram","age":"23",}
# my_dict["branch"]="full stack"
# x=my_dict.values()
# x=my_dict.keys()
# x=my_dict.items()
# print(x)


# list=[10,20,30,40,50]
# my_frozenset=frozenset(list)
# print(my_frozenset)
# list.append(100)
# print(list)
# # print(my_dict)


# my_dict = {"name":"Neeraj","age":37,"Quali":"M.tech"}
# my_frozenset = frozenset(my_dict.values())
# print(my_frozenset)
# my_frozenset = frozenset(my_dict.items())
# print(my_frozenset)
# my_frozenset = frozenset(my_dict.keys())
# print(my_frozenset)
# print(type(my_frozenset))

# # my_frozenset['name']="Neeraj Patel" # TypeError: 'frozenset' object does not support item assignment
# print(my_dict)



# # bytearray()
# x=(10,20,30,255)  # TypeError: 'str' object cannot be interpreted as an integer ,  ValueError: bytes must be in range(0, 256)
# print(type(x))

# x = bytearray(x)
# print(type(x))
 
# x[1]=15
# print(x)


# list="hello i am ankit "
# print(len(list))
# print(len(list[-8:-1]))
# print(list[11:-1])



# d={1: 'Neeraj', 2: 'Rahul', 3: 'Ravi',4:'sumit',5:'satyam'}
# # print(d.items())
# # print(d.values())
# # print(d.keys())

# # del d[5]
# # print(d.pop(4))
# # d.clear()
# # d.popitem()
# # print(d.get(1))
# # print(d[2])
# # print(d.get(9,"ankti"))


# print(d)
# for i in d.keys():
#     if i<4:
#         print(i)








# s={10,20,30,50}
# t={50,60,70,80,90}
# s.add(100)
# s.update(t,range(2))
# s1=s.copy()
# s.pop()
# print(s1)
# s.remove(10)
# s.clear()

# s.discard(599)
# print(s)

# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.union(y))
# print(x&y)
# print(y&x)
# print(x.intersection(y))



# x = {"7", "b", "c"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y) 
# print(z)




# score = int(input("Enter your score: "))

# if score >= 90:
#     print("You got an A.")

# elif score >= 80:
#     print("You got a B.")
    
# elif score >= 70:
#     print("You got a C.")
       
# elif score >= 60:
#     print("You got a D.")
# else:
#     print("You got an F.")






# n=int(input("Enter the number of rows: ")) 


# for i in range(1,(n+1)):
#     print("* "*i)
# for i in range (1,(n+1)):
#     print(" "*(n-i),"*"*i)
# for i in range(1,(n+1)):
#     print("* "*i)





# st="Ankittt"
# # print(str)
# new_str=st.swapcase
# print(new_str)


# str="A,B,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,V,W,X,Y,Z"
# print(str)

# def add(x,y):
#     return x+y
# x=int(input("enter first number"))
# y=int(input("enter second number:"))

# z=add(x,y)
# print("tobal of sum:",z)





# def square(x):
#     print("The Square of",x,"is", x*x)
# def qube(y):
#     print("the qube of:",y*y*y)

# square(4)
# square(5)
# qube(3)

# print(list(range(11,1,-1)))
# print(list(range(5)))


