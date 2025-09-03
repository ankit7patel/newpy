def add(x,y):     
   return x+y   
def subtract(x,y):     
   return x-y   
def multiply(x,y):     
   return x*y  
def divide(x,y):     
   return x/y   

while True:   
    print ("Please select the operation.")    
    print ("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Off\n")             
    n = int(input("Please enter choice (1,2,3,4,5): "))          
    p = int (input ("Please enter the first number: "))    
    q = int (input ("Please enter the second number: ")) 
    print(type(n),type(p),type(q))         
    if n == 1:    
        print (p, " + ", p, " = ", add(p, q))           
    elif n == 2:    
        print (p, " - ", q, " = ", subtract(p, q))          
    elif n == 3:    
        print (p, " * ", q, " = ", multiply(p, q))    
    elif n == 4:    
        print (p, " / ", q, " = ", divide(p, q))    
    elif n==5 :
        break
