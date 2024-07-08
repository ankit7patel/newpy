# n=int(input("enter nu:"))
# i=1
# while i<=n:
#     print(i*"* ")
#     i+=1


# n=int(input("enter nu:"))
# i=1
# while i<=n:
#     print(" "* (n-i) + i * ' *')
#     i+=1


# n=int(input("enter nu:"))
# for i in range(1,(n+1)):
#     print(" "*(n-i),"*"*(2*i-1))


# n=int(input("enter nu:"))
# i=1
# while i<=n:
#     print(' '*(n-i) , i * ' *')
#     i+=1
    



# n=int(input("enter nu:"))    #(2n)=even ,(2n-1) oddd
# i=1
# while i<=n:
#     print(' '*(n-i) + (2*i-1) * '* ')
#     i+=1
    


#=================================


# n=int(input("enter num:"))
# i=1
# while i<=n:
#     print(((n+1)-i) *'*')
#     # print("*"*i)
#     i+=1



# n=int(input("enter nu:"))
# i = n
# while i > 0:
#     print(' ' * (n - i) + '*' * i)
#     i -= 1

# n=int(input(""))
# i=n
# while i>0:
#     print("  "*((n-1) -i),"*"*i)
#     i-=1

#------------------------
# n=int(input("enter nu:"))
# i=1
# while i<=n:
#     print(i*"*")
#     i+=1
# i=1
# while i<=n:
#     print(((n+1)-i) * '*')
#     i+=1
# #----------------------------------

# n=int(input("enter nu:"))
# i=1
# while i<n:
#     print(' '*(n-i) + i * '*')
#     i+=1
# i = n-1
# while i > n:
#     print(' ' * (n - i) + '*' * i)







# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1): 
#     print(" "*(n-i),"* "*i) 
# for i in range((n-1),0,-1): 
#     print(" "*((n-1)-i)," *"*i)





# n=int(input("enter nu:"))
# i=n
# while i>0:
#     print(' '*(n-i) + i * ' *')
#     i-=1





###################==============

# n=int(input(" enter a number :"))
# for i in range (1,n+1):
#     print(i * ' * ')


# n=int(input(" enter a number :"))
# for i in range (n-1,0,-1):
#     print(i*'*')
   
# n=int(input(" enter a number :"))
# for i in range (1,n+1):
#     print(" "*(n-i)," *"*i)


# n=int(input(" enter a number :"))
# for i in range (n,0,-1):
#     print(i*'*')
# for i in range (1,n+1):
#     print(i*'*')



# n=int(input(" enter a number :"))
# for i in range (1,n+1):
#     print(" "*(n-i),"* "*i)
# # n=int(input(" enter a number :"))
# for i in range (n,0,-1):
#     print(" "*(n-i),"* "*i)



# n=int(input(" enter a number :"))
# for i in range(n,0,-1):
#     print(" "*(n-i),"*"*i)
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i)


# n=int(input(" enter a number :"))
# for i in range(n,1,-1):
#     print(" "*(n-i),"* "*i)
# for i in range(1,n+1):
#     print(" "*(n-i), "* "*i)


# n=int(input(" enter a number :"))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i)
# for i in range(n,1,-1):
#     print( "*"*i)



n=int(input(" enter a number :"))
for i in range(1,n+1):
    print("*"*(2*i))