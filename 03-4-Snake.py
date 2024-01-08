n = int(input("enter a number: "))
if n % 2 == 0:
    for i in range (1, n//2+1):
        print("*#", end ="")
else:
    for i in range (1, n//2+1):
        print("*#",end = "")
    print("*")