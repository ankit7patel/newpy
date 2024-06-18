
##############################  python overloding ni krta
#  1)
class A:
    def new(self,a ,b):    ### overloding  class name same rhega para alg alg rhege 
        return a*b
    def new(self,x,y,z):
        return x*y*z
    
        
obj=A()
# print(obj.new(10,20))
print(obj.new(10,20,30))

#2) 

class A:
     def new(self,x=0,y=0,z=0):   ##### defualt 
         return x*y*z
obj=A()
print(obj.new(10))
print(obj.new(10,20))
print(obj.new(10,20,30))




from multipledispatch import dispatch
  #3 )  
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



  # 4)
class A:
    def new(self,a ,b):
        print("this is base")
        

class B(A):
    def new(self,x,y):
        print("this is child")
        super().new(2,3 )

obj=B()
obj.new(54,76)

    



