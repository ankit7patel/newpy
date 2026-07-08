
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

nums = [10, 15, 22, 31, 40, 55, 61] 

even = []
sum=0
for num in nums:
    if num % 2 == 0:
        even.append(num)
        sum+=num

print(even , "sum of number : ", sum , end="\n")

num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")