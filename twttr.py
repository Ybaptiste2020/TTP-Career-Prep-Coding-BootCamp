'''
    a program that prompts the user for a str of text and then outputs 
    that same text but with all vowels (A, E, I, O, and U) 
    omitted, whether inputted in uppercase or lowercase.
'''

text = input('User please input a string of text and I will basically \nshorten it with vowels such as: A,E,I,O,U \n')

text = text.lower() # variable holding the lowercase 
#for loop created to loop through the array of the 
#users string displaying only the vowels contained in that string.
for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        text = text.replace(i, '')

print(text)