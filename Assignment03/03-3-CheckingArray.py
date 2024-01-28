user_input = input("enter a list of numbers separated by ',': ")
user_array = [int(num) for num in user_input.split(",")]

if user_array == sorted(user_array):
    print("the array is in order")
else:
    
    print(" the correct order of array is:")
    print(sorted(user_array))