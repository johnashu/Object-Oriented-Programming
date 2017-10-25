# array = [1, 2, 3, 4, 5]

# value = int(input("input an Integer: "))

# array[0] = value
 
# print(array)

# # lists = [(u'a', 5), (u'b', 3), (u'c', 2), (u'd', 2), (u'e', 2), (u'f', 2), (u'g', 2), (u'h', 1), (u'i', 1)]

# # for k,v in lists:
# #     print('{} = {}'.format(k,v))

# # 1)The user is prompted to enter 5 integers and these integers are carried out by the program to print out.

# # ->The sum of all integers
# # ->The average
# # ->The sum off the squared integers
# # ->The sum off the cubed integers

# # The program shouldn't accept any negative values

# # int_list = []

# # #Take in 5 integers
# # while len(int_list) < 5:
# #     int_in = int(input("input integers "))
# #     int_list.append(int_in)
    
# # # ->The sum of all integers
# # sum_of_all = sum(int_list)

# # # ->The average
# # average = sum_of_all / len(int_list)

# # # ->The sum off the squared integers
# # squares = [(x ** 2) for x in int_list]
# # sum_of_squares = sum(squares)

# # # ->The sum off the cubed integers
# # cubes = [(x ** 3) for x in int_list]
# # sum_of_cubes = sum(cubes)

# # print(int_list)
# # print(sum_of_all)
# # print(average)
# # print(squares)
# # print(sum_of_squares)
# # print(cubes)
# # print(sum_of_cubes)

# # Challenge 3

# # Create a program that will prompt the user to play a coin toss game, this program should ask for the amount off flips the user wants and it should generate heads or tails until that constraint is reached.

# # Eg:

# # Enter number off flips=>5

# # Computer: heads, heads, tails,heads,tails.

# import random

# num_of_flips = int(input("enter number of coin tosses here: "))

# heads = 0
# tails = 0

# for x in range(num_of_flips):
#     flip = random.randint(0,1)
#     if flip == 0:
#         print('Heads')
#         heads += 1
#     else:
#         print('Tails')
#         tails += 1


# print("The total of Heads is {}".format(heads))
# print("The total of Tails is {}".format(tails))


# def fun(x):
#     if(x >100):
#         return x-10
#     else:
#         return fun(fun(x+11))

# print(fun(95))



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
    return matrix

matrix_size_in = int(input("Enter the size of the matrix: "))

matrix_size = matrix_size_in

matrix1 = create_matrix(matrix_size)
print('\n', matrix1, '\n')

matrix2 = create_matrix(matrix_size)
print(matrix2, '\n')

zero_list = '0' * matrix_size
empty_matrix = [[i for i in zero_list]] * matrix_size
#print(empty_matrix)

# 1. Sum of the matrices.

result_add = [[int(matrix1[i][j]) + int(matrix2[i][j])  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print('The result of adding the matrices is: \n')
for r in result_add:
    print(r)
print('\n')   

# 2. Difference between the matrices.

result_sub = [[int(matrix1[i][j]) - int(matrix2[i][j])  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print('The difference between the matrices is: \n')
for r in result_sub:
   print(r)
print('\n')   

result_mul = [[sum(int(a) * int(b) for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(* matrix2)] for matrix1_row in matrix1]

print('The difference between the matrices is: \n')
for r in result_mul:
   print(r)
print('\n')   