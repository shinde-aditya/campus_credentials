#! list
# mylist=["Aditya","prashant",77,"ankush","Soham",88,"Darshan",55,99]
# print(mylist)
# print(type((mylist)))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

#list is mutable
# mylist[0] = "Akshay"
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print("not available")

# mylist.append("harsh")
# mylist.append("Laxman")
# print(mylist)

#?insert()
# mylist.insert(1,"Sanket")
# print(mylist)

#?remove()
# mylist.remove("Aditya")
# print(mylist)

#?copy()
# newlist=mylist.copy()
# print(newlist)

#?nested list
# mylist2=[["Aditya","176"],['89.65'],['11111','uuuu']]
# #print(mylist2[row][col])
# print(mylist2[0][0])
# print(mylist2[0][1])
# print(mylist2[1][0])
# print(mylist2[2][0])
# print(mylist2[2][1])

# list1 = ["Prashant","Jha"]
# print(list1*3)

# list2=[50,25,30]
# print(list1+list2)

#?del
list2 = [50,30,25,"Prashant"]#
#del list2[2]
# del list2
# print(list2)

#?clear
# list2.clear()
# print(list2)

#?list()
# name="Prashant"
# myname=list(name)
# print(myname)

#?reverse()
# mylist=[10,20,30,40]
# mylist.reverse()
# print(mylist)

#?sort
list=[90,40,30,80,75]
# list.sort()
# print(list)

#?decending order
# list.sort(reverse=True)
# print(list)

#?id()
mylist=[90,43,55,88,22]
newlist=mylist
print(id(mylist))
print(id(newlist))
