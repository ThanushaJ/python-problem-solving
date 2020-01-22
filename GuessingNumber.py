import random

x = random.randint(1, 10)
attempts = 5
while attempts > 0:
    print(attempts, " attempts left")
    print("guess the number")
    num = int(input("Enter  "))
    attempts -= 1
    if num == x:
        print("you won")
        break
else:
    print("You lost")
