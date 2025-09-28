# accessing index by [start : end : step]


phone_number="1234-4543-2423-2423"
print(phone_number[0])
print(phone_number[:5])
print(phone_number[5:9])
print(phone_number[5:])
print(phone_number[-1])

#stp
print(phone_number[::2])

# exercise
print(f"XXXX-XXXX-XXXX-{phone_number[-4:]}")