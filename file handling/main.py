# f=open("n1.txt",'w')
# data=('bhaiya me bhaiya ankit bhaiya')
# f.write(data)
# print(data)

# data1=('uhifuh\n',' ufi\n','    hfoioh  \n')
# f.writelines(data1)
# print(data1)

# print(f.writable())



# f=open("n1.txt",'r')
# data = f.read()
# print(data)


f=open('n1.txt','r')
data=f.read()
print(data)
data=f.readable()
print(data)


f=open('n1.txt','r')
print(" start point ", f.tell())
# data = f.read(5)
f.seek(-8,0)
print("end :" , f.tell())
print(data)







