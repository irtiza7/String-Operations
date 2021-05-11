#   program to check if letters "a" and "b" have exactly 3 letter distance between them

def checkAB(string):

    for character in string:
        index1 = string.index(character)
        index2 = index1 + 4

        if(string[index1] == "a" and string[index2] == "b"):
            return "True"
    
    return "False"



string1 = "ajkdblsdiklabksdlblsdbab"
string2 = "adbalkdbaldb"

print(checkAB(string1))
print(checkAB(string2))