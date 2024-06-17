from multipledispatch import dispatch
    
class A:
    @dispatch(int ,int)                   ####### ### overloding  class name same rhega para alg alg rhege 
    def add(self,x,y):
        print(x+y)

    @dispatch(int,int,int)
    def add(self,x,y,z=0):
        print(x+y*z)

obj=A()
obj.add(9430,9340)
obj.add(11,10)