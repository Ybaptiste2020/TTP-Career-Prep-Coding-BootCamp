'''
     a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
     Assume that the user’s input will indeed be in camel case.

'''
#a variable that has the input function stored in it that prompts the user for a camel case variable.
camel_case = input('User please enter a word in camel case: eg.(firstName, skateBoard)\n where the first letter of the first word is lowercase and the first letter in the second\n word is uppercase and I will convert the word to snake case.\n')

snake_case = '' #empty dictionary to store the string in snake case.

#use of for loop to loop through the array of strings 
#to place an underscore between the two words and 
#lowercase the first letter in the second word. 
for letter in camel_case:
    if letter.isupper():
        snake_case += '_' + letter.lower()
    else:
        snake_case += letter
print(snake_case)