 ################################ <<< SINGLE  LEVEL INHE=================================>>>>>

####    1)============>>
class A:
    name="ankit"

    def m1(self):
        return "this is m1 method"
    
class B(A):
    age=33
    def m2(self):
        print("name=",A.name)   # clss me acces   ( print("name=",self.name))  --> self acces  ## static vriable ko hm method ke ande -->  Class name ,self , obj  kisi se bhi acces kr skte hai
        print("m1=",self.m1())
        
class C(B):
    def m3(self):
        print("age==", obj.age)     ## local  vriable ko hm method ke ande -->  Class name ,self , obj  kisi se bhi acces kr skte hai
        self.m2()
        
obj=C()
obj.m3()
# print("wyuehfu",B.age)     ###local veriable ko class ke bahr class name, obj se acces krte hai

 ######   2)---------------------------> 
# class sbi:
#     Head_name ="RBI BANK"

#     def detail(self,name,account,ifsc):
#         global Bank_name       # local varibale ko

#         Bank_name="SBI"
#         self.name=name
#         self.account=account
#         self.ifsc=ifsc
#         print(Bank_name)

# class punjab(sbi):

#     def m(self):

#         self.detail("ankit", 7135071 ,"sbiif0999")   # Setting the details using the inherited detail method  (sbi ki metthod ko cll kiya )

#         print("this is a punjab bank ")
#         print("head bank=",obj.Head_name)
#         print("user name=", obj.name)
#         print("user account=",obj.account)
#         print("user ifsc=",self.ifsc)
#         print(Bank_name)

# obj=punjab()
# obj.m()



#__________________________________________MULTI LEVEL INHER --------------------------->>>>>>>>>>>>>>>>>>>..
####    1)

class sbi:
    Head_name ="RBI BANK"

    def detail(self,name,account,ifsc):
        global Bank_name      
        Bank_name="SBI"

        self.name=name
        self.account=account
        self.ifsc=ifsc
        print(Bank_name)

class punjab(sbi):

    def m(self):

        self.total_amount= "927139"   ##self se diclear krna pdta hai

        self.detail("ankit", 7135071 ,"sbiif0999")   # Setting the details using the inherited detail method

        print("this is a punjab bank ")
        print("head bank=",obj.Head_name)
        print("user name=", obj.name)
        print("user account=",obj.account)
        print("user ifsc=",self.ifsc)
        print(Bank_name)

class dcb(punjab):

    def user(self):
        self.m()   #    -----> pub ke method ko cll kiya  hai
        print("total amount=", self.total_amount)
        

obj=dcb()
obj.user()

###########     2)

class sbi:
    Head_name ="RBI BANK"
    def detail(self,name,account,ifsc):
        global Bank_name

        Bank_name="SBI"

        self.name=name
        self.account=account
        self.ifsc=ifsc
        print(Bank_name)

class punjab(sbi):

    def m(self,age):
        self.age=age

        self.total_amount= "927139"                                                  ##self se diclear krna pdta hai

class dcb(punjab):

    def user(self, year):
        self.year=year
        print(self.age)
        print("total amount=", self.total_amount)

        self.detail("ankit", 7135071 ,"sbiif0999")                                 # Setting the details using the inherited detail method

        print("this is a punjab bank ")
        print("head bank=",obj.Head_name)
        print("user name=", obj.name)
        print("user account=",obj.account)
        print("user ifsc=",self.ifsc)
        print(Bank_name)


class airtl(dcb):
    def last(self):
        self.m(90)
        self.user(22)
        print("year of this bank:",self.year)
        

        

obj=airtl()
obj.last()









################==================================___MULTIPALLEVEL INHER====================================================<<<<<<<<<<<<<<<<<<<,


############ 1)------------<


class ankit:

    def room1(self):
        print("enter a room ")

class ad:
    def room2(self):
        print("enter a room ad ")

class key(ad,ankit):   ##(MRO)--> LEFT to right value leta hai 
    def lock(self):
        self.room1()
        self.room2()

        super() #### dono method ko cl krega     

obj=key()
obj.lock()

################## 2)--------------> 



class ankit:

    def room(self):
        print("enter a room ")

class ad:
    def room(self):
        print("enter a room ad ")

class key(ad,ankit):   ##(MRO)--> LEFT to right value leta hai 
    def lock(self):
        self.room()
        super().room()   #### dono method ko cl krega 

    

obj=key()
obj.lock()


###############    3)--------------->>>>>>>>>>>> 


class ankit:

    def room1(self):
        print("enter a room ")

class ad:
    def room1(self):
        print("enter a room ad ankuuu ") 

    def room2(self):
        print("enter a room ad ")

class key(ankit,ad):   ##(MRO)--> LEFT to right value leta hai 
    def lock(self):
        ankit.room1(self)
        ad.room1(self)                            # explicitly calls the room1 method from both 
        ad.room2(self)


    

obj=key()
obj.lock()





############################################# -----multipal----- ##########################################################################
#   ### multipal 




# class p1:
#     def m1(self):
#         print("p1 acces ")
# class p2:
#     def m1(self):
#         print("p2 acces ")

# class child(p2,p1):    ##def first or left to right (MRO)
#     def m2(self):  
#         self.m1()   
# obj=child()
# obj.m2()

  ### multipal 




# class p1:
#     def m1(self):
#         print("p1 acces ")
# class p2:


    
#     def m2(self):
#         print("p2 acces ")

# class child(p2,p1):    ##def first or left to right (MRO)
#     def m3(self):  
#         self.m1()   
#         self.m2()
# obj=child()
# obj.m3()





# multipal 


# class p1:
#     def m1(self):
#         print("p1 acces ")
# class p2:

#     def m1(self):
#         print("p1 m2 acces ")

    
#     def m2(self):
#         print("p2 acces ")

# class child(p2,p1):    ##def first or left to right (MRO)
#     def m3(self):  
#         self.m1()   
#         self.m2()
# obj=child()
# obj.m3()


############# queestion  super () methods hai ---------------------->




# class A:
#     def m1(self):
#         print("m1 called from A")


# class B(A):
#     def m1(self):
#         print("m1 called from B")
#         # super().m1()    ### jab hme A ki m1 ko cll krna ho tb super() mwthod ka use kkregeeee

# obj=B()
# obj.m1()






#############_________________________pract....--------------------------->

# class A:
#     name="ankit"

#     def m1(self):
#         return "this is m1 method"
    
# class B(A):
#     age =22
#     add="bhopalllll"
#     def m2(self):
#         add="bhopal"
#         print("name=",A.name)   # clss ame acces   ( print("name=",self.name))  --> self acces 
#         print("m1=",self.m1())
#         print(B.add)
#         print(add)
        
# class C(B):
#     def m3(self):
#         print("age",self.age)
#         self.m2()
        
        
# obj=C()
# obj.m3()
# print("age",B.age)




# class A:
#     name="ankit"
#     cours="full stack"

#     def m1(self):
#        global add
#        add="bhopal"    ### bahr acce krne ke liye global krna pdt Hai 
       
#        print("this is m1 method")
#        print(A.name)       ## static vriable ko hm method ke ande -->  Class name ,self , obj  kisi se bhi acces kr skte hai
#        print(self.name)
#        print(obj.name)
#        print(add)
#        print(A.cours)
       
# obj=A()
# obj.m1()
# print(A.name)
# print(obj.name)
# print(add)
# # print(self.name)  ### sttaic variable ko hm self se obj me cll ni kr skte 

    



