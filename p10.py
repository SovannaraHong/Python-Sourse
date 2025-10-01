price1:float=2.342
price2:float=-544.34
price3:float=300.235
#it takes 2last number
print(f"price1: {price1:.2f}")
print(f"price2: {price2:.2f}")
print(f"price3: {price3:.2f}")
print("============================")
# space + with number =10
print(f"price1: {price1:10}")
print(f"price2: {price2:10}")
print(f"price3: {price3:10}")
print("============================")

#+0 first with number =10
print(f"price1: {price1:010}")
print(f"price2: {price2:010}")
print(f"price3: {price3:010}")
print("============================")

#+number with space=10 || space end
print(f"price1: {price1:<10}")
print(f"price2: {price2:<10}")
print(f"price3: {price3:<10}")
print("============================")


#space right and left text center
print(f"price1: {price1:^10}")
print(f"price2: {price2:^10}")
print(f"price3: {price3:^10}")
print("============================")

#check positive number or negative number // use with + or use with space
print(f"price1: {price1:+}")
print(f"price2: {price2:+}")
print(f"price3: {price3:+}")
print("============================")


#take , with number like 1000 to 1,000
print(f"price1: {price1:,}")
print(f"price2: {price2:,}")
print(f"price3: {price3:,}")

print("============================")


#plus================
print(f"price1: {price1:+,.2f}")
print(f"price2: {price2:+,.2f}")
print(f"price3: {price3:+,.2f}")