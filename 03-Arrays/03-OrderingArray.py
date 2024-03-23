user_array = []

while True:
    print("if finished enter 'end'")
    user_input = (input("please enter a number:"))
    if user_input == "end":
        break

    elif user_input.isdigit():

        user_array.append(int(user_input))
    else:
        print("you can only enter a number 😐")

print (sorted(user_array))