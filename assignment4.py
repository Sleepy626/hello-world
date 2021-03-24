# Assignment Name: Procedures and Conditionals Assignment
# Question Number: 4
# 
# TODO: Create a program that calculates the amount of federal tax 
# you will have to pay depending on a given salary. Hint: The second 
# tax bracket does not mean you pay 20.5% on ALL of your income!

# date and time completed: 2021-03-12 7:46

def check(variable, conversion):
    '''The variable parameter takes in an already defined variable as an argument
    and the conversion parameter takes in a constructor function as an argument.
    The check() function uses the try block to see whether the input is valid and
    if a ValueError occurs, it tells the user to re-input their response'''
    try:
        conversion(variable)
    except ValueError:
        print('Please put a valid number')
        variable = conversion(input('Give a yearly salary'))
    finally:
        return conversion(variable)

# The salary variable asks the user to input their yearly salary and check to see
# whether it's a valid input
salary = input('yearly salary')
salary = check(salary, float)

# Prints the federal tax you'll have to pay within your tax bracket
if salary <= 48535:
    print(f'The amount of federal tax you will have to pay is {salary * 0.15:.2f} dollars')
elif 48535 < salary <= 97069:
    print(f'The amount of federal tax you will have to pay is \
{(48535 * 0.15) + ((salary - 48535) * 0.205):.2f} dollars')
elif 97069 < salary <= 150473:
    print(f'The amount of federal tax you will have to pay is \
{(48535 * 0.15) + (48534 * 0.205) + ((salary - 97069) * 0.26):.2f} dollars')
elif 150473 < salary <= 214368:
    print(f'The amount of federal tax you will have to pay is \
{(48535 * 0.15) + (48534 * 0.205) + (53404 * 0.26) + ((salary - 150473) * 0.29):.2f} dollars')
else:
    print(f'The amount of federal tax you will have to pay is \
{(48535 * 0.15) + (48534 * 0.205) + (53404 * 0.26) + (63895 * 0.29) + ((salary - 214368) * 0.33):.2f} dollars')