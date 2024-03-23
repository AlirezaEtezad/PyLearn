def khayyam_pascal_triangle(n):
    triangle = []
    
    for i in range(n):
        row = [1]
        
        if i > 0:
            prev_row = triangle[i-1]
            
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
                
        row.append(1)
        triangle.append(row)
        
    return triangle

n = int(input("Enter the number of rows: "))
triangle = khayyam_pascal_triangle(n)

for row in triangle:
    print(row)