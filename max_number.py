#Max number`
n1=int(input("Number1:"))
n2=int(input("Number2:"))
n3=int(input("Number3:"))
n4=int(input("Number4:"))
n5=int(input("Number5:"))

if n1>n2 and n1>n3 and n1>n4 and n1>n5:
  print(n1," is greater")
elif n2>n1 and n2>n3 and n2>n4 and n2>n5 :
  print(n2," is greater")
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
  print(n3," is greater")
elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
  print(n4," is greater")
else:
  print(n5,"is greater")