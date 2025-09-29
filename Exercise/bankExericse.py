initialPrice=0
interestRate=0
time=0

# while initialPrice<=0:
#     initialPrice=float(input("enter initial price:"))
#     if initialPrice<=0:
#         print("your money cant not be zero or negative")
#
# while interestRate<=0:
#     interestRate=float(input("enter rate price:"))
#     if interestRate<=0:
#         print("your rate cant not be zero or negative")
#
# while time<=0:
#     time=int(input("enter time:"))
#     if time<=0:
#         print("your time cant not be zero or negative")
#
# total = initialPrice*pow((1+interestRate/100),time)
# print(f"your money is {initialPrice} $ ")
# print(f"your rate is {interestRate} %")
# print(f"your time is {time}")
# print(f"your year is{time}/years and your money you could be have back to you {total:.2f}$")


while True:
    initialPrice=float(input("enter initial price:"))
    if initialPrice<=0:
        print("your money cant not be zero or negative")
    else:
        break
while True:
    interestRate=float(input("enter rate price:"))
    if interestRate<=0:
        print("your rate cant not be zero or negative")
    else:
        break
while True:
    time=int(input("enter time:"))
    if time<=0:
        print("your time cant not be zero or negative")
    else:
        break

total = initialPrice*pow((1+interestRate/100),time)
print(f"your money is {initialPrice} $ ")
print(f"your rate is {interestRate} %")
print(f"your time is {time}")
print(f"your year is{time}/years and your money you could be have back to you {total:.2f}$")