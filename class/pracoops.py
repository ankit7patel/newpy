# ### 1)---

# class sbi:

#     Head_name ="RBI BANK"

#     def detail(self,name,account,ifsc):
#         global Bank_name      
#         Bank_name="SBI"

#         self.name=name
#         self.account=account
#         self.ifsc=ifsc
#         print(Bank_name)

# class punjab(sbi):

#     def m(self):

#         self.total_amount= "927139"                                                  ##self se diclear krna pdta hai

# class dcb(punjab):

#     def user(self, year):
#         self.year=year
#         print("total amount=", self.total_amount)

#         self.detail("ankit", 7135071 ,"sbiif0999")                                 # Setting the details using the inherited detail method

#         print("this is a punjab bank ")
#         print("head bank=",sbi.Head_name)
#         print("user name=", obj.name)
#         print("user account=",obj.account)
#         print("user ifsc=",self.ifsc)
#         print(Bank_name)


# class airtl(dcb):
#     def last(self):
#         self.m()
#         self.user(22)
#         print("year of this bank:",self.year)
        
# obj=airtl()
# obj.last()



# ####  2)------

# # class ankit:

# #     def room1(self):
# #         print("enter a room ")

# # class ad:
# #     def room1(self):
# #         print("enter a room ad ankuuu ") 

# #     def room2(self):print("this is base"
# #         print("enter a room ad ")

# # class key(ankit,ad):   ##(MRO)--> LEFT to right value leta hai 
# #     def lock(self):
#         # ankit.room1(self)
#         # ad.room1(self)                            # explicitly calls the room1 method from both 
#         # ad.room2(self)
       
        


    

# # obj=key()
# # obj.lock()



#  #### 3)------


# class A:
#     def m2(self):
#          return "m1 called from A"


# class B(A):
#     def m1(self):
#         print("m1 called from B")
#         # print(self.m2())
        


#         # super().m1()    ### jab hme A ki m1 ko  krna ho tb super() mwthod ka use kkregeeee

# obj=B()
# obj.m1()





# ###  4)-----

# # class Student:
# #    name="ankuuuu"
# #    def __init__(self):
# #        self.a=10
# #        self.b=20
# #    def display(self):
# #        print(self.a)
# #        print(s.b)
# # s= Student()
# # s.display()
# # print(s.a)
# # print(s.name)



# # # 1.  Instance variable declare through constructor…………………


# # class Student:
# #     ''' This class is develop by Neeraj for demo'''


# #     def __init__(self,name,roll,marks,city):
# #         self.name=name
# #         self.roll=roll
# #         self.marks = marks
# #         self.city = city
# #     def display(self):
# #         print("my name is", self.name)
# #         print("my roll no is", self.roll)
# #         print("my marks is", self.marks)
# #         print("my city is", self.city)
# # stu1 = Student("Neeraj",101,"90","Bhopal")
# # stu2 = Student("Rahul",102,"92","Indore")
# # print(stu1.name)
# # print(stu2.name)
# # stu1.display()
# # stu2.display()
# # print(stu1.__dict__)
# # print(stu2.__dict__)


# # class Student:

# #     college="Career college Bhopal" # static      #  acces class name ,object name 
# #     new="MCA"

# #     def __init__(self,name,rollno,marks,city):
# #         cours="BCA"   #local                            ### varivale name inside ## out  side global krna pdta hai 
# #         self.name=name  # instace      #### self ,obj se acces krte hai 
# #         self.rollno=rollno 
# #         self.marks=marks
# #         self.city=city
# #         print(cours)             # local ko acces krne ke lite variable name bs 
# #         print("college name & univ-:",Student.college)
# #         print(Student.new)                      ### varivale name inside ## out  side global krna pdta hai 

# #     def show(self,fees,):
# #         self.fees=fees
# #         print("name:",self.name)
# #         print("rollnu:",obj.rollno)
# #         print("cgp:",self.marks)
# #         print("city:",self.city)
# #         print("total fees:",obj.fees)
        
# #         print(newcours)
# #         print("local_address:", localaddres)    ## print("local_address:", self.localaddres)
# #         print(self.vari)    # ## self or kwlobj se acces krege 

# # obj=Student("ankit", 1638,9.2,"indore")
# # localaddres="kalpana nagar bhopal"  
# # newcours="MCA"                                    # global or local ko acces krne ke variable name likkhte hai 
# # obj.vari="instance variable declare through object"   ### instance through object variable 
# # print(obj.vari)                            ###obj se acces krege 
# # # print("local_address:",Student.localaddres)
# # obj.show(146550)

