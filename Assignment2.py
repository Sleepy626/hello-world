# Assignment Name: Procedures and Conditionals Assignment
# Question Number: 2
# 
# TODO: Create a program that takes three lengths and 
# determines if it can form a valid triangle. If it can, 
# then indicate what kind of triangle it can make. 
# Lastly, have a function that takes in the dimensions 
# and returns the area to be printed.

# date and time completed: 2021-03-12 7:46

import math

def check(variable, conversion, promptnumber):
    '''The variable parameter takes in an already defined variable as
    an argument, the conversion parameter takes in a constructor
    function as an argument and the promptnumber parameter takes
    in an ordinal number as an argument to be inputted into the
    string below. The check() function uses the try block to see whether
    the input is valid and if a ValueError occurs, it tells the user to
    re-input their response'''
    try:
        conversion(variable)
    except ValueError:
        print('Please put a valid number')
        variable = conversion(input(f'Input the number you want the\
{promptnumber} length to be'))
    finally:
        return conversion(variable)

# Each of the following length vairables take a seperate input from
# the user for each triangle length and is checked to see whether the
# input is valid or not, as explained above
length1 = input('Input the number you want the first length to be ')
length1 = check(length1, float, 'first')

length2 = input('Input the number you want the second length to be ')
length2 = check(length2, float, 'second')

length3 = input('Input the number you want the third length to be ')
length3 = check(length3, float, 'third')

def triangle():
    '''The triangle() function first checks to see if the three lengths
    can form a valid triangle. If they can then it checks to see what
    type of triangle it can make and prints the answer. If not, the else
    statment prints 'Your lengths cannot make a triangle. Re-run the code
    if you want to try again'.'''
    if (length1 + length2 > length3) and (length1 + length3 > length2) and \
        (length3 + length2 > length1):
        if length1 == length2 == length3:
            return True, 'Your lengths can make an equilateral triangle.'
        elif length1 == length2 or length1 == length3 or length3 == length2:
            return True, 'Your lengths can make an isosceles triangle.'
        else:
            return True, 'Your lengths can make a scalene triangle.'
    else:
        return False, 'Your lengths cannot make a triangle. Re-run the code if you want\
to try again.'

# unpacks the retrun values above
unpackTriangle, unpackType = triangle()

def area():
    '''Returns the area of the triangle made with the three lengths taken from the user'''
    if unpackTriangle == True:
        perimeter = (length1 + length2 + length3) / 2
        return f'The area of your triangle is \
{round(math.sqrt(perimeter * (perimeter - length1) * (perimeter - length2) * (perimeter - length3)), 3)}'
    else:
        return 'Area cannot be calculated'

print(unpackType, area()) # Prints the functions above