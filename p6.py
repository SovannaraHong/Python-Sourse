#condition of python have or and not


temp=50
is_sunny=False
check = True
if temp>=35 or is_sunny:
    print("you can go outside ")
    print("it sunny☀️")
elif temp<35:
    print("you cant go outside")
    print("it raining")

if temp>=40 and not is_sunny:
    print("it too much hot you cant go outside")
elif temp>=35 and check:
    print("you can go outside with family")