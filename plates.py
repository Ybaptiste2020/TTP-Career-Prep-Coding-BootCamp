'''
“All vanity plates must start with at least two letters.” “… vanity plates may contain a maximum of 6 characters (letters or numbers) 
and a minimum of 2 characters.” “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would 
be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.” “No periods, spaces, or
 punctuation marks are allowed.” In plates.py, implement a program that prompts the user for a vanity plate and then output 
 Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. 
 Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
 Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

'''

'''
First Attempt
#Prompts user for a vanity plate.
vanity_plate = input('User please enter a Vanity Plate \n and I will validate if it is a \n correct one or not: \n')

def valid_vanity():
    if len(vanity_plate) >= 2 and len(vanity_plate) <= 6:
  #Checks if the first two characters are letters.
        if vanity_plate == isalpha():
    
    #else:
       # print("Invalid Vanity Plate")
       '''


#Second attempt
#A function to handle the validaty of the vanity plate.
def is_valid(s):
    if has_valid_length(s) and starts_with_letters(s) and no_middle_numbers(s) and no_invalid_characters(s):
        return True
    else:
        return False

#A function taking care of how long the numbers / letters should be.
def has_valid_length(s):
    return 2 <= len(s) <= 6

#A function dealing with what the vanity plate starts with.
def starts_with_letters(s):
    return s[:2].isalpha()

#A function dealing with the middle of the plate.
def no_middle_numbers(s):
    if len(s) > 2:
        return not any(char.isdigit() for char in s[1:-1])
    else:
        return True

#A function dealing with what maybe wrong with the plate number.
def no_invalid_characters(s):
    return all(char.isalnum() and char.isalpha() or char.isdigit() for char in s)

#Main function prompting the user for a vanity plate number and processing if 
#its correct or not based on using the programmer's defined functions.
def main():
    user_input = input("Enter a vanity plate: ")
    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
