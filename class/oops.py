# # without constracter -------------> class call 


# class Student:
#     Stu_qualification="MBA"    # static variable
#     Stu_college="career college"


#     def Stu_details(name,age):                # method 
#          print("qualification=",Student.Stu_qualification)
#          print("college=",Student.Stu_college)
#          print("Stuname=",name)
#          print("Stu_age=",age)
         
    
# obj=Student
# obj.Stu_details('ankit',22)





# # with constracter ----------------> classs call----- 
# #  __init__ --> constrater hai ek iska obj bnte hi autometic cll kr lena  isme () lgna pdta hai  self pss krna pdta hai 

 ##### que 1)---------<
# class Student:
#     Stu_quelification="MBA"
#     Stu_college="MvM"

#     def __init__(self,name):
#         self.name=name
#         print("constrator")
#         print("college=",Student.Stu_college)
#         print("name=",name)
        

# obj=Student("ankuuuuu")
# print(obj)


#######que 2)------<

# class Marksh:

#     college_name = "Career College Bhopal" 

#     def __init__(self, name, marks, address):
#         self.name = name
#         self.marks = marks
#         self.address = address

#     def get_avg(self):
#         sum_marks = sum(self.marks)
#         avg_marks = sum_marks / len(self.marks)
#         # print("Hi", self.name, "your average mark is:", avg_marks)           ##isme 2 bar cll krega return kiya hai to
#         # print(self.address)     #self se address ko cll 
#         return avg_marks

#     def get_grate(self):
#         avg_marks = self.get_avg()
#         print("Hi", self.name, "your average mark is:", avg_marks) 
#         print(self.address)           #self se address ko cll
#         if avg_marks >= 90:
#             print("Grade is A+")
#         elif avg_marks >= 80:
#             print("Grade is A")
#         elif avg_marks >= 70:
#             print("Grade is B")
#         elif avg_marks >= 50:
#             print("Grade is C")
#         elif avg_marks >= 34:
#             print("Grade is D")
#         else:
#             print("Fail")

# s1 = Marksh("Ankit", [70, 86, 92, 87, 94], "Bhopal")
# # s1.get_avg()
# s1.get_grate()
# # print(s1.address)                # obj se address ko cll
# print(Marksh.college_name)















#### 3  question  )----------------<  isme hm defult const.. ke andr value pss kr rye hai 


# class Student:
#     " string doc "           ## string ko acces krne ke liye (__doc__) ka use krege 
   
#     Stu_qualification="MBA"
#     Stu_college="MBM"


#     def Stu_details(self,name,age):      ## method me peram pss kr rye hai 
#          print("qualification=",Student.Stu_qualification)
#          print("college=",Student.Stu_college)
#          print("Stuname=",name)
#          print("Stu_age=",age)
         
    
# obj=Student()          # constractor me para pss krte us tum class ke obj me argument pss kra padta hai 
# print(obj.__doc__)         # string 
# obj.Stu_details('ankit',22)      # method me param pss krte hai to obj ki method e=me pss krte hai 







 #=========================== 1) instance vari, 2)local vari ,3) static========================
 ######### ========================( 1 question )--------------> 
# instance varivable isme hm obj ki valau chnge krte hai to ye variable  ki value bhi change kr deta hai 

# class Student:
   
#    "string testing"                 ### string ko acces (__doc__) se krte 
   
#    def __init__(self,name,age):    # self can hold the refrence of current object of current class 
#       self.name=name               #instance varible 
#       self.age=age
      

#    def display(self):
#       print(self.name)
#       print(self.age)

# obj=Student("ankit",22)              # first obj of Student 
# obj.display()
# print(obj.__doc__)                    # string 
# # print(dir(obj))                       # 
# print(obj.__dict__)                  # dict me value deti hai 
# # print(obj.name)
# # print(obj.age)

# print("second obj")

# Sumit=Student("Sumit",21)          # second obj of Student 
# # Sumit.display()                  # method ke though print 
# print(Sumit.__dict__)
# print(Sumit.name)                  # obj ke though print
# print(Sumit.age)





###########=========================( 2 question )=======================> 

