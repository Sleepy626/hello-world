# Assignment Name: Repetition Assignment
# Question Number: 1
# 
# TODO: Create a loop that calculates the 
# Fibonacci sequence of the first 25 numbers and 
# prints each one. Lastly, state the 25th and 24th 
# sequence in a sentence, and explain how the golden 
# ratio is conducted from it, including what it is.
# Note: you don’t know what the 24th and 25th number 
# are, get the program to find out and calculate itself 
# what the ratio is.

# date and time completed: 2021-03-23 9:29

# The two variables below are, by definition, the first 
# and second numbers of the fibonacci sequence. Note: 
# They are not printed as the first and second numbers 
# in the output, as that is not the desired outcome.
# Instead fibonnacci 2 is used as the number of each 
# term and fibonnacci 1 is used as the number of the
# previous term
fibonacci1 = 0
fibonacci2 = 1

# Prints the heading for the first 25 numbers of the
# fibonacci sequence
print('Below are the first 25 numbers of the fibonacci \
sequence:')

# For each number up to 25, prints the term in the sequence
# (fibonacci2). On the 25th term (the number in the range 
# would be 24), it prints the golden ratio.
for number in range(25):
    print(fibonacci2)
    nextNumber = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = nextNumber
    if number == 23:
        ratio = fibonacci2 / fibonacci1
        statement = (f'Below is the golden ratio caluclated from\
 the 25th term divided by the 24th term ({fibonacci2} divided by {fibonacci1}):')
    if number == 24:
        print(statement)
        print(f'{ratio:.3f}')



