# Assignment Name: Repetition Assignment
# Question Number: 3
# 
# TODO: Create a program that uses a loop to 
# provide a k 𝖷 k times table similar to the 
# one below. You do not need to include lines 
# (borders), but try to use the \t keyword or 
# center string method in your string to clean
#  the table up.

# date and time completed: 2021-03-23 9:24
def check():
    '''While True, asks the user for a k value
for the k x k times table. The check() function
then uses the try block to see if the input is
valid, meaning no ValueError occuring and k > 0
and k <= 10. If not, continues looping until a
valid value is inputted.'''
    while True:
        k = input('Please input a k value for your times table between 1 and 10: ')
        try:
            k = int(k)
            if not 0 < k <= 10:
                raise ValueError
        except ValueError:
            print('Please put a valid number')
        else:
            return int(k)

# the variableChecked variable is the same as the 
# k variable above, but checked with the check()
# function 
variableChecked = check()

# Prints a timetable by multiplying each number
# in each range per iteration
for i in range(1, variableChecked + 1):
    for j in range(1, variableChecked + 1):
        print(i * j, end = '\t')
    print()