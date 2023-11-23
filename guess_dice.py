import random

myrandom = random.randrange(1,7)

while True:
    x = int(input("Enter Number: "))
    if x == myrandom:
        print("Correct")
        break
    else:
        print("Incorrect")
