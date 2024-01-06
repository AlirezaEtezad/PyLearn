import random


computer_number = random.randint(1,100)


for i in range (100):
    user_number = int(input("please enter your guess: "))

    if computer_number == user_number :
        print ("You won")
        break
    elif computer_number > user_number:
        print("go up")

    else:
        print ("go down")
print("You guessed ",i+1," times.")
