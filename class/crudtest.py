# class student:
#     stu_collega="career college bhopal"
#     stu_quli="MCA"
    
#     def __init__(self,name,age,adr):
#         self.name=name
#         self.age=age
#         self.adr=adr
#         print(student.stu_collega)
#         print(student.stu_quli)
       

#     def show(self,cgp,job):
#          z=50
#          self.cp=cgp
#          self.job=job
#          print(self.name)
#          print(self.age)
#          print(self.adr)
#          print(z)

#     def show_de(self):
#         print(self.cp)
#         print(self.job)
#         print(obj.a)
#         print(obj.name)
    
# obj=student('ankit', 22 ,'bhopal')
# obj.show(9.8,'yes')
# obj.show_de()
# print(student.stu_collega)
# obj.a=10 
# print(obj.a)



# class book:
#     price=1000

#     @classmethod

#     def update_price(cls):
#         cls.price=1500
#         print(cls.update_price)
       

#     def show(self,name):
#         self.name=name

#         print(self.price)

# obj=book()
# obj.update_price()
# obj.show("python")
# print(obj.name)
        


# Shopping_Cart:---

# class MyCart:
#     def __init__(self):
#         self.my_items = []

#     def add_item(self,item,price):
#         self.my_items.append({'item_name':item,'item_price':price})

#     def show_items(self):
#         if len(self.my_items)==0:
#             print("Cart is empyty")
#         else:
#             print("All cart details are :")
#             for i in (self.my_items):
#                 print(i['item_name'],'=',i['item_price'])   

#     def total_price(self):
#         total = 0
#         for i in self.my_items:
#             total += i["item_price"]
#         print("Total Amount =",total)
    
#     def remove_item(self, item_name):
#         for item in self.my_items:
#             if item["item_name"] == item_name:
#                 self.my_items.remove(item)
#                 break

#     def clear_cart(self):
#         self.my_items=[]
#         print("Now your cart is empity...")

# obj = MyCart()
# obj.add_item('Laptop',25000)
# obj.add_item('Table_Lamp',5000)
# obj.add_item('Decor',2000)
# obj.show_items()
# obj.total_price()
# obj.remove_item('Laptop')
# obj.show_items()
# obj.total_price()
# obj.clear_cart()
# obj.show_items()


# class book:
#     price=1000

#     @classmethod

#     def update_price(cls):
#         cls.price=20000000
       
       

#     def show(self,name):
#         self.name=name
#         print(book.price)

# obj=book()
# obj.update_price()
# obj.show("python")
# print(obj.name)
        


# class ankit:

#     def room1(self):
#         print("enter a room ")

# class ad:
#     def room1(self):
#         print("enter a room ad room1 ")

#     def room2(self):
#         print("enter a room room2 ")

# class key(ad,ankit):   ## (MRO)--> LEFT to right value leta hai 
#     def lock(self):
#         self.room1()
#         self.room2()
#         super().room2()
#         super().room1() #### dono method ko cl krega    
         

# obj=key()
# obj.lock()




# class ankit:

#     def room(self):
#         print("enter a room ")

# class ad:
#     def room(self):
#         print("enter a room ad ")

# class key(ankit,ad):   ##(MRO)--> LEFT to right value leta hai 
#     def lock(self):
#         self.room()
#         super()   #### dono method ko cl krega 
#         super()

    

# obj=key()
# obj.lock()

# my_list=(1,2,3,4,5,6,7,8,9)
# def prime(n):
#     if n==1 or n==0:
#         return False
    
#     for i in range(2,int(n/2)+1):
#         if n%i==0:
#             return False
#     return True

# print(list(filter(prime,my_list)))



# from functools import reduce

# n = int(input("Enter a number: "))

# def fac(x, y):
#     return x * y
# numbers = list(range(1, n+1))

# x= reduce(fac, numbers)
# print(x)




class MyCart:
    def __init__(self):
        self.my_items = []

    def add_item(self,item,price):
        self.my_items.append({'item_name':item,'item_price':price})

    def show_items(self):
        if len(self.my_items)==0:
            print("Cart is empyty")
        else:
            print("All cart details are :")
            for i in (self.my_items):
                print(i['item_name'],'=',i['item_price'])   

    def total_price(self):
        total = 0
        for i in self.my_items:
            total += i["item_price"]
        print("Total Amount =",total)
    
    def remove_item(self, item_name):
        for item in self.my_items:
            if item["item_name"] == item_name:
                self.my_items.remove(item)
                break

    def clear_cart(self):
        self.my_items=[]
        print("Now your cart is empity...")

obj = MyCart()
obj.add_item('Laptop',25000)
obj.add_item('Table_Lamp',5000)
obj.add_item('Decor',2000)
obj.show_items()
obj.total_price()
obj.remove_item('Laptop')
obj.show_items()
obj.total_price()
obj.clear_cart()
obj.show_items()



                         
                         
