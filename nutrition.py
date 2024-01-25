'''
     a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of 
     calories in one portion of that fruit, per the FDA’s 
     poster for fruits, which is also available as text. Capitalization aside, 
     assume that users will input fruits exactly as written in the 
     poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
'''
#Prompts user for fruit of their choice to display to them the calories.
fruit = input("User please enter a fruit of your choice\n Then I will display the # of calories in that fruit.\n List of Fruits: \n Grapes\n Strawberries \n Apples \n Bananas \n Oranges \n Blueberries \n")

#If statements handling the user's input of type of fruit. 
if fruit.lower() == "strawberries":
    print("Strawberries have 50 calories per 100 grams.")
elif fruit.lower() == "apples":
    print("Apples have 95 calories per 100 grams.")
elif fruit.lower() == "bananas":
    print("Bananas have 105 calories per 100 grams.")
elif fruit.lower() == "oranges":
    print("Oranges have 45 calories per 100 grams.")
elif fruit.lower() == "grapes":
    print("Grapes have 37 calories per 100 grams.")
elif fruit.lower() == "blueberries":
    print("Blueberries have 60 calories per 100 grams.")
elif fruit.lower() == "blackberries":
    print("Blackberries have 70 calories per 100 grams.")

#If not any of the options below, will display error message.
else:
    print("Error: Not valid input")




