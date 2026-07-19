
"""
# o(1) constant
a=10
b=20
print(a+b)

# o(1) constant
for i in range(10):
    print(i)

# o(1) constant
lst=[10,20,30,40,50,60,70,80]
for i in lst:
    print(i)

# o(n) Linear
n=int(input("num")) 
for i in range(n):
    print(i) 


# O(n²) Quadrtic
n=int(input("num")) 
for i in range(1,n+1):
    for j in range(n):
        print(i,j)
        
# o(n) Linear  = o(n*m) m=constant =o(n)
n=int(input("num"))
for i in range(1,n+1):
    for j in range(10):
        print(i,j)
        

# O(log n) logarthimc
n=int(input("num"))   # Half krte ja ra hai
while n > 1:
    n=n//2
    print(n)


#0(n) - Linear  o(n*n) = 2n -> o(n)
n=int(input("num"))

for i in range(1,n+1):
    print(i)
for i in range(1,11):
    #print(f"{n}*{i}={n*i}")
    print(n ,"*" , i ,"=", n*i )


# 0(n*m)
lst1=[1,2,3,4]
lst2=[2,3,4,5,6]
for i in lst1:
    for j in lst2:
         print(i,j)


#o(1)
lst1=[1,2,3,4]
lst2=[2,3,4,5,6]
#lst1.append(list(lst2))
lst1.extend(lst2)
print(lst1)
 


#0(n) 
n=int(input("num"))
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

a=fact(5)
print(a)

 
n=int(input("num"))
fact=1

for i in range(1,n+1):
    fact=fact*i

print(fact)




n=int(input("num"))
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i

    return fact
a=fact(n)
print(a)




n=int(input("num"))
def fact(n):
    fact = 1
    if n==0 or n==1:
        return 1
    else:
        fact = n*fact(n-1)

a=fact(n)
print(a)



num=[10,20,30,405,500,84]

x=405
for i in num:
    if i == x :  
        print("found",i) 
        


#prefex sum 
arr = [10, 20, 30, 40]

prefix = []
total = 0

prefix=[]
total=0

for num in arr:
    total = total + num
    prefix.append(total)
print(prefix)





nums = [5, 12, 50, 25, 10]

maximum = nums[0]

for num in nums :
    if num > maximum :
        maximum  =  num
print(maximum)



nums = [5, 12, 50, 25, 10]
total=0 

for i in nums:
    total+=i

print(total)



#List me kitni baar ek number aaya hai

nums = [5, 12, 5, 50, 25, 5, 10]
target=25
count=0
for num in nums:
    if num == target:
        count += 1
print(count)


#list me number search 

nums=[12,32,54,65,87,91,82,8,82,64,82]
target=822
found = False

for num in nums:
    if num == target:
        found = True
        break


if found:
    print("mil gya")

else:
    print("not")



#List me Duplicate Numbers
nums = [10, 20, 30, 20, 40, 10, 50, 30]
duplicate=[]

for num in nums:
    if nums.count(num) > 1 and num not in duplicate:
        duplicate.append(num)
print(duplicate)



#Sirf Odd Numbers ki Nayi List Banao

nums=[10,20,30,40,59,39,382,84,39,49,4,7,2,12,512,15,73,81,17,777,72,1,9,29,92,38,8]

odd=[]
for num in nums:
    if num%2!=0:
        odd.append(num)

print(odd)

#Do Lists ke Same Index ke Numbers Add Karo
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result=[]

for i in range(len(list1)):

    result.append(list1[i]+list2[i])
print(result)





nums=list(map(int,input(" enter a list :").split()))
odd=[]

for i in nums:
    if i % 2 != 0:
        odd.append(i)

print(odd)

 """



#amstrong number 

# nums = [10, 15, 22, 31, 40, 55, 61] 

# even = []
# sum=0
# for num in nums:
#     if num % 2 == 0:
#         even.append(num)
#         sum+=num

# print(even , "sum of number : ", sum , end="\n")

# num = int(input("Enter a number: "))

# temp = num
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** 3
#     temp = temp // 10

# if sum == num:
#     print(num, "is an Armstrong Number")
# else:
#     print(num, "is not an Armstrong Number")



# class Student:
#     Stu_quelification="MBA"
#     Stu_college="MvM"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("constrator")
#         print("college=",Student.Stu_college)
#         print("name=",name , "age=",age)
        

# obj=Student("ankuuuuu",24)
# print(obj)







# ### 3  question

# class Student:
#     " string doc "     
#     Stu_qualification="MBA"
#     Stu_college="MBM" 


#     def Stu_details(self,name,age):    
#          print("qualification=",Student.Stu_qualification)
#          print("college=",Student.Stu_college)
#          print("Stuname=",name)
#          print("Stu_age=",age)
         
    
# obj=Student()         
# print(obj.__doc__)        
# obj.Stu_details('ankit',22)   





# class Student:
   
#    "string testing" 
#    college="ccb" 
   
#    def __init__(self,name,age):   
#       self.name=name               
#       self.age=age
      

#    def display(self):
#       print(self.name)
#       print(self.age)


