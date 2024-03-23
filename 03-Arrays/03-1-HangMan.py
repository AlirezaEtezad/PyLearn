import random

words_bank = ["tree", "book", "schedule", "life", "leonard", "itisthebestchoice"]

word = random.choice(words_bank)

corrcet_guess = []
worng_guess = []

user_mistakes = 0
while user_mistakes < 6:

    

    for i in range(len(word)):
        if word[i] in corrcet_guess:
            print(word[i], end = " ")

        else:
            print("-", end=" ")


    if set(word) == set(corrcet_guess) :
        print("you won")
        break

            
    user_guess = input("your guess: ").lower()

    


    if len(user_guess) == 1:

        if user_guess in (set(corrcet_guess) or set(worng_guess)):
            print("😐 do not enter duplicate")


        elif user_guess in word:
            corrcet_guess.append(user_guess)
            print("✅")

        else:
            worng_guess.append(user_guess)
            user_mistakes +=1
            if user_mistakes == 1:
                print("❌","you made ",user_mistakes," mistake out of 6")
            else:
                print("❌","you made ",user_mistakes," mistakes out of 6")
    else:
        print("enter only 1 charactor")
if user_mistakes == 6:
    print("game over")
    print("you lost 😔")


