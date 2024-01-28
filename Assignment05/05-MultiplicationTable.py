n = int(input("enter a number n: "))
m = int(input("enter a number m: "))


multiplication_table = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
    
for row in multiplication_table:
    print(row)