# Program to check if a string exists in another string.

def isSubstring(str1, str2):

    # Base Case: if length of any string is o then we cant compare them
    if len(str1) == 0 or len(str2) == 0:
        return False

    # Base Case: if the strings passed are single character long, and the characters of both string aren't same then return false.
    if (len(str1) == 1 or len(str2) == 1) and (str1[0] != str2):
        return False

    # Base Case: if the strings passed are single character long, and the characters of both string are same then return true.
    if (len(str1) == 1 or len(str2) == 1) and (str1[0] == str2):
        return True


    # Check if characters match, if so then pass the next characters to the recursive function
    if str1[0] == str2[0]:

        #Recursive Case if there is a match in characters of both strings
        if isSubstring(str1[1:], str2[1:]):
            return True

    # Recursive Case
    return isSubstring(str1[1:], str2)


str1 = "importantance"
str2 = "ant"

print(isSubstring(str1, str2))