#
#!
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 

# n=int(input("Enter no.of rows:"))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     print(i,end=" ")
#   print()4

#!
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 
# A B C D E F G H I 

# n=int(input("Enter the no.of rows:"))
# for i in range(1,n+1):
#   for i in range(1,n+1):
#     print(chr(64+i),end=" ")
#   print()

#!
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# n=int(input("Enter the no.of rows:"))
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(i,end=" ")
#   print()

#!
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# F F F F F F 

# n=int(input("Enter the no.of rows:"))
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(chr(64+i),end=" ")
#   print()

#!
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=int(input("Enter the no.of rows:"))
# for i in range(1,n+1):
#   for j in range(1,n+2-i):
#     print("*",end=" ")
#   print()

#!
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 

# import time
# n=int(input("Enter the no.of rows:"))
# for i in range(1,n+1):
#   for j in range(1,n+2-i):
#     print(n+1-i,end=" ")
#   print()
# time.sleep(2)

#!
#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * * 

# import time
# n=int(input("Enter the no.of rows:"))
# for i in range(1,n+1):
#   print(" "*(n-i),end=" ")
#   for j in range(1,i+1):
#     time.sleep(1)
#     print("*",end=" ")
#   print()

#!
#Q.2
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=[10,20,30,40,50,60]
# print(a)

#  ValueError: attempt to assign sequence of size 6 to extended slice of size 5

#!
# arr=[
#     [1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]
#     ]
# for i in range(0,4):
#   print(arr[i].pop())

# 4
# 7
# 11
# 15

#!
# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#   arr[i-1] = arr[i]
# for i in range(0,6):
#   print(arr[i],end=" ")

#   2 3 4 5 6 6 


#!
# fl1=['a','b','c','p']
# fl2=fl1
# fl3=fl1[:]
# fl2[0]='g'
# fl3[1]='k'

# sum=0
# for ls in (fl1,fl2,fl3):
#   if ls[0]=='g':
#     sum+=1
#   if ls[1]=='k':
#     sum+=20
# print(sum)

# 22

#! 
# 1
# 2
# 3
# 4
# i=1
# while(i<5):
#   print(i)
#   i=i+1

#!
# i=1
# while i<6:
#   print(i)
#   if i==3:
#     pass
#   i=i+1

# 1
# 2
# 3
# 4
# 5

#!
# i=0
# while i<6:
#   i=+1
#   if i==3:
#     continue
#     print(i)

#!
# i=0
# while i<6:
#   i+=1
#   if i==3:
#     continue
#   print(i)

# 1
# 2
# 4
# 5
# 6

#!
# username= ''
# password= ''
# user = input("Enter user")
# pa = input("Enter password")

# while username != user and password != pa :
#   username = input("Enter username")
#   password = input("Enter password")

#!

# name=input("Enter any string:")
# alphabet=['a','e','i','o','u']
# consonant=0
# vowel=0
# for i in name:
#   if i in alphabet:
#     vowel+=1
#   else:
#     consonant+=1
# print(vowel)
# print(consonant)

# ?Enter any string:Aditya
# 2
# 4

#!
# #Anagrams
# #sorted -sort the string in alphabetical order
# str1 = input("Enter the string:")
# str2 = input("Enter the string:")

# # for i in str1:
# #   if i in str2:
# #     print("Anagrams")


# if sorted(str1) == sorted(str2):
#   print("Anagram")
# else:
#   print("Not Anagram")

# ?Enter the string:listen
# ?Enter the string:neslit
# ?Anagram

#!
#count words in a string
# s=input("Enter any sentense:")
# count=1
# for i in s:
#   if i == " ":
#     count+=1
# print(count)

# ?Enter any sentense:This is the sentense
# ?4

#!
#tuple

# mytuple = ("Aditya","Akshay","Soham","Darshan")
# print(mytuple)

# print(type(mytuple))

# mytuple[2]="Jack"
# print(mytuple)

# ?('Aditya', 'Akshay', 'Soham', 'Darshan')
# ?<class 'tuple'>
# ?TypeError: 'tuple' object does not support item assignment

#!
# init_tuple=()
# print(init_tuple.__len__())

#? 0

#!
# init_tuple_a='a','b'
# init_tuple_b=('a','b')
# print(init_tuple_a == init_tuple_b)

#? True

#!
# init_tuple_a='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a + init_tuple_b)

#? ('1', '2', '3', '4')

#!
# init_tuple=[(0,1),(1,2),(2,3)]
# result=sum(n for _.n in init_tuple)
# print(result)

#!
# l=[1,2,3]
# init_tuple=('Python',)*(l.__len__()-1[::1][0])
# print(init_tuple)


#!
# init_tuple=('Python')*3
# print(type(init_tuple))
# print(init_tuple)

#? <class 'str'>
#? PythonPythonPython

#!
# init_tuple=(1,)*3
# init_tuple[0]=2
# print(init_tuple)

#? TypeError: 'tuple' object does not support item assignment

#!
# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8]))

#? 4


