number = int(input("please enter a number: " ))
factorial = 1
for i in range (1, number+1):
    factorial = factorial * i
    if factorial == number :
        print ("yes")
        break
    elif factorial > number:
        print("No")
        break