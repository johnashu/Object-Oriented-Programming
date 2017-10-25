innnn = input()

def create_matrix(matrix_size):
    """ 
    A function that creates an N x N size 
    matrix based on an integer input
    """
    count = matrix_size
    matrix = []

    while count > 0:
        matrix_row = input("please enter a row of integers: ")
        if len(matrix_row) == matrix_size:
            matrix += [matrix_row]
            count -= 1
        else:
            print("please enter the correct number of integers for the row", matrix_size)
            continue
    return matrix

matrix_size_in = int(input("Enter the size of the matrix: "))

matrix_size = matrix_size_in

matrix1 = create_matrix(matrix_size)
print(matrix1)