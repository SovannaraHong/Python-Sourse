#for loop
import time



for x in range(1,2):
    print(f"i love you so much")
    if x ==10:
        print("i just kidding hahaha")
        continue
for y in range(1,5):
    print(y)

my_text=int(input("Enter time for countdown: "))
for x in reversed(range(1,my_text+1)):
    print(x)
    time.sleep(1)
print("HAPPY NEW YEAR")



times=int(input("Enter times for times: "))
for x in reversed(range(1,times+1)):


    #if else
    # if x<10:
    #     print(f"00:00:0{x}")
    # else:
    #     print(f"00:00:{x}")


    #ternary
    text = f"00:00:0{x}" if x < 10 else f"00:00:{x}"
    print(text)
    time.sleep(1)
print("HAPPY BIRTHDAY TO YOU")




#or use with converting
timee =int(input("Enter time for times: "))
for x in reversed(range(1,timee+1)):
    second =x %60
    minute =int(x//60) %60
    hour =x//3600
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

