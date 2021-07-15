# these are some practice questions that will help you to put to use what you learnt in sample code files from 0-3

"""
Question1: Using what you have learnt, write a function called 'distance_formula' which takes 2 tuples of the form (x1,y1) and (x2, y2) to calculate the euclidean distance between them.
call the function, and print the results.

Question2: Using a loop and the list given below, design a logic and write a my_min function to find the minimum number in the list. Write another function my_max to find the largest number
note: DO NOT USE the min max functions given by python. use a loop and variables to write your code.
"""

import random


def distance_formula(point1, point2):
    # your code
    return


def my_min(list_of_values):
    # your code
    least_num = 0
    return least_num


def my_max(list_of_values):
    # your code
    largest_num = 0
    return largest_num


# Q1
pt_1 = (10, 2)
pt_2 = (-14, 8)
print("Distance between pt_1 and pt_2 is: " + str(distance_formula(pt_1, pt_2)))

list_of_numbers = []
# this generates 20 random numbers
for i in range(20):
    list_of_numbers.append(random.randint(1, 100))
print(list_of_numbers)

print("Least number is: " + str(my_min(list_of_numbers)))
print("Largest number is: " + str(my_max(list_of_numbers)))

# write your code here
