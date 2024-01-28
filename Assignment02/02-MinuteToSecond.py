

while True:

    choice = int(input("if ypu want to change time to sesonds enter '1' and if you want to change seconds to time enter '2' :"))
    if choice == 1 :
        time = input("please enter the time in the format 'HH:MM:SS' ")
        time_parts = time.split(":")

        H = int(time_parts[0])
        M = int(time_parts[1])
        S = int(time_parts[2])

        TotalSeconds = H * 3600 + M * 60 + S
        print("It is totally ",TotalSeconds," seconds.")



    elif choice == 2 :
        Seconds = int(input ("please enter seconds: "))

        H = Seconds // 3600
        M = (Seconds % 3600) // 60
        S = Seconds % 60

        print (H , ":" , M , ":", S )
    else:
        continue