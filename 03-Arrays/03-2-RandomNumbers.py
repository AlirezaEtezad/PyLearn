import random

Array = []
n = int(input("please enter a number: "))
for i in range (n):
    Array.append(random.randint(1,100))
print (Array)