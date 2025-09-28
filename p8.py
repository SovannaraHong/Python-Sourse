name =input("enter your name:")
if len(name)>12:
    print("name too long than 12 characters")
elif name.find(" ")!= -1:
    print("name contains only single characters")
elif not name.isalpha():
    print("name no need contains space ")
else:
    print(f"your {name} is correct condition")