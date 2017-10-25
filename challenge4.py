# Challenge 4

# So you need to take two 2-D Array of equal rows and columns (say 3 or 4) from the user and print the following:
# 1. Sum of the matrices.
# 2. Difference between the matrices.
# And only if possible,
# 3. Product of the matrices.

# Please note that the array should be printed in a proper format i.e.
 
# 1  8  7
# 5  9  6
# 2  0  1

# The code will get lengthy so it will be amazing if you guys could send the code in a txt file. That will make it easier to account.

# code to add n matrices, return the differences
# and if possible the product of the matrices


# Pre steps, Create Matrices..

def create_matrix(matrix_size):
    """ 
    A function that creates an N x N size 
    matrix based on an integer input
    """
    count = matrix_size
    row_num = matrix_size
    matrix = []

    while count > 0:
        matrix_row = [int(x) for x in input('Please enter a row of integers, put a space between each: ').split()]
        if len(matrix_row) == matrix_size:
            matrix += [matrix_row]
            count -= 1
            row_num -= 1
        else:
            print("please enter the correct number of integers for the row", matrix_size)
            continue
    print('\n')
    return matrix 

matrix_size_in = int(input("Enter the size of the matrix: "))
print('\n')

matrix_size = matrix_size_in

matrix1 = create_matrix(matrix_size)
for r in matrix1:
    print('{:>15}'.format(*r))
print('\n')

matrix2 = create_matrix(matrix_size)
for r in matrix2:
    print('{:>15}'.format(*r))
print('\n')

zero_list = '0' * matrix_size
empty_matrix = [[i for i in zero_list]] * matrix_size
#print(empty_matrix)

# 1. Sum of the matrices.

result_add = [[int(matrix1[i][j]) + int(matrix2[i][j])  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print('The result of adding the matrices is: \n')
for r in result_add:
    print('{:>15}'.format(*r))
    #print(r)
print('\n')   

# 2. Difference between the matrices.

result_sub = [[int(matrix1[i][j]) - int(matrix2[i][j])  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print('The difference between the matrices is: \n')
for r in result_sub:
    print('{:>15}'.format(*r))
    #print(r)
print('\n')   

result_mul = [[sum(int(a) * int(b) for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(* matrix2)] for matrix1_row in matrix1]

print('The product of the matrices is: \n')
for r in result_mul:
    #print(r)
    print('{:>15}'.format(*r))
print('\n')   