   # list ,tuple , range 
 #----------------->list function 
# my_list=[10,20,30,40,50]
# # my_list[0] = 500
# print(my_list)
# print(len(my_list))
# print(type(my_list))
# print(min(my_list))
# print(max(my_list))

# my_list=[10,20,30,40,50]
# x=my_list.index(30)

# my_list[x]=500
# my_list[4]=1000
# print(my_list)

# #--------------> methods
# # my_list.append(777)
# my_list.clear()
# x=[]
# print(type(x))

# x=[10,20,30,40,50,60]
# y=x
# print(y)
# x.remove(10)
# print(y)


# x=x.copy()
# print(y)
# print(id(x))
# print(id(y))

# my_list1=[99,33,44,55]
# my_list=[10,20,30,40,50]
# print(my_list.count(10))
# print(my_list)
# print(my_list)
# my_list.extend(my_list1)
# print(my_list)
# my_list1.extend(my_list)
# print(my_list1)
# my_list.insert(3,500)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.remove(500)
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)


# my_list=[10,20,30,40,50]
# my_list.count(10)
# print(my_list.count(10))


#-----------------> tuple <-------------

# my_tuple=(10,20,30,40,50,60)
# print(my_tuple.index(30))
# print(my_tuple.count(40))

# new_tuple=my_tuple.index(40)
# print(new_tuple)


# print(my_tuple[0])
# print(my_tuple[0:4]) #slicing work -----< + ,-
# print(my_tuple[1:3])
# print(my_tuple[-1]) #indexing work ----< +,-

# my_tuple=(10,20,30,40,50,60)
# print(my_tuple)
# print(len(my_tuple))
# print(max(my_tuple))
# print(min(my_tuple))
# print(sum(my_tuple))
# print(id(my_tuple))
# print(type(my_tuple))




##========tuple chnge to list and list conv.. to tuple ==============
my_tuple=(10,20,30,40,50,60)
x=list(my_tuple)
print(type(x))

x[0]=20
print(x)

y=tuple(x)
print(type(y))
print(y)
print(y.count(20))



## end tuple to list============================
my_tuple=(10,20,30,40,50,60)
x=list(my_tuple)
print(type(x))

x.append(80)
x[1]=77
print(x)

y=tuple(x)
print(y)
print(type(y))