# obj=Student("ankit",22) 
# obj.name         
# obj.display()
# print(Student.college)
# print(obj.__doc__)                
# # print(dir(obj))                       
# print(obj.__dict__)                
# # print(obj.name)
# # print(obj.age)

# print("second obj")

# Sumit=Student("Sumit",21)         
# # Sumit.display()                 
# print(Sumit.__dict__)
# print(Sumit.name)                  
# print(Sumit.age)





# class Mobile:
#     modal_num="note 9 pro max"

    

#     def __init__(self,emi,color,addres):
#         self.emi=emi
#         self.color=color
#         self.addres=addres

#     def locall(self):
#         print(self.emi)                 
#         print(Mobile.modal_num)  
#         print(Mobile.color)   


# obj=Mobile("12345678","blur","ip6")
# print(obj.emi)    
# print(obj.color)
# print(obj.addres)
# print(obj.__dict__)
# # obj.locall()
# print(obj.locall)






# class Mobile:

#     modal_num="note 9 pro max"       

#     def __init__(self,emi): 
#         self.emi=emi                
#         print(id(self.emi))         
        
        

#     def locall(self,model):
#         global color                
#         color="blue"                
#         print("emi_num=",self.emi)
#         print("color=",color)
#         print("modal_num=",Mobile.modal_num)
#         self.model=model
#     def col(self):
#         print("local variable ",color)   
#         print(self.model)   
    
    
# obj=Mobile("12345678")
# obj.locall("iphone14")
# obj.col()
# # print(obj.model)





# class Student:

#     # Class Attribute (Static Variable)
#     college = "Career College Bhopal"

#     def __init__(self, name, age, course):
#         # Instance Variables
#         self.name = name
#         self.age = age
#         self.course = course

#     def display(self):
#         # Local Variable
#         message = "Student Details"

#         print(message)
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Course :", self.course)
#         print("College :", Student.college)
#         print()

#     @classmethod
#     def change_college(cls, new_college):
#         cls.college = new_college

#     @staticmethod
#     def welcome():
#         print("Welcome to Python OOP")
#         print()

# # Object Creation
# s1 = Student("Ankit", 22, "BCA")
# s2 = Student("Rahul", 21, "BSc")

# # Static Method
# Student.welcome()

# # Instance Method
# s1.display()
# s2.display()

# # Class Method
# Student.change_college("LNCT College")

# print("After Changing College")
# print()

# s1.display()
# s2.display()






# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print("Name :", self.name)
#         print("Age :", self.age)


# class Student(Person):

#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course

#     def display(self):
#         self.show()
#         print("Course :", self.course)


# # Object
# s1 = Student("Ankit", 22, "Python Full Stack")
# s1.display()



# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):

#     def sound(self):
#         print("Dog barks: Woof Woof")


# class Cat(Animal):

#     def sound(self):
#         print("Cat meows: Meow Meow")


# class Cow(Animal):

#     def sound(self):
#         print("Cow says: Moo Moo")


# class Lion(Animal):

#     def sound(self):
#         print("Lion roars: Roar Roar")


# # Polymorphism Function
# def animal_sound(animal):
#     animal.sound()


# # Object Creation
# d = Dog()
# c = Cat()
# cw = Cow()
# l = Lion()

# animals = [d, c, cw, l]

# print("Animal Sounds")
# print("----------------")

# for animal in animals:
#     animal_sound(animal)




# Calculator Project in Python  ---------- 

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero is not allowed."
#     return a / b


# while True:
#     print("\n====== CALCULATOR ======")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "5":
#         print("Thank you for using Calculator.")
#         break

#     if choice in ["1", "2", "3", "4"]:
#         try:
#             num1 = float(input("Enter First Number: "))
#             num2 = float(input("Enter Second Number: "))

#             if choice == "1":
#                 print("Result =", add(num1, num2))

#             elif choice == "2":
#                 print("Result =", subtract(num1, num2))

#             elif choice == "3":
#                 print("Result =", multiply(num1, num2))

#             elif choice == "4":
#                 print("Result =", divide(num1, num2))

#         except ValueError:
#             print("Please enter valid numbers.")

#     else:
#         print("Invalid Choice! Please select between 1 to 5.")









# -------------------------------
# Shopping Billing System
# -------------------------------

# products = {
#     1: ("Rice", 60),
#     2: ("Sugar", 45),
#     3: ("Milk", 30),
#     4: ("Bread", 40),
#     5: ("Oil", 150),
#     6: ("Soap", 35),
#     7: ("Tea", 120),
#     8: ("Coffee", 250)
# }

# cart = []

# print("=" * 40)
# print("      SHOPPING BILL SYSTEM")
# print("=" * 40)

# customer = input("Enter Customer Name: ")

# while True:

#     print("\nAvailable Products")
#     print("-" * 40)

#     for key, value in products.items():
#         print(f"{key}. {value[0]} - Rs.{value[1]}")

#     try:
#         item = int(input("\nEnter Product Number: "))

#         if item not in products:
#             print("Invalid Product!")
#             continue

