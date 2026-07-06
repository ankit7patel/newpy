
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

 """

num=[10,20,30,405,500,84]

x=405
for i in num:
    if i == x :
        
        print("found",i) 
        
    





