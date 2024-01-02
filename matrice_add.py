# Function to add two matrices
def add_matrices(matrix1, matrix2):
    result_matrix = []

    # Check if the matrices have the same dimensions
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)):
            row_result = []
            for j in range(len(matrix1[0])):
                # Sum the corresponding elements of the two matrices
                row_result.append(matrix1[i][j] + matrix2[i][j])
            result_matrix.append(row_result)

        return result_matrix
    else:
        return None  # Return None if matrices have different dimensions

# Input matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Add matrices
result = add_matrices(matrix_a, matrix_b)

# Display the result
if result:
    print("Matrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nSum of Matrices A and B:")
    for row in result:
        print(row)
else:
    print("Matrices have different dimensions. Addition not possible.")