#         qty = int(input("Enter Quantity: "))

#         name = products[item][0]
#         price = products[item][1]
#         total = price * qty

#         cart.append([name, price, qty, total])

#         choice = input("Add More Items? (yes/no): ").lower()

#         if choice == "no":
#             break

#     except ValueError:
#         print("Please Enter Valid Number!")

# print("\n")
# print("=" * 50)
# print("             FINAL BILL")
# print("=" * 50)

# print("Customer Name :", customer)
# print("-" * 50)
# print("{:<15}{:<10}{:<10}{:<10}".format(
#     "Product", "Price", "Qty", "Total"))
# print("-" * 50)

# grand_total = 0

# for item in cart:
#     print("{:<15}{:<10}{:<10}{:<10}".format(
#         item[0], item[1], item[2], item[3]))
#     grand_total += item[3]

# print("-" * 50)

# discount = 0

# if grand_total >= 1000:
#     discount = grand_total * 0.10
#     print("Discount (10%) : Rs.", discount)

# final_amount = grand_total - discount

# gst = final_amount * 0.05

# net_amount = final_amount + gst

# print("Subtotal       : Rs.", grand_total)
# print("GST (5%)       : Rs.", round(gst, 2))
# print("Payable Amount : Rs.", round(net_amount, 2))

# print("=" * 50)
# print("   Thank You For Shopping!")
# print("=" * 50)








# snake Game  --------------



 
# import tkinter as tk

# # Window
# root = tk.Tk()
# root.title("Snake Movement")
# root.geometry("600x400")

# canvas = tk.Canvas(root, width=600, height=400, bg="black")
# canvas.pack()

# # Snake Starting Position
# snake = [(100, 100), (80, 100), (60, 100)]
# size = 20

# direction = "Right"

# # Draw Snake
# def draw_snake():
#     canvas.delete("snake")

#     for x, y in snake:
#         canvas.create_rectangle(
#             x, y,
#             x + size, y + size,
#             fill="green",
#             tags="snake"
#         )

# # Move Snake
# def move():

#     global snake

#     head_x, head_y = snake[0]

#     if direction == "Right":
#         head_x += size

#     elif direction == "Left":
#         head_x -= size

#     elif direction == "Up":
#         head_y -= size

#     elif direction == "Down":
#         head_y += size

#     new_head = (head_x, head_y)

#     snake.insert(0, new_head)
#     snake.pop()

#     draw_snake()

#     root.after(150, move)

# # Keyboard Control
# def change_direction(event):

#     global direction

#     if event.keysym == "Right":
#         direction = "Right"

#     elif event.keysym == "Left":
#         direction = "Left"

#     elif event.keysym == "Up":
#         direction = "Up"

#     elif event.keysym == "Down":
#         direction = "Down"

# root.bind("<Key>", change_direction)

# draw_snake()
# move()

# root.mainloop()



# lst=[1,3,5,3,2,94,83,82]
# for i in lst:
#     if i%2==0:
#         print(i)



# n=int(input("star of number"))
# for i in range(1,n+1):
#     print(i*"*")

# n=int(input("star of number"))
# for i in range(n,0,-1):
#     print(i*"*")


# n=int(input("star of number"))
# for i in range(1,n+1):
#     print(" "*(n-i) , i*"*")


# n=int(input("star of number"))
# for i in range(n,0,-1):
#     print(" "*(n-i),i*"*")

# n=int(input("star of number"))
# for i in range(1,n+1):
#     print(" "*(n-i) , (2*i-1)*"*")
# for i in range(n-1,0,-1):
#     print(" "*(n-i) , (2*i-1)*"*")



# n=int(input("star of number"))
# for i in range(1,n+1):
#     print(i*"*" , end="\t")
# for i in range(1,n+1):
#     print(" "*(n-i), i* " *")




# n=int(input(" enter a number :"))
# for i in range(n,1,-1):
#     print(" "*(n-i),"* "*i)
# for i in range(1,n+1):
#     print(" "*(n-i), "* "*i)




# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1): 
#     print(" "*(n-i),"* "*i) 
# for i in range((n-1),0,-1): 
#     print(" "*((n-1)-i)," *"*i)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(i*"* ")
# for i in range(n-1,0,-1):
#     print(i* "* ")


# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     print(" "*(n-i), (2*i-1)*"*")
# for i in range(2,n+1):
#      print(" "*(n-i), (2*i-1)*"*")
    



# n=int(input(" enter a number :"))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i)
# for i in range(n,0,-1):
#     print("*"*i)


    

# lst=[5,3,2,1]
# for i in lst:
#     print(i*"*")
# print("ended")



class car:
    Brand="BMW"
    company_city="INDORE"

    def __init__(self,car_name,model,color,fuel_type,car_type):
        self.car_name=car_name,
        self.model=model,
        self.color=color,
        self.fuel_type=fuel_type,
        self.car_type=car_type
    
    def car_details(self):
        print(self.car_name)
        print(self.fuel_type)

cars=car("M5",2025,"black","elc","AMT")
print(cars.car_details())


