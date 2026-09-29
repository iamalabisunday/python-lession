# Write a Python Program to Multiply Two Matrices.

def matrices(rows, cols):
    if rows < 0 or cols < 0:
        return []
    
    matrix = []
    for i in range(rows):
        rows = []
        for j in range(cols):
            val = int(input(f"Enter value at {i}{j}: "))
            rows.append(val)
        matrix.append(rows)
    return matrix

def multiply_matrices(matrix_1, matrix_2):

    result = []
    for m1 in range(len(matrix_1)):
        matrix = []
        for m2 in range(len(matrix_1[0])):
            val = matrix_1[m1][m1] * matrix_2[m1][m1] 
            matrix.append(val)
        result.append(matrix)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

while True:
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of cols: "))

        print("Enter the value for matrice_1")
        matrix_1 = matrices(rows, cols)

        print("Enter the value for matrice_2")
        matrix_2 = matrices(rows, cols)

        result = multiply_matrices(matrix_1, matrix_2)
        print_matrix(result)

    except ValueError:
        print("Error")

    again = input("Do you want to try again - y/n: ").lower()
    if again != "y":
        break