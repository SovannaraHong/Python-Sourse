foods=[]
prices={}
qty={}

while True:
    food = input("Which food or Drink you want to buy: (q to quit) ")
    if food.lower() == "q":
        break
    else:
        price_input=input(f"What of {food} you want to buy?: $")
        qty_input=input(f"What of {food} you want to buy?: $")
        foods.append(food)
        prices[food]=float(price_input)
        qty[prices]=int(qty_input)
        break
print(foods)
print(prices)
print(qty)


