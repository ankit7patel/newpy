"""i=1
n=100

while i<=n:
    print(i, end=" ")
    i=i+1
"""

# i 2 4 8 16 32 64 
#=int(input("enter a number"))
"""def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
fact(5)

n=5

for i in range(1,n+1):
    print(i*"*")

#list=[4,2,1,6,7,8]

tuple=(6,5,4,1)
for i in tuple:
    print(i*"*")


n=int(input("number a stars"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1),"end")
for i in range(n-1,0,-1):
    print(" "*(n-i),"*"*(2*i-1))

n=int(input("a number"))
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i)

for i in range(1,n+1):
    print(" "*(n-i),"*"*i)

for i in range(n,0,-1):
    print("*"*i)


n=int(input("number"))
for i in range(n,0,-1):
    print(" "*(n-i),"*"*(2*i-1))
for i in range(2,n+1):
    print(" " *(n-i),"*"*(2*i-1))



n=int(input("number"))
for i in range(n,0,-2):
    print(" "*(n-i),"*"*i)



n=int(input("num"))
sum=0
for i in range(n):
    if i%2==0:
        print(i,"even")
        sum+=i

print("total number of sum",sum)


n=int(input("num"))
for i in range(2,n,2):
    print(i,end="")



n=int(input("num"))
i=1
sum=0
while i<=n:
    if i%2==0:
        print(i)
        sum+=i
    i+=1
   
print("totoal sum",sum)



n=int(input("num"))
for i in range(1,11):
    if i<10:
        print(i*n,end=",")
    else:
        print(i*n)






n=int(input("num"))
i=1
sum=0
while i<=n:

    if i<n:
        print(i , end="+")
    else:
        print(i,end="=")
    
    sum+=i
    i+=1
print(sum)



n=int(input("num"))
sum=0
for i in range(1,n+1):
    if i<n:
        print(i,end="+")
    else:
        print(i,end="=")
    sum+=i
print(sum)


"""


    