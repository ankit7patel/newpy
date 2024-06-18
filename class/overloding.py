from multipledispatch import dispatch
    
class A:
    @dispatch(int ,int)                   ####### ### overloding  class name same rhega para alg alg rhege 
    def add(self,x,y):
        print(x-y)

    @dispatch(int,int,int)
    def add(self,x,y,z):
        return x*y*z

obj=A()
obj.add(100,20)
obj.add(11,10,1)






















############# abstraction --------------->


class Student:
    school= "CVP"
    
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def detail(self):
        print("name:",self.__name)
        print("age:",self.__age)
        print("school:", Student.school)

class Marks(Student):
    def Show(self,math,hindi):
        self.hindi=hindi
        self.math=math
    def complete(self):
        print("name:",self.__name)
        print("age:",self.__age)
        print("school:", Student.school)
        print("hindi:",self.hindi)
        print("math:",self.math )

obj = Show("ankuu", 22)
obj.__name="Sumit patel"
obj.detail()
obj.Show(98,86)
obj.complete()
