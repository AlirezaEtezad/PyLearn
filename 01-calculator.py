import math

op= input("please choose an operation +,-,*,/,fac,log,sqrt or if you want to enter a degree choose: sin,cos,tan,cot,: ")

if op=="+" or op=="-" or op=="*" or op=="/" :
    a= float(input("enter 1st number: "))
    b= float(input("enter 2nd number: "))

elif op=="sqrt" or op=="fac" or op=="log":
    a= float(input("enter a number: "))

else:
    a= float(input("enter a degree: "))
    a= math.radians(a)
    

if op =="+":
    result= a+b
elif op =="-":
    result= a-b

elif op=="*":
    result= a*b

elif op=="/":
    if b==0:
        result="cannot divide by 0"
    else:
        result= a/b
elif op=="sin":
    result= math.sin(a)
elif op== "log":
    result= math.log(a)
elif op=="cos":
    result= math.cos(a)
elif op=="tan":
    result= math.tan(a)
elif op=="cot":
    result= 1/math.tan(a)
elif op=="fac":
    result= math.factorial(a)
elif op=="sqrt":
    result= math.sqrt(a)


print(result)