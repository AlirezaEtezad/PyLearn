a= int(input("please enter 1st side: "))
b= int(input("pleas enter 2nd side: "))
c= int(input("please enter 3rd side: "))

if  a < b + c and b < c + a and c < a + b:
    print ("this triangle is possible")

else:
    print("this triangle is impossible")