# ##### instance variables 
# class Mobile:
#     modal_num="note 9 pro max"      
    

#     def __init__(self,emi,color,addres):
#         self.emi=emi
#         self.color=color             # instance variable 
#         self.addres=addres
#         print(Mobile.modal_num)
#         print("constr")
        

#     def sell(self):                 
#         # print("this is a new member ")
#         print("emi=",self.emi)
#         print("color=",self.color)
#         print("address=",self.addres)
#         print("methodsee")


#     def locall(self):
#         print(self.color)

# # print("new member details" , end="\t")
# obj=Mobile("112234567","blue","ip4&6")
# obj.sell()
# obj.locall()

# print("new member details" , end="\t")
# obj1=Mobile("123212322","black","ip8&ip9")
# obj1.sell()







####################( 3 question )=======================>
# constractor ka object bnna ho tb

# how to declear variable ----------------> 3 tpyes 

# class Mobile:
#     modal_num="note 9 pro max"

    

#     def __init__(self,emi,color,addres):
#         self.emi=emi
#         self.color=color
#         self.addres=addres

#     def locall(self):
#         print(self.emi)                 
#         print(Mobile.modal_num)            # class se acces 
    


# obj=Mobile("12345678","blur","ip6")
# print(obj.emi)    # obj se acces 
# print(obj.color)
# print(obj.addres)
# print(obj.__dict__)
# obj.locall()



###########=================================== 1)mothod   ---> constractor

# class Mobile:

#     modal_num="note 9 pro max"       # static varible

#     def __init__(self,emi):          # self is a refrence variable of current obj of cureent class 
#         self.emi=emi                 # instace variable  -> ise vari jo obj badne ke sth data badal de 
#         print(id(self.emi))          # id pta krna ho tb
        
        

#     def locall(self):
#         global color                 # local ko global bnne ke liye (global variable name ) 
#         color="blue"                 # local variable
#         print("emi_num=",self.emi)
#         print("color=",color)
#         print("modal_num=",Mobile.modal_num)
#     def col(self):
#         print("local variable ",color)         # local ko acces kiya hai
    
    
# obj=Mobile("12345678")
# obj.locall()
# obj.col()








###############=========================2) moethod   -->instance ki help 




# class Student:

#     def display(self,name):         # instance 
#         self.name=name
        
    
#     def show(self):
#         print("name=",self.name)
        

# obj=Student()          
# obj.display("ankitttt")         # instance ki help se  acces 
# obj.show()



###################################### 3)  methods   --> obj ki help 

# class Student:
#     Mobile_num=6851418885186

#     def __init__(self,name,addr):
#         self.name=name            # though constractor
#         self.addr=addr
#         print(Student.Mobile_num)     #### static ko class se acces
#     def display(self,age):
#         self.age=age               # though instance method
    
        
#     def show(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("quely",self.quely)           # static variable ko print krwa rye hai 
#         print("addres=",self.addr)
#         print("college",self.college)

        
        

# obj=Student("ankitttt","bhopal")
# obj.display(22) 
# obj.quely="MCA"                   # though object methods------> static variable bnya hai obj ki help se 
# obj.college="career college of bhopal"               #### obj ki help se variable
# obj.show()
# print(obj.Mobile_num)             ####   static ko obj se acces




# ################ ===================================== How to accces instance variavle=================================---------------> 
# 2 types     --> 1) inside to class   ->   self se cll hote hai === 2) outside to object   --> obj kethough cll hota hain




# class Student:
#     quali = "M.Tech"   # static variable declare inside the class   
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.school = "SHSS"  # static variable declare inside the constructor
#     def display(self):
#         Student.gread = "P.hd"   # static variable declare inside the instence variable
#         print("Name = ",self.name)
#         print("Age = ",self.age)
#         print("Quali =",Student.quali)  # static variable access inside the class through class name
#         print("School = ",Student.school) # static variable access inside the class through class name
#         print("Gread = ",Student.gread) # static variable access inside the class through class name
#         print("Achivment = ",Student.achivment)   # static variable access inside the class through class name

