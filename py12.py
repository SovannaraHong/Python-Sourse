balance =99.22
#
# num=float(input("Enter a number: "))
# balance+=num
# print(f"Your balance is {balance}")

while True:
    try:
        num = float(input("Enter a number: "))
        if num<0:
            print("That's not a positive number.")

        else:
            break
    except ValueError:
        print("you cant input text or negative number")
print(f"Your balance is {balance}")