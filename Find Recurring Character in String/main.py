# Program to find a recurring charater in a string.

def findRecurringChar(string):

    cList = [] # Characters List to store characters while iterating given string

    # Iterate each character in given string.
    # If the character doesn't exist in 
    for char in string:

        # IF: The character read is already in cList then it means it has multiple occurences.
        # ELSE: If the character read is not in cList then it means it has occured for the first time.  
        if(char in cList):
            return char
        else:
            cList.append(char)



string = "abcdabcdef"

print(findRecurringChar(string))