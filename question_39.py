# Write a Python Program to Transpose a Matrix.

def transpose_matrix(rows, cols):
    if rows < 0 or cols < 0:
        return [], []

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter the value of {i},{j}: "))
            row.append(val)
        matrix.append(row)

    transpose_matrix = []
    for k in range(cols):
        transpose_row = []
        for l in range(rows):
            transpose_row.append(matrix[l][k])
        transpose_matrix.append(transpose_row)


    return matrix, transpose_matrix

while True:
    try:
        rows = int(input("Enter the numbers of rows: "))
        cols = int(input("Enter the numbers of cols: "))

        matrix, transpose_matrix = transpose_matrix(rows, cols)

        print("-------Answer--------------------------")
        print("Original matrix")
        for row in matrix:
            print(row)

        print("Transpose matrix")
        for row in transpose_matrix:
            print(row)
        print("---------------------------------------")

    except ValueError:
        print("Invalid input! Please enter integer values.")

    again = input("Do you want to try it again, y/n: ").strip().lower()
    if again != "y":
        break