name=input("enter your name: ")
family=input("enter your family: ")
a=float(input("enter 1st score: "))
b=float(input("enter 2nd score: "))
c=float(input("enter 3rd score: "))

average=(a+b+c)/3
if average>=17:
    print( (name)+" "+(family)+ " your average is " + str(average) + " and you are a top student")
elif 17>average>=12 :
    print(( (name)+" "+(family)+ " your average is " + str(average) + " and you are a normal student"))
else:
    print(( (name)+" "+(family)+ " your average is " + str(average) + " and you are failed"))