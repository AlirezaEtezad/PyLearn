n = int(input("enter a number n: "))
m = int(input("enter a number m: "))

for j in range (1, m+1):
    if j % 2 == 0:
        if n % 2 == 0:
            for i in range (1, n//2+1):
                print("*#", end ="")
            print("")
        else:
            for i in range (1, n//2+1):
                print("*#",end = "")
            print("*")
    else:
        if n % 2 == 0:
            for i in range (1, n//2+1):
                print("#*", end ="")
            print("")
        else:
            for i in range (1, n//2+1):
                print("#*",end = "")
            print("#")