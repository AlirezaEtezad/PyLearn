n = int(input("please enter the size of the diamon: "))
def print_diamond(size):
    if size % 2 == 0:
        size += 1
    
    for i in range(size):
        spaces = abs((size-1)//2 - i)
        stars = size - 2 * spaces
        print(' ' * spaces + '*' * stars)

        
print_diamond(n)