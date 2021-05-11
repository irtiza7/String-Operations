#   OPTIMIZED SOLUTION ( ( O(n) ) ) .........................................

def findRecurringChar(string):
    cList = []

    for char in string:

        if(char in cList):
            return char
        else:
            cList.append(char)



string = "abcdabcdef"
print(findRecurringChar(string))


#   NON OPTIMIZED SOLUTION ( O(n^2) ) .........................................

# def findNonRecurringChar(string):
#     charList = []
#     count = 0

#     for character in string:
#         charList.append(character)

#     for character in string:
#         count = 0

#         for element in charList:
#             if(character == element):
#                 count += 1
        
#         if count > 1:
#             return character


# string2 = "Noor"

# print(f"Recurring Character: {findNonRecurringChar(string2)}")

# #print(f"Non Recurring Character: {findNonRecurringChar(string)}")
