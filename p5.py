#if else statement
#
# age =int(input("enter age"))
#
# if age<=19:
#     print("you are young")
# elif age>19:
#     print("you are adult")
# else:
#     print("you are old")

# disPr="Big Pizaa"
#
# food =input(f"hello sir what food you would like to buy?: ")
# response =input(f"Are you come from alone or waiting friend (Y/N): ")
# if(response == "Y"):
#     print(f"ohh great i recomment this food for alot people {disPr}")
# else:
#     print(f"Ohh it okay wait a minuite")



#Calculater



sign=input(f"enter the sign calculator (+/-/*/%): ")
num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))
if sign == "+":
    result =num1+num2
    print(round(result))
elif sign == "-":
    result =num1-num2
    print(result)
elif sign == "*":
    result =num1*num2
    print(result)
elif sign == "/":
    result =num1/num2
    print(result)
else:
    print(f"Please enter a valid sign")