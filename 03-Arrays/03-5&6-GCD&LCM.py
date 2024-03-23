

while True:
    try:

        first_number = int(input("please enter 1st number: "))
        break
    except ValueError:
        print("you can only enter integer ")

while True:
    try:
        second_number = int(input("p'lease enter 2nd number: "))
        break
    except ValueError:
        print("you can only enter integer ")

while True:

    entrance = input("Choose 'LCM' or 'GCD': ").lower() #LCM: Least Common Multiple, GCD: Greatest Common Divisor
    if entrance == "gcd" :
        break
    elif entrance == "lcm" :
        break
 
first_number_divisors = []
second_number_divisors = []
GCD_found = False


for i in range (1, first_number+1):
    if first_number % i == 0:
        first_number_divisors.append(i)

for i in range (1, second_number+1):
    if second_number % i == 0:
        second_number_divisors.append(i)        
        
for n in range(len(second_number_divisors)-1 , -1, -1):
    temp2 = second_number_divisors[n]
    for m in range(len(first_number_divisors)-1 , -1, -1):
        temp1 = first_number_divisors[m]
        if temp1 == temp2:
            GCD = temp1
            GCD_found = True
            break

    if GCD_found == True:
        break


if entrance == "gcd":
    print("The 'GCD' of ",first_number ,"and ", second_number, "is: ", GCD)
elif entrance == "lcm":
    print("The 'LCM' of ", first_number, "and ", second_number, "is: ",int(first_number * second_number / GCD))