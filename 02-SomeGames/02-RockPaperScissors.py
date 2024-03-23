import random

user_score = 0
computer_score =0


for i in range(10):
    x = random.randint(1,3)
    if x == 1:
        computer_choice ="rock"
    elif x==2:
        computer_choice = "paper"
    elif x==3:
        computer_choice = "scissors"




    user_choice = input("please enter your choice: rock,paper,scissors: ")

    print ("computer choice is: ", computer_choice)
    print ("user choice: ", user_choice)


    if computer_choice == "rock" and user_choice == "paper":
        user_score = user_score + 1
    elif computer_choice =="rock" and user_choice == "scissors":
        computer_score = computer_score + 1 


    elif computer_choice == "paper" and user_choice == "scissors":
        user_choice = user_choice + 1
    elif computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score + 1

    elif computer_choice == "scissors" and user_choice =="paper":
        computer_score = computer_score + 1
    elif computer_choice == "scissors" and user_choice =="rock":
        user_score = user_score + 1

    else:
        print ("No points on this round")

    print ("user score is: " ,user_score)
    print ("computer score is: " ,computer_score)


    if computer_score == 3:
        print("computer won")
        break


    if user_score ==3:
        print("user won")
        break
    