# obj = Student("Neeraj",37)
# Student.achivment="Gate-qualified"   # static variable declare outside of the class
# print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name
# print("Access through object = ",obj.quali) # static variable access outside the class through object
# obj.display()
# print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name
# print("Access through class_Name = ",Student.school)# static variable access outside the class through class name
# print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# # obj.display()



#####local variable -----------  global ke sth local ho koi se bhi function me use krte hai> 

# class Student:
#     def display(self):
#         global a
#         a=10
#         print("valueof a",a)
#     def show(self):
#         print("value of a",a)
#     def new():
#         print("student se acces value of a", a)
#     def old():
#         print(a)

# obj=Student()
# obj.display()
# obj.show()
# Student.new()                                        #new function ko class ke name se bahr acces krte hai
# Student.old()




# print('local value of a ',a)                       # print krwa skte hai


# class pp:

#     a=500
#     def new ():
#         print(pp.a)          ##without const------>class se acces
# obj=pp
# pp.new()

#======================methods=========================
# #metod --------------> instance methods-------------------< 

# class Student:
#     def display(self,name,add):
#         self.name=name
#         self.add=add
#         print("name=",name)
#         print("add",add)

        
        
#     def show(self,age):
#         self.age=age
#         self.display("sumit","jbil")   #instance method   -------> display acces kr skte hai show ko cll krke 
#         print("age=",age)


# obj=Student()
# obj.display("ankitt","bhopal")
# obj.show(22)


# ##########=========classs methods------------------------->  1)  @classmethod --> decoreater   2) instance of self ,here we use cls
 

# class Book:

#     price=1000

#     def book_detail(self,name,auther):
#         self.name=name
#         self.author=auther

#     @classmethod            # decoreter @ 
#     def update_price(cls,price):  
#         cls.price=price

#     def show_detail(self,page):
#         self.page=page
#         print("Bookname=",self.name)
#         print("bookauthor=",self.author)
#         print("boksprice=",Book.price)
#         print("chnge this page_num=",page)


# obj=Book()
# obj.book_detail("pyhton","guido")
# obj.update_price(2500)     # update ko cll krega 
# obj.show_detail(23)



########################======static method============================>>>


# class Student:
#     @staticmethod      # -> instance method  se cll kr skte hai

#     def great():
#         print("thanks for visit")
        
      
      
#     def great1():
#         print("welcomw to my webpage")
       


# obj=Student
# obj.great()
# obj.name="ankit"   #static variable define 
# Student.great()
# obj.great1 () ###() lgne pr isme error aayegi obj ke through cll ni kr skte ku ki isme self ni hai
# Student.great1()


########333================================================> inheri==>
###########--------------------> 





############################+===================  ALL variable type ============>


class Student:

    college="Career college Bhopal" # static      #  acces class name ,object name 
    new="MCA"

    def __init__(self,name,rollno,marks,city):
        cours="BCA"   #local                            ### varivale name inside ## out  side global krna pdta hai 
        self.name=name  # instace      #### self , obj se acces krte hai 
        self.rollno=rollno 
        self.marks=marks
        self.city=city
        print(cours)             # local ko acces krne ke lite variable name bs 
        print("college name & univ-:",Student.college)
        print(Student.new)                      ### varivale name inside ## out  side global krna pdta hai 

    def show(self,fees,):
        self.fees=fees
        print("name:",self.name)
        print("rollnu:",obj.rollno)
        print("cgp:",self.marks)
        print("city:",self.city)
        print("total fees:",obj.fees)
        
        print(newcours)
        print("local_address:", localaddres)    ## print("local_address:", self.localaddres)


obj=Student("ankit", 1638,9.2,"indore")
localaddres="kalpana nagar bhopal"  
newcours="MCA"                                    # global or local ko acces krne ke variable name likkhte hai 
obj.vari="instance variable declare through object"   ### instance through object variable 
print(obj.vari)                            ###obj se acces krege 
# print("local_address:",Student.localaddres)
obj.show(146550)

# print("college name & univ-:",obj.college)
# print(obj.__dict__)
# obj2=Student("Sumit", 1639,9.5,"indore")
# obj.show(146550)

