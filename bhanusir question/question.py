# WAP  1))) mx value ka data 

# name=["ankit","sumit", "aayush","pankaj" ,"om"]
# addres=["bhopa","sainkheda","mp nagar","rewa" , "ujjain"]
# st_marks=[56,14,36,56,24]

# M=max(st_marks)
# print(M)

# C=st_marks.count(M)
# print(C)

# # i=st_marks.index(56,0)
# # print(i)

# # i=st_marks.index(56,i+1)
# # print(i)
# index=-1
# for i in range(C):
#     index=st_marks.index(M,index+1)
#     print("student name" , name[index])
#     print("student adrss" , addres[index])
#     print("student name" , st_marks[index])



# varss=-1
# for i in range (C):
#     varss=st_marks.index(M,varss+1)
#     print(varss)



#WAP to create folling list at number and placed  them all in single list

# record=int(input("how many ^"))
# st_detail=[[],[],[]]

# for i in range(record):
#     name=input("enter name ")
#     address=input("enter address")
#     marks=int(input("enter marks"))
#     st_detail[0].append(name)
#     st_detail[1].append(address)
#     st_detail[2].append(marks)
# print(st_detail)






#dict

# dict = {123:["ankit",7024911772],
#         456:["sumit",7806158132],
#         789:["om",6382824635]
#         }
# dict[123]=7637864988365
# print(dict)
# dict[111]=["ankuuu",8326058665]
# print(dict)
# dict.update({267:["qwe",1863846868]})
# print(dict)
# # dict.clear()
# print(dict.key())
# # print(dict)




# records={}
# n=int(input("how many re....."))

# for i in range(n):
#     adhar=int(input("enter adhar"))
#     name=input("enter name")
#     mob=int(input("entwr mobile"))
#     age=int(input("enter age"))
#     city=input("enter city")
#     d={"name":name , "mobile":mob , "age":age , "city":city}
#     records[adhar]=d
#     print(records)

# records={}
# n=int(input("how many re....."))
# for i in range(n):
#     adhar=int(input("enter adhar"))
#     name=input("enter name")
#     mob=int(input("entwr mobile"))
#     age=int(input("enter age"))
#     city=input("enter city")
#     address=input("enter addresss")
#     d=records.update({"addres":address})
#     records[adhar]=d
    


# x=(10,20,230,40,60)
# print(type(x),x)
# y=bytes(x)
# print(type(y))

# m=(10,20,230,40,60)
# for i in m(0,(m+1)):
#     print(m*2)


# import sys , keyword
# val1=int(input("enter val1: "))
# val2=float(input("enter val2: "))
# su=val1+val2
# print(su)
# print(type(val2))
# print(sys.getsizeof(val1))
# print(keyword.kwlist)



# a=2
# b=4.4
# sum=a+b
# print(sum)

# a=int ("33")
# b=2.3
# print(a+b)
# print(type(b))

# a=2
# b=int("23")
# print(a+b)

# line1=" hye i am ankit patel thnakyou HH for me this oppetunity i have a compelet BCA in career college in bhopal "
# line2="i am from sainkheda but cureenty line in indore. i am resentaly pusuing full stack pyhton developer"
# add=line1+line2
# # print(add)
# # print(type(add))
# # print(len(add))
# # print(add[-12:-2])
# print(add[0:44:6])
# print(add[-11:-1:2])
# print(add[-1:-9:-1])
# print(add[5:1:-1])
# print(id(add))


# line="To check how many objects/characters present in string"
# # out=line.str()
# print(str(line))
# # print(line[5])
# line[1]="w"
# print(line)

# list=[20,20,294,493,484,39,39]
# x=0
# for i in list:
#     print('list[{}]='.format(x),i)
#     x+=1

# list=[20,20,294,493,484,39,39]
# new=[1,2,3,4,5,6]
# # list[0]=23
# # print(list)
# # list.append('83481')
# print(list)
# countt=list.count(20)
# print(countt)
# list.extend(new)
# print(list)
# # list.insert(1,"10000")
# print(list)
# list.pop()
# print(list)
# list.remove(20)
# print(list)
# # list.reverse()
# print(list)
# list.sort(reverse=True)
# print(list)

