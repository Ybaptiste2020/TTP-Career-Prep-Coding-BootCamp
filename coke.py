'''
    implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
    Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
    Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

'''
coin = input("User Please insert a coin \n")  #Prompts the user for a coin.
amount_due = 50
change_owed = 0
total = amount_due - change_owed

while coin != "0":  #While the coin is not 0, the loop will continue.
    if coin == "5" or coin == "10" or coin == "25":  #If the coin is 5, 10, or 25, the loop will continue.
        amount_due - coin
        print("Amount Due: " + amount_due)  #Prints the amount due.
        #coin = input("User Please insert a coin \n")  #Prompts the user for a coin.
    else:  #If the coin is not 5, 10, or 25, the loop will continue.
        change_owed -= amount_due
        print("Change Owed: " + change_owed)  #Prints the amount due.
        
        #coin = input("User Please insert a coin \n")  #Prompts the user for a coin.
        
print("Change Owed: " + coin)  #Prints the amount of change owed.