
# for x in range(1,3):
#     for y in range(1,10):
#         for z in range(1,5):
#             print(x,y,z, end="")
# print()
            #3


# row =int(input("enter row: "))
# col =int(input("enter column: "))
# symbol =str(input("enter symbol: "))
# for x in range(row):
#     for y in range(col):
#
#             print(symbol ,end="")
#     print()
#
#


#loop data in arr ============================================

# list =[] it can with duplicate it can remove change or add
#Set ={} it cant duplicates you can add and remove, but it can not change
#Tuple=() You want a fixed collection of items that shouldn’t change.
#Often used for returning multiple values from a function.


#============================================
#list==============
# fruits=["apple","banana","orange","coconut"]
# print(fruits)
# for x in fruits:
#     print(x)
# print(dir(fruits)) #showing function all
# print(len(fruits)) # count in arr or count text in string
# print(help(fruits)) #show detail
# print("apple" in fruits) # return true false find item
# fruits.append("mango")
# fruits.remove("banana")
# fruits.insert(2,"mango") #insert by index
# fruits.sort() #sort a-z and z-a
# fruits.reverse() #reverse item in arrr not revers by z-a

# fruits.clear() #it clear all items
# print(fruits.index("banana")) #print output by index
# print(fruits.count("orange")) #count item in arr

#Set ==============================

fruits={"apple","banana","orange"}
# print(dir(fruits))
# fruits.add("pineapple")
# fruits.remove("orange")
# fruits.pop()
# fruits.clear()
# for fruits in fruits:
#     print(fruits)
#
# a= {1,2,3,4,5}
# b={1,2,3,4,5,6,7,8,9}
# print(a,b)
# print(a&b)
# print(a|b)
#


#tuple ===========================

num =(19,29,39,45)

def get_name (age):
    return age
print(get_name(num))
for nums in num :
    print(nums)
# print(num.index(29))
# print(num.count(1))



arr_num =[1,2,3,4,5,56,7,8,9,9,9,3,2,4,5,6,]

print(set(arr_num))