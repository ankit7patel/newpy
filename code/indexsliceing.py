# ------------------------------------ # --value--> memory location 
# import keyword
# x=20
# print(keyword) # keyword list 
# y=30
# total=x+y
# print(id(total))

#  # --value--> memory location 
 
#  # ----------------------------------------------------------------x -- ide..

# num=10
# For=100
# NUM=20
# num_num2=20
# totalSum=num+NUM+num_num2+For
# age=5
# print(age,totalSum)


# x,y,z=20,50,30
# print(x,y,z)

# x=y=z=100
# print(x*x+y*y+z*z)
 #--------------------------------------------------  type casting 
"""age=22  
age_str=str(age)
txt="name ankit , age :" +age_str
print(txt)



age="22"
txt="ankit ,age :" +age
print(txt)

multiline comm """

"""
name ="ankittt"
age = "22"
txt=name+age
print(txt)
"""

# --------------------------------------------------------------------datatype -------->


# PYTHON --- const vari 

# x=10
# x=50  #overwrite last value in run time 
# y=20
# x1=12.1
# y1=25.1
# str='class'
# str2="class2"
# str3="""str_class
#           second
#             last    """
# m=3+4j
# print(type(m))
# print(m)
# print(x) # overwrite last value in run time 
# print(x)
# print(type(x))

# print(type(y))
# print(type(x1))
# print(type(y1))
# print(type(str))
# print(type(str2))
# print(type(str3))
# print(str3)
# print(id(x)) #addrsss..


# tuple=(10,20,30,'anku')   # immutable  slicing allowing
# print(type(tuple),tuple)

# list=[50,30,20,50,'python'] 
# list[3]=1000
# print(type(list),list)

# my_dict={"class":"p17" ,
#           "add":"bpl"}
# print(my_dict["class"],)
# print(my_dict["add"])

# set={10,88,99,88,555,555}
# print(set)


# n=int(input("enter a no"))
# i=1
# while i<=10:
#     print(i*n)
# #     i += 1


# n=int(input("enter a no"))
# for i in  range(n):
#     for i in range (1 ,11):
#     print(i)

# n=int(input("enter a no"))
# for i in range(1 ,11):
#     print(n*i)

# for i in range(1 ,11):
#     print(i)

# i = 0
# while i<10:
#     print('hello')
#     i +=1

# i = 0
# while i < 100:
#     print("hello")
#     i += 1

# for i in range (100):
#     print("pyhton")
#     if(i == 10):
#         break
# print(i)


# #   -----------------------------------------------------indexing & sliceing-----


# list=[10,12,30,40,50,29,93,40,50,10]  # index find 
# print(len(list))
# print(list.index(40)) # find single value
# print(list.index(50,5,))  # (element,start ,end)

# str="cybromcybrom2"    #(el ,start ,end)
# print(str.index("b"))
# # print(str.index("c", 2))
# print("index_no:", str.index("c" , 2))

# my_list=[10,20,20,30,40,50,50,"python"]
# print(my_list.index(40))
# print(my_list.index(20))
# print(my_list.index("python"))
# print("index:" ,my_list.index(10))
# print(my_list.index(40 ,2))

# # print("index_no:", str.index("c" , 2))




#  ----- sub string
""" { +ve direc (endpoint -1)
-ve direc (endpoint +1)}"""

# var="hellofiends"
# print(var[-6:-1])
# print(var[-1:-7:-1])
# print(var[-8:-1])
# print(var[-6:-9:-3])
# print(var[7:-1:1])




# li = [1,2,3,4,5,6,7,8,9]
# print(len(li))
# print(li[:3:-1])
# print(li[-5:-2])




# name =input("enter your name ")
# age =input("enter your age ")


# print("my name is :" , name)
# print("my age is :" , age )

# x=80
# print(bin(x)) 

# x ="ankitt"
# print(int(x))

# x=22
# print(str(x))

# x = (10,20,30,40,50)
# print(list(x))
# print(set(x))
# print(type(list(x)))
# print(type(set(x)))

# x1 = {10,20,"python",20,60,100}
# print(tuple(x1))
# print(set(x1))
# print(list(x1))
# print(type(list(x1)))
# print(type(tuple(x1)))



# y=(11,3,3,34,524,125,21,84,14,141,67,53,13,18)
# print(list(y))
# print(y[2:7:2])
# print(y[::-1]) 

# print(y[6:13])



# ------> string <-------



# str1="python"
# s=str1
# print(type(s))


# str='goodbyee'  # charactor chnge ni kr skte   
# print(str)
# print(type(str))

# print(str.index('g'))  #str ki index pta krte h
# print(len(str))
# print(str[2:6:])
  

# str1="python"
# str2="django"
# str=(str1+str2)
# print(str)


# str="mm2"
# print(str*2)


#<----------------------------string methods------------------<

# m = "Ankittt"     #function (value)
# print(len(m))
# print(max(m))
# print(min(m))
# # print(chr(m))

# m = "hye i am ankit"
# print(ord(m[0]))
# print(m.split(" "))
# x=ord('m')
# print(x)


# str = "hye i aM ankit"  # methods --> obj.metods()
# print(str.upper())
# print(str.lower())
# print(str.capitalize())
# print(str.swapcase())
# print(str.title())
# print(str.center(80,'*'))
# new_str=str.center(40)
# print(new_str)
# c_str=str.count('a') # ('a',start el ,end elm)
# print(c_str)

# str1=['python','django','javascript','github']
# print(' '.join(str1))
# print('//'.join(str1))

# list=['10','20','30','50','52']
# separator=','
# print(separator.join(list))

# my_tuple=('10','20','30','50','52')
# separator=','
# print(separator.join(my_tuple))


# my_list="python django javascript github"
# print(my_list.split(" "))
# print(my_list.split(" ",2))
# print(my_list.split("  ",1))
# print(my_list.split(",", 0))
# print(my_list.split(",",4))









