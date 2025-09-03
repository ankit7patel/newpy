for i in range(1,11):
        print(i*6)

i=0
while i<=20:
    if i%2==0:
        print(i)
    else:
        print("odd number" ,i)
    i+=1


n=30
sum=0
for i in range(2,n):
    if i%2!=0:
        sum=sum+i
        print(i, "total",sum)



# # n=input("enter your age")
x=10
y=20.0
print('python')
print(id(x))
print(id(y))
print(type(x))
print(x+y)

#Converting string into integer 
string = "56"
num = 44 
str_num = int(string)
sum = num + str_num
print("Sum: ", sum)







x=23
y=str(x)
sum=x+y
print(type(y))
print(sum)


str="50"
num = 20
str_num=int(str)
sum = num+str_num
print("sum:",sum)


num1 = 20 
num2 = 30
str1 = "30"

str_num = int(str)
sum = num1+num2+str_num
print("total_sum:", sum)

input("enter your name")
input("enter your age ")
input("enter your mobile_no ")
input("enter adderes age ")
input("enter your batch ")


num6=input()
num3=float(input("enter no:"))
num4=int(input("enter no:"))
num5=int(input("enter no:"))
# str_num=float(num6)
num_6=float(num6)

total_sum=num3+num4+num5+num_6
print("total of num:", total_sum)

P=float(input("enter no of P  :"))
R=float(input("enter no of R:"))
T=float(input("enter no  of T:"))

total=P*R*T/100

print("total_sum:", total)

a = "Hello, World!"
print(a[1])
       
a ="hello world"
print(a[:6])


age = 22  # 1st
age_str=str(age)
txt = "my name is ankit , I am  " + age_str
print(txt)


age="21" #second 
txt="my name is ankit , I am :" +age 
print(txt)

i = 1 # while loop
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
   

i = 5 #while loop
j = 6
while i <=50:
    print(i )
    i += 5
while j <=60 :
    print(j)
    j += 6


for i in range(1,10): #for loop 
    print(i)
    if(i == 5):
     break
    i += 10





'''
 . = current directory /folder
.. = previews directory /folder

../../../.. = 3 folder 

cd CODE = folder/directory _name 

cd = change directory

1)-python -m py_compile first.py = machine language
2)cd _pycache_  --> python first.cpython-312.pyc
3)cd ../ --> python -m dis first.py
cll by Reference
futur 
'''

# Example of ord()
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}.")  # Output: The ASCII value of 'A' is 65.

# Example of hex()
integer_value = 255
hex_value = hex(integer_value)
print(f"The hexadecimal representation of {integer_value} is {hex_value}.")  # Output: The hexadecimal representation of 255 is 0xff.

# Example of oct()
oct_value = oct(integer_value)
print(f"The octal representation of {integer_value} is {oct_value}.")  # Output: The octal representation of 255 is 0o377.

# Example of chr()
ascii_value = 65
char = chr(ascii_value)
print(f"The character corresponding to ASCII value {ascii_value} is '{char}'.")
