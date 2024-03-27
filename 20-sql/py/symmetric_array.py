user_input = input("enter a list of numbers separated by ',': ")
user_array = [int(num) for num in user_input.split(",")]
reveresd_array = list(reversed(user_array))
# print (user_array)
# print (reveresd_array)
if user_array == reveresd_array :
    print("YES, This is a symmetric Array")
else:
    print("NO, it is not a symmetric Array")
