# balance =99.22
#
# num=float(input("Enter a number: "))
# balance+=num
# print(f"Your balance is {balance}")

# while True:
#     try:
#         num = float(input("Enter a number: "))
#         if num<0:
#             print("That's not a positive number.")
#
#         else:
#             break
#     except ValueError:
#         print("you cant input text or negative number")
# print(f"Your balance is {balance}")


#====================================================


fruit=["apple", "banana", "cherry"]
for item in fruit:
    print(item)

for i in range(5):
    print(f"number is {i}")


for item in range(2,10,2):#2+2=4| 4+2=6|6+2=8|8+2=10 but 10 equal to 10 exit
    print(item)
print("==========================================================")

for num in range(1,5,2):
    print(num)
print("==========================================================")

for number in range(1,12,4):#1+4=5|5+4=9
    print(number)
print("==========================================================")

for n in range(1,4):
    print(n)
    print("end")
print("==========================================================")
for x in range(1,4):
    for y in range(1,6):
        print(x,y)

print("==========================================================")
