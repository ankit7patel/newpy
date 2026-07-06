""""
dict = {
    "name":"ankitt",
    "city":"indore",
    "course":"MCA"

}
dict["name"]="ankuuu"


print(dict['name'])
print(dict['city'])

print(dict.items())

print(dict.keys())
print(dict.get("najje"))
dict.update({"college":"career college bhopal"})
print(dict.items())

new_dict={
    "number":"8187329"
}

dict.update(new_dict)

#rint(dict.update(new_dict))
print(dict)

print(list(dict.items()))
print(list(dict.keys()))



n=int(input("number"))
sum=0
for i in range(1,n+1):
    if i < n:
        print(i ,end="+")
    else:
        print(i,end="=")
    sum+=i
print(sum)


n=int(input("number"))
for i in range(1,n+1):
    print(i,"=", i*i)
n=int(input("number"))
for i in range(1,n+1):
    print(i*n ,end=" ")


n=int(input("number"))
i=1
while i<=10:
    print(i*n , end=" ")
    i+=1


list=[1,3,5,6,7,8,4,54]
for i in list:
    print(i*i,end=" ,")



#number of total digit count
num=int(input("num"))
count=0
for i in str(num):  # int ko str me conv..
    count+=1
print(count)



#char count
name=input("char")
count=0
for i in name: # i last tk chlega counter ka kaam kra ra hai 
    count+=1



#number of total digit count while 
num=int(input("num"))
count=0

while num>0:
    count+=1
    num = num//10  # revers 
print(count)

print(count)



#reverse of number 

n=input("number")
rev = " " 
for i in n:
    rev = i + rev
print(rev)


str="aJKFBKjkcKJWKJKJCJK"
print(str[::-1])


text=input("string   : ")

reverse=" "

for i in range(len(text)-1,-1,-1):
    reverse=reverse + text[i]
print(reverse)


# reverse string 
text=input("string   : ")
i=len(text)-1
reverse= " "

while i>=0:
    reverse = reverse + text[i]
    i-=1
print(reverse)




n=int(input("num"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


n=int(input("num"))
i=1
fact=1


while i>=n:
    fact*=i
    i+=1
print(fact)




 #prime number 
num=int(input("number :"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
        print("prime  :---")
else:
        print("not prime :")

       

num=int(input("number :"))
count=0
for i in range(1,num+1):
    if i%2==0:
       count+=1
print("even ")


num=int(input("number :"))
if num%2==0:
    print(num,"even")
else:
    print("not")


num=int(input("number :"))
for i in range(1,num+1):
    if i%2==0:
        print(i ,end=" , ")
        

 
list=[1,2,3,23,21,4,43,24,543,21,53,553,432,4,5,6543,3,24,4,543,2,39,7,6,5,4]
count=0
for i in list:
    if i%2==0:
        print("even",i)
        count+=1
print(count)


# armstrong number
num=int(input("number :")) 
total=0
for i in str(num):
    total += int(i)**3

if total == num:

    print("Armstong number ")

else:
    print("NOT armstong")


##  subrting of size three with distinct char

s="xyzzazb"
n=len(s)
ans=0

for i in range(1,n-2):
    if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
        ans+=1
print(ans)



#frequency count 

arr=[1,1,2,3,4,3,2,1,5,7,8,7,6,5,6,8,2,8,3,6]
num=0
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1

print(freq)


#unique element

arr=[134,5,5,5,417,17,8148,458,588,134,588,17,74,88,88]
dict={}
 #arr.set()
print(tuple(arr))
print(set(arr))




lst=["apple","banna","mango"]
d={}
for i in range(len(lst)):
    d[i]=lst[i]

print(d)



### dictaionary
d1={}

d1["name"]="vishu"
d1["age"]=24
d1["city"]="delhi"
d1["course"]="MCA"

print(d1["name"])
print(d1.keys())

print(d1.items())

for key,value in d1.items():
    print(key,value )

print(dict(d1))





d1={'name': 'vishu', 
    'age': 24,
      'city': 'delhi',
        'course': 'MCA'
}

d1["city"]="pune"
print(d1["city"])
print(d1.values())




# update 1
d1_new={"laptop":"Lenovo",
        "ram":"16GB"
}
d1.update(d1_new)
print(d1)
#2

d1.update({"rollnum":"1632"})
print(d1)



lst=[12,32,12,47,31,61,43,22,74,31,90]
even=[]
for i in lst:
    if i%2==0:
        even.append(i)
print(even)

lst=[12,32,12,47,31,61,43,22,74,31,90]
list=[]
for i in lst:
    if i%2==0:  
        print(i,end=" ,")


lst=[12,32,12,47,31,61,43,22,74,31,90]
lst.sort(reverse=True)
print(lst)

 """

lst=[12,32,12,47,31,61,43,22,74,31,90]
maxm=lst[0]
minm=lst[0]

for i in lst:
    if i > maxm:
        maxm = i

    if i < minm:
        minm = i
print(maxm)
print(minm)



  