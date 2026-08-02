# 2D array Metrix :
# What is a 2D Array?
# 2D Array matlab List ke andar List.

matrix  = [
    [ 2 , 2, 3 ],
    [ 4 , 5, 6 ],    # Rows = 3 and columns = 3
    [ 7 , 8, 9 ]
]

# metrix[row][column]

print(matrix[0][0])
print(matrix[1][2])  
print(matrix[2][2])

# Row Print
print(matrix[0])
print(matrix[1])
print(matrix[2])

# Traverse Matrix
for row in matrix:
    for value in row:
        print(value, end=" ")

# using index :
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print() # for new line after each row
    