
while True:
    khmer = input("Enter your khmer number here: ")
    while True:
        # if khmer=="" or khmer>0 and khmer <=125:
        if khmer=="" or not (0 <= int(khmer) <= 125):
            print("your score khmer is invalid")
            khmer = input("Enter your khmer number here: ")
        else:
            break
    math = input("Enter your math number here: ")
    while True:
        if math == "" or not (0 <= int(math) <= 125):
            print("your score math is invalid")
            math = input("Enter your math number here: ")
        else:
            break
    english = input("Enter your english number here: ")
    while True:
        if english == "" or not (0 <= int(english) <= 50):
            print("your score english is invalid")
            english = input("Enter your english number here: ")
        else:
            break
    history = input("Enter your history number here: ")
    while True:
        if history == "" or not (0 <= int(history) <= 75):
            print("your score history is invalid")
            history = input("Enter your history number here: ")
        else:
            break
    khmer = int(khmer)
    math = int(math)
    english = int(english)
    history = int(history)
    print(f"your khmer is {khmer}")
    print(f"your math is {math}")
    print(f"your english is {english}")
    print(f"your history is {history}")
    totalScore = khmer + math + english + history
    print(f"your total score is {round(totalScore)}")
    if totalScore <237:
        print("your Greate is F")
    elif 237 <= totalScore <= 322:
    # elif totalScore >= 237 and totalScore <= 322:
        print("your Greate is D")
    elif 322 <= totalScore <= 410:
        print("your Greate is C")
    elif 410 <= totalScore <= 490:
        print("your Greate is B")
    else:
        print("your Greate is A")
    break






