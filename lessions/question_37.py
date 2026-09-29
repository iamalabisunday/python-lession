# Write a Python Program to Add Two Matrices.

def matrices(rows, cols):
    if rows < 1 or cols < 1:
        return []
    
    matrix = []
    for i in range(rows):
        rows = []
        for j in range(cols):
            val = int(input(f"Enter value at ({i},{j}): "))
            rows.append(val)
        matrix.append(rows)
        
    return matrix

def add_matrices(matrix_1, matrix_2):
    result = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[0])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        result.append(row)
    return result
        
def print_matrix(matrix):
    for row in matrix:
        print(row)
    
while True:
    try:
        row = int(input("Enter the number of rows: "))
        col = int(input("Enter the number of columns: "))

        print("Enter values for Matrix 1:")
        matrix_1 = matrices(row, col)

        print("Enter values for Matrix 2:")
        matrix_2 = matrices(row, col)

        result = add_matrices(matrix_1, matrix_2)

        print("Result of addition:")
        print_matrix(result)
        
    except ValueError:
        print("Error: kindly check your code")
        
    again = input("Do you want to try again - y/n: ").lower().strip()
    if again != "y":
        break