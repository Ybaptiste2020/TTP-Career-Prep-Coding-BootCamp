'''
Write a function that takes 2 string parameters (arguments). Return an array of all the letters that are present in both strings. 
You can assume both strings only contain lowercase letters. The strings can be of any size.
If a letter appears multiple times in the input, it should appear only once in the output.

'''

'''def letters(yashadii, baptiste):

    #Nested for loop for an iterater for both strings.
    for i in yashadii:
        for j in baptiste:
            if yashadii[i] == baptiste[j]:
        return [i][j]
print(letters("happy","days"))
'''

#second attempt
def letters(yashadii, baptiste):
    #Empty list to store the common letters.
    common_letters = []
    #Nested for loop for an iterater for both strings.
    for i in yashadii:
        for j in baptiste:
            if i == j:
                common_letters.append(i)
    return common_letters
print(letters("happy","days"))