# list[0]=57
# print(list)
# print(sum(list))
# print(set(list))
# print(min(list))
# print(max(list))
# print(len(list))
# print(type(list))
# print(id(list))
# # print(list(tuple))
# print(tuple(list))
# print(str(list))


# lis=["hindi"]
# tuple=("english","sanskrit")
# set={"marthi"}
# lis.extend(tuple)
# lis.extend(set)
# print(lis)
# print(type(lis))

# clt=(10,10,202,29,30,93,202,930, 202,92,202,92192,991)
# print(type(clt))
# # new=list(clt)
# # print(list(clt))
# # print(type(clt))
# new=clt.count(10)
# print("count of 10:",new)
# print(clt.index(10,1,9))
# print(clt.index(202,4,9))

# d={}
# d[1]="ankit"
# d[2]=33
# d[3]="indore"
# print(d)


# d={1: 'ankit', 
# 2: 33,
#  3: 'indore'}
# print(d.keys())
# print(d.items())
# print(d.values())
# # print(d[3])

# print(d.keys())
# print(d.values())
# print(d.items())
# print(d[2])
# d[4]="ankittt"    #update element dictionary
# print(d)

# d[4]="patel"
# print(len(d))
# # print(d.keys())
# print(d.get(1))
# print(d[1])
# print(d.keys())
# print(d.items())
# print(d.values())
# del d[2]
# d.clear()
# d.pop(4) 
# d.popitem()
# del d[2]
# print(d)
# del d[4]
# d.clear()
# 
# for k, i in d.items():
# #     print(k,"---",i)


# list=[10,12,123,32,1,3]
# newcopy=list.copy()
# newcopy.append(12)
# print(newcopy)
# print(list)

# dict = {1: 'ankit', 2: 33, 3: 'indore'}
# newcopy=dict.copy()
# newcopy[6]="anittttt"
# print(newcopy)
# print(dict)

# student ={

#    "details":{ "name":"ankit",
#     "city":"indore"
#     },
#     "score":{
#         "math":90,
#         "phy":93,
#         "chm":89    
#     }
# }
# student["clg"]="career bhopal"
# student["score"]["english"]=98
# # student["score"].pop('math')
# del student["details"]["name"]
# print(student["details"].keys())
# print(student["details"].values())
# print(student["details"].items())
# print(student["details"].clear())



# print(student)
# print(student["score"]["math"])
# # print(student)


# s={10,20,10,20,102,38,29,"ankittt",True}
# s1=[11,12,123,13]
# s2=(1111,2222,333,444)
# print(s)
# print(len(s))
# print(type(s))
# s.add(343)
# s.update(s1)
# s.update(s2, range(100))
# print(s)


# s=set(range(10))
# print(s)

# m=set()
# print(type(m))
# s={10,20,10,20,102,38,29}
# s1=s.copy()
# print(s1)
# print(sum(s1))
# print(s.pop())
# s1.remove(38)
# s.discard(102)
# s.clear()
# print(s)
# print(s1)

# s1={10,20,30,40,50}
# s2={40,50,60,70,50, 100,84,93}
# x=s1.union(s2)
# print("union:", x)

# s1={10,20,30,40,50,100,84}
# s2={40,50,60,70,50, 100,84,93}
# y=s1.intersection(s2)
# print("intersection:",y)
# print(x&y)
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year %100==0):
#     print("It's a leap year.")
# else:
#     print("It's not a leap year.")

# num = float(input('Enter a number: '))
# num_sqrt = num ** 3
# print('The square root of Num :', num_sqrt)

# for i in range(10):
#     if i%2!=0:
#         print("even",i)
#     else:
#         print("odd",i)

for i in range(9,100):
    if i%9==0:
        print(i)
    else:
        pass
        
