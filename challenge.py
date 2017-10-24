array = [1, 2, 3, 4, 5]

value = int(input("input an Integer: "))

array[0] = value
 
print(array)

# lists = [(u'a', 5), (u'b', 3), (u'c', 2), (u'd', 2), (u'e', 2), (u'f', 2), (u'g', 2), (u'h', 1), (u'i', 1)]

# for k,v in lists:
#     print('{} = {}'.format(k,v))

# 1)The user is prompted to enter 5 integers and these integers are carried out by the program to print out.

# ->The sum of all integers
# ->The average
# ->The sum off the squared integers
# ->The sum off the cubed integers

# The program shouldn't accept any negative values

# int_list = []

# #Take in 5 integers
# while len(int_list) < 5:
#     int_in = int(input("input integers "))
#     int_list.append(int_in)
    
# # ->The sum of all integers
# sum_of_all = sum(int_list)

# # ->The average
# average = sum_of_all / len(int_list)

# # ->The sum off the squared integers
# squares = [(x ** 2) for x in int_list]
# sum_of_squares = sum(squares)

# # ->The sum off the cubed integers
# cubes = [(x ** 3) for x in int_list]
# sum_of_cubes = sum(cubes)

# print(int_list)
# print(sum_of_all)
# print(average)
# print(squares)
# print(sum_of_squares)
# print(cubes)
# print(sum_of_cubes)

# Challenge 3

# Create a program that will prompt the user to play a coin toss game, this program should ask for the amount off flips the user wants and it should generate heads or tails until that constraint is reached.

# Eg:

# Enter number off flips=>5

# Computer: heads, heads, tails,heads,tails.

import random

num_of_flips = int(input("enter number of coin tosses here: "))

heads = 0
tails = 0

for x in range(num_of_flips):
    flip = random.randint(0,1)
    if flip == 0:
        print('Heads')
        heads += 1
    else:
        print('Tails')
        tails += 1


print("The total of Heads is {}".format(heads))
print("The total of Tails is {}".format(tails))


def fun(x):
    if(x >100):
        return x-10
    else:
        return fun(fun(x+11))

print(fun(95))