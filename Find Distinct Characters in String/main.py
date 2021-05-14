# Program to find all distinct characters in a given string.

def findDistinctChars(string):
    
    countDict = {} # dictionary to stores characters while iterating along with their occurrences.
    distinctChars = [] # list to store characters which have only single occurence.

    
    # storing characters in countDict along with their occurrence. 
    for char in string:

        # IF: the character is not already in dictionary then it means it hasn't occured yet. So store it with its occurrence equal to 1.
        # ELSE: the character is already in countDict then it must have occured before. So increment its previous occurrence with 1.
        if char not in countDict:
            countDict[char] = 1
        else:
            countDict[char] = countDict[char] + 1

    
    # append the character to distinceChars if its occurrence is equal to 1 i.e. it has occurred only once in given array.
    for item in countDict:
        if countDict[item] == 1:
            distinctChars.append(item)
    

    return distinctChars

testString1 = "apples"
testString2 = "characters"

print(f"Distinct Characters in |{testString1}|: {findDistinctChars(testString1)}")
print()

print(f"Distinct Characters in |{testString2}|: {findDistinctChars(testString2)}")