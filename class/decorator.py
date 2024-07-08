
######## Decorator 
##   1)  type 

def deco(x):
    def w():
        print("start")
        x()
        print("end")
        
    return w

def original_fun():
    
    print("this is original function")


var = deco(original_fun)
var()

# ##  2) type
# def decorator(x):
#     def wrapper():
#         print("start")
#         x()
#         print("end")
#     return wrapper

# @decorator
# def original_fun():
#     print("this is original function")


# original_fun()


def decor(x):
    def new():
        print("start code :")
        x()
        print("end code :")

    return new

def orignal():
    print("this is a all code :")

runn=decor(orignal)
runn()



def decoo(m):
    def new():
        print("--:")
        m()
        print("end deco--:")

    return new
@decoo
def orignal():
    print("pura code ___:")

orignal()