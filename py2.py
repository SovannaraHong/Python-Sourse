#input() = a function that prompts the user to enter data returns the enter data as string


# input("What is your name? :")
# first_name =input("enter your name: ")
# print(first_name)


age =input("Enter your age: ")
name = input("Enter your name: ")
is_Student=input("are you a student or not ")

age =int(age)
age +=1
if(is_Student == "yes"):
    print("You are a Student")
else:
    print("You are not a Student")
print(f"Hello {name}")
print(f"Your age is : {age} years old")
