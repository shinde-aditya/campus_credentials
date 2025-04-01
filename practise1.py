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


num1=int(input("First no:"))
num2=int(input("second no:"))
hcm=1

for i in range(1,min(num1,num2)):
    if(num1%i==0 and num2%i==0):
        hcf=i
print(hcf)