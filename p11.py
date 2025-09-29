#while loop = execute some code while some condition remains true


# name =input("enter your name:")
# while name =="":
#     print("your name can't be empty")
#     name = input("enter your name:")
# print(f"your name is {name}")



# age =int(input("enter your age : "))
# while age <0:
#     print("your age cant not be negative")
#     age = int(input("enter your age : "))
# print(f"your age is {age}")


num =float(input("enter num:"))
while num<0 or num>10:
    print(f"enter number please enter number between 0 and 10")
    num = float(input("enter num:"))
print(f"your number is {num}")