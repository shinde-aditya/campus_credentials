#
#! max min

# list=[5,3,9,2,8]
# max=min=list[0]

# for i in range(len(list)):
#     if list[i]>max:
#         max=list[i]
    
#     if list[i]< min:
#         min=list[i]

# print(max)
# print(min)


#!second largest
# list=[7,3,9,2,8]
# list.sort()
# print(list[-2])

#!move zero to the end
# list=[0,1,0,3,12]  #EO->[1,3,12,0,0]

# for i in list:
#     if i==0:
#         list.remove(i)
#         list.append(i)
        

# print(list)


#!intersection of three arrays
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)
 

#!
# c=[2,1,4,5,5,4,4,1,1]

# count=0
# even=0
# odd=0

# for i in c:
#     if i==4:
#         count+=1
#     elif i==2:
#         even+=1
#     elif i==5:
#         odd+=1
# print(even)
# print(odd)

#!
from ast import Mult
from re import X


# rollno=[3,5,7,11,4,5,2]
# for i in rollno:
#     if i==2 or i==4 or i==6 or i==8 or i==10:
#         print('Even number is found',i)
#         break
   
# mycart=[10,20,30,40,300,500,60,700]
# for i in mycart:
#     if i>400:
#         print("This is my purchased cart item")
#         continue
#     print(i)

# else:
#     print("You have purchase everything")

#!1 5
# 2 4
# 4 2
# 5 1

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,' ',j)
     
#!

# print("aditya Shinde".find("d"))
# print("aditya Shinde".index("d"))
# print("aditya Shinde".count("a"))

#!count()
n=[1,2,3,5,5,5,1,2,4,4,6,6,6]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.count(6))
# print(n.count(7))
 
#!index():return index of the first occurence
# val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
# print(val.index(1))
# print(val.index(2))
# print(val.index(3))
# print(val.index(4))
# print(val.index(5))
# print(val.index(6))

#!
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

# print(id(y))
# print(id(z))

#!
# a=50
# b=30
# c=20
# d=10

# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#!consecutive ones
list=[1,1,0,1,1,1,0,1,1,1,1]
count=0
for i in list:
    if i ==1:
        count+=1
    else:
        count=0

print(count)

#!product of array Except self
list=[1,2,3,4]
m=1
# for i in list:
print(Mult(list)) 