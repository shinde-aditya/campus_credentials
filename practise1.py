#sum of all natural numbers from 1 to 10
# sum =0
# for i in range(1,11):
#     sum+=i
# print(sum)


#Factorial of any number
# num = int(input("Enter any number:"))
# fact=1
# for i in range(1,num+1):
#     fact*=i

# print(fact)

#fibonaacci series
# num = int(input("Enter the number:"))
# str=''
# count=0
# first = 0
# second = 1

# while count<num:
#     print(first)
#     nth=first+second

#     first=second
#     second=nth
#     count +=1

#     print(first)

 
# a, b = 0, 1  

# for _ in range(num):  
#     print(a, end=" ")  
#     a, b = b, a + b  


#LCM
# num1=int(input("First no:"))
# num2=int(input("second no:"))

# if num1>num2:
#     greater=num1
# else:
#     greater=num2

# while(True):
#     if((greater%num1==0) and (greater%num2==0)):
#         lcm=greater
#         break
#     greater+=1
# print(lcm)


# num1=int(input("First no:"))
# num2=int(input("second no:"))
# hcm=1

# for i in range(1,min(num1,num2)):
#     if(num1%i==0 and num2%i==0):
#         hcf=i
# print(hcf)


#armstrong number

num = int(input("Enter a number: "))

# initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


#prime number
num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")