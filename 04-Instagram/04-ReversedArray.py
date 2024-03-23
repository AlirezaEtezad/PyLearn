user_array = []
reversed_user_array = []

while True:
    print("if finished enter 'end'")
    user_input = (input("please enter a number:"))
    if user_input == "end":
        break

    elif user_input.isdigit():

        user_array.append(int(user_input))
    else:
        print("you can only enter a number 😐")

for digit in range(len(user_array)-1 , -1, -1):
    reversed_user_array.append(user_array[digit])

print (reversed_user_array)

