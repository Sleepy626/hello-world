# Assignment Name: Repetition Assignment
# Question Number: 4
# 
# TODO: You have been asked to take a small icon
#  that appears on the screen of a smart telephone 
# and scale it up so it looks bigger on a regular 
# computer screen.
# The icon will be encoded as characters (x and *) 
# in a 3 x 3 grid as follows:
# *X*
#  XX
# * *
# Write a program that accepts a positive integer 
# scaling factor and outputs the scaled icon. A 
# scaling factor of k means that each character 
# is replaced by a k 𝖷 k grid consisting only of
#  that character.

# date and time completed: 2021-03-23 9:26

def check():
    '''While True, asks the user for a scaling size.
The check() function then uses the try block to see if
the input is valid, meaning no ValueError occuring and
scale > 0 and scale <= 10. If not, continues looping
until a valid value is inputted.'''
    while True:
        scale = input('Input a scaling size between 1 and 10: ')
        try:
            scale = int(scale)
            if not 0 < scale <= 10:
                raise ValueError
        except ValueError:
            print('Please put a valid number')
        else:
            return int(scale)

# scaleChecked is the same as the scale variable above,
#  but checked with the check() function 
scaleChecked = check()

# Prints the pre existing icon below and in the
# user's chosen size determined by the scale
# variable above
for i in range(scaleChecked):
    print('*' * scaleChecked, end = '')
    print('X' * scaleChecked, end = '')
    print('*' * scaleChecked)
for j in range(scaleChecked):
    print(' ' * scaleChecked, end = '')
    print('X' * scaleChecked, end = '')
    print('X' * scaleChecked)
for x in range(scaleChecked):
    print('*' * scaleChecked, end = '')
    print(' ' * scaleChecked, end = '')
    print('*' * scaleChecked)