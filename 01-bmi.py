h=float(input("please enter your height in meter: "))
w=float(input("please enter your weight in Kilogram: "))
bmi=w/h**2
if bmi<18.5 :
    status="underwiehgt"
elif 18.5<=bmi<25 :
    status="normal"
elif 25<=bmi<30:
    status="overweight"
elif 30<=bmi<35 :
    status="ebesity"
else:
    status="extreme obesity"
print ("your status is: " + (status))