# # # print("college name & univ-:",obj.college)
# # # print(obj.__dict__)
# # # obj2=Student("Sumit", 1639,9.5,"indore")
# # # obj.show(146550)


# # class Student:
# #     city="bhopal"
# #     cour="bca"
# #     def __init__(self,name):
        
# #         self.name=name
# #         print(self.name) 
# #         print("This is constructor")
     
        
        
# #     def m1(self,room):
# #         self.room=room
# #         print("This is instance method")
# #         print(t.city)
# #         print(t.cour)
# #         print(t.roommate)
# #         print(ptl)
# #         self.__init__(t)
        
# # t=Student("ankit")
# # t.roommate="all"
# # ptl="sumit"
# # t.m1(5/3)








# class Student:
#     quali = "M.Tech"   # static variable declare inside the class   
#     def __init__(self,name,age):
#         # global school
#         school = "SHSS"        # static variable declare inside the constructor
#         self.name = name
#         self.age = age
#         print("School = ", school)
    
#     def display(self):
#         Student.gread = "P.hd"   # static variable declare inside the instence variable
#         print("Name = ",self.name)
#         print("Age = ",self.age)
#         print("Quali =",Student.quali)  # static variable access inside the class through       
         
#         # print("School = ", school) # static variable access inside the class 
        
#         print("Gread = ",Student.gread) # static variable access inside the class 
       
#         print("Achivment = ",Student.achivment)   # static variable access inside the class through class name
        

# obj = Student("Neeraj",37)
# Student.achivment="Gate-qualified"   # static variable declare outside of the class
# print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name
# print("Access through object = ",Student.quali) # static variable access outside the class through object
# obj.display()
# print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name
# # print("Access through class_Name = ",school)# static variable access outside the class through class name
# print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# # obj.display()
# # print(dir(Student))



# class Demo:
#    def m(self):
#        Demo.a=100
#        print(Demo.a)
#    def n(self):
#        print(Demo.a) 
       
# d=Demo()
# d.m()
# d.n()


# class Book:
#     Price=1350
#     Addres="kalpana nagar Bhopal"

#     def __init__(self,name,author):
#         self.name=name
#         self.author=author

#     @classmethod
#     def update_price(cls,price,Address):
#         cls.Price=price
#         cls.Addres=Address
#     def show(self,page):
#         self.page=page
#         print("BOOK_NAME:",self.name)
#         print("BOOK AUTHOR:",self.author)
#         print("BIIK OF TOTAL PAGE:",self.page)
#         print("BOOK PRICE:",Book.Price)
#         print("latest addresss:",obj.Addres)

# obj=Book("python","guido")
# obj.update_price(1750,"INDORE")
# obj.show(134)


class Student:
    @staticmethod
    def great():
        return "Thank for visiting our site"
    @staticmethod
    def great1():
        return "Please visit again"
    
    def normal():
        return "---------!!!!!----------"

obj = Student
# access static method
print("Access through class =",Student.great())
print("Access through object =",obj.great1())

# access normal method
print("Access through class =",Student.normal())
print("Access through object =",obj.normal())


class Student:
    @staticmethod
    def great():
         print("Thank for visiting our site")
    @staticmethod
    def great1():
        return "Please visit again"
    def normal(self):
        print( "---------!!!!!----------")

    

obj=Student
obj.great()
obj.great1()

##############################  python overloding ni krta

class A:
    def new(self,a ,b):    ### overloding  class name same rhega para alg alg rhege 
        return a+b
    def new(self,x,y,z):
        return x+y+z
        
        
obj=A()
# print(obj.new(10,20))
print(obj.new(10,20,30))


class A:
     def new(self,x=0,y=0,z=0):   ##### defualt 
         return x+y+z
obj=A()
print(obj.new(10))
print(obj.new(10,20))
print(obj.new(10,20,30))




from multipledispatch import dispatch
    
class A:
    @dispatch(int ,int)                   ####### ### overloding  class name same rhega para alg alg rhege 
    def add(self,x,y):
        print(x+y)

    @dispatch(int,int,float)
    def add(self,x,y,z):
        print(x+y*z)

obj=A()
obj.add(9430,9340)
obj.add(11,41,54.7)


class A:
    def new(self,a ,b):
        print("this is base")
        

class B(A):
    def new(self,x,y):
        print("this is child")
        super().new(1,2)

obj=B()
obj.new(54,76)

    


