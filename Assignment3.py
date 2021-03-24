# Assignment Name: Procedures and Conditionals Assignment
# Question Number: 3
# 
# TODO: Create a program that takes the a, b, and c values of a 
# quadratic function (function as in mathematical function, not a 
# programming procedure). Create a function that returns the 
# discriminant given, along with whether the quadratic function has
#  zero roots, one root, or two roots. List the roots (if any)
#  by using the quadratic formula.

# date and time completed: 2021-03-12 7:46

import math

def check(variable, conversion, promptletter):
    '''The variable parameter takes in an already defined variable as
    an argument, the conversion parameter takes in a constructor
    function as an argument and the promptletter parameter takes
    in an alphabetical letter as an argument to be inputted into the
    string below. The check() function uses the try block to see whether
    the input is valid and if a ValueError occurs, it tells the user to
    re-input their response'''
    try:
        conversion(variable)
    except ValueError:
        print('Please put a valid number')
        variable = conversion(input(f'Type the {promptletter} value'))
    finally:
        return conversion(variable)

# Each of the following letter vairables take a seperate input from
# the user and is checked to see whether the input is valid or not,
# as explained above
a = input('Type the a value')
a = check(a, float, 'a')

b = input('Type the b value')
b = check(b, float, 'b')

c = input('Type the c value')
c = check(c, float, 'c')

# The discriminant variable calculates the discriminant of the 3 inputs
# above
discriminant = b ** 2 - 4 * a * c

def discriminants():
    '''Returns the distcriminant'''
    return (f'The discriminant is {discriminant}')

def rootnumber():
    '''Returns the number of roots of the quadratic function, using\
    the variables above'''
    if discriminant > 0:
        x = round(((-b) + math.sqrt(discriminant)) / (2 * a), 3)
        x1 = round(((-b) - math.sqrt(discriminant)) / (2 * a), 3)
        return (f'There are two roots: {x} and {x1}')
    elif discriminant == 0:
        x = round(((-b) + math.sqrt(discriminant)) / (2 * a), 3)
        return (f'There is 1 root: {x}')
    elif discriminant < 0:
        return (f'There are zero real roots')

# Prints the above functions
print(discriminants())
print(rootnumber())
