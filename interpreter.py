'''
a program that prompts the user for an arithmetic expression and then calculates and 
outputs the result as a floating-point value 
formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and 
one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

'''
#First attempt
'''def expression():
    arithmetic_expression = input("User please give me an arithmetic expression\n") #Prompts user for expression
    result = float(arithmetic_expression)   #stores the users expression as a float to be able to return a float-point value as requested.
    x = int() 
    z = int()
    y = '+' , '-', '*', '/'

    result = x(z(y))
    print(float(result))

print(expression())
'''

#second attempt
arithmetic_expression = input("User please give me an arithmetic expression\n")  # Prompts user for expression

# Split the input expression using the space as a delimiter
tokens = arithmetic_expression.split()

# Assuming the input format is always as specified: x y z
try:
    x = float(tokens[0])  # Convert the first token to a floating-point number
    operator = tokens[1]  # Get the operator
    z = float(tokens[2])  # Convert the third token to a floating-point number

    # Perform the calculation based on the operator
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z != 0:  # Ensure that z is not zero for division
            result = x / z
        else:
            print("Error: Division by zero")
            exit()
    else:
        print("Invalid operator")
        exit()

    # Output the result as a floating-point value to one decimal place
    print("Result: {:.1f}".format(result))

except (IndexError, ValueError):
    print("Invalid input format. Please provide an arithmetic expression in the format 'x y z'.")


