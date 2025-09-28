name =input("enter your name:")
if len(name)>12:
    print("name too long than 12 characters")
elif  name.find(" ")!= -1: #input _nara
    print(f"your {name} cant use with contain space")
elif len(name)==0:
    print("name cant be an empty string")
elif not name.isalpha():
    print(f"your {name} cant use with number or space ")
else:
    print(f"your {name} is correct condition")