'''
    a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting 
    Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''

#check if users input is 42 forty-two or forty two 
def forty_two():
    prompt = input('Enter a number between 40 and 50 and I will print out \"Yes\" if the number is correct else \"No\" \n')
    #number = int(prompt)

    if prompt == "42":
        return "Yes"
    
    elif prompt == "forty-two":  #Both elif checks for case-insensitively just in case user dont enter an exact number.
        return "Yes"

    elif prompt == "forty two":
        return "Yes"   

    else:    #Else will return no if anything other than 42 forty-two or forty two was entered.
        return "NO"
    
print(forty_two())

