
######## Decorator 
##   1)  type 

def deco(x):
    def wrapper():
        print("start")
        x()
        print("end")
    return wrapper

def original_fun():
    print("this is original function")


var = deco(original_fun)
var()

##  2) type
def decorator(x):
    def wrapper():
        print("start")
        x()
        print("end")
    return wrapper

@decorator
def original_fun():
    print("this is original function")


original_fun()