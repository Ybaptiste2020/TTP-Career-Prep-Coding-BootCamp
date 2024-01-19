'''
    a program that prompts the user for the name of a file and then outputs that file’s 
    media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

'''

import mimetypes

#First attempt
'''def media_type(fileName):
    suffixes = ['.zip', '.txt', '.pdf', '.png','.jpeg' , '.jpg', '.gif']

    #Below checks if file name ends with any of the suffixes in the above
    #initialized array.

    for suffix in suffixes:
        if fileName.lower().endswith(suffix):

            #Use mimetypes to retrieve media type.
            try:
                media_type, encoding = mimetypes.guess_type(fileName)
                return media_type
            except:
                return "Unsupported File Type"

file = input("Enter the name of the file\n")  #Requesting the name of file from user.

#Obtain and print out the media type.
media_type = get_media_type(file)
print("Media Type: ", media_type)
'''

#Second attempt

suffixes = ['.zip', '.txt', '.pdf', '.png', '.jpeg', '.jpg', '.gif']

file = input('Enter the name of a file \n')
fileName = file.lower()

for extention in suffixes:
    try:
        if fileName.endswith(extention):
            print("Extension: ", extention)
    except NameError:
        pass
    else:
        print("application/octet-stream")
        
