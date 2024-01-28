user_input = input("enter a list of numbers separated by ',': ")
user_array = [int(num) for num in user_input.split(",")]
unique_user_array = []

for i in user_array:
    if i not in unique_user_array:
        unique_user_array.append(i)

print (unique_user_array)