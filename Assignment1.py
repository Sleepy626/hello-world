# Assignment Name: Procedures and Conditionals Assignment
# Question Number: 1
# 
# TODO: Create a program that checks to see whether a given
#  year is a leap year.

# date and time completed: 2021-03-12 7:46

def check(variable, conversion):
    '''The variable parameter takes in an already defined variable as
    an argument and the conversion parameter takes in a constructor
    function as an argument. The check() function uses the try block to
    checks to see whether the input is a valid input and if a ValueError
    occurs, it tells the user to re-input their response'''
    try:
        conversion(variable)
    except ValueError:
        print('Please put a valid number')
        variable = conversion(input('Give a year'))
    finally:
        return conversion(variable)

# The year vairable takes an input from the user and is checked to see
# whether the input is valid or not, as explained above
year = input('Give a year')
year = check(year, int)

# Prints 'Leap year!' if the unser input is a leap year and 'Not a leap year'
# if not
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Leap year!')
else:
    print('Not a leap year!')
