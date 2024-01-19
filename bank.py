"""
    a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
    If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
    Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

"""

def greeting():
    greet = input('Please enter a greeting\n')

    #if statement using the 'or' logical operator to compare how the user enters the word hello.
    if greet == "hello" or greet == "Hello" or greet == "HELLO":
        print("$0")

    #elif statement to compare the first element of the greeting if the string begins with h but not the word hello.
    #eg. holiday or help should output $20
    elif greet[0] == "h" and greet != "hello":
        print("$20")

    #otherwise print out $100.
    else:
        print("$100") 

#function call to get things running.
print(greeting())
