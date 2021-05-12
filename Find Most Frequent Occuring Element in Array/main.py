# program to find the most frequent occuring item in an array

def mostFrequentElement(list):
    
    tempDict = {} # the dictionary will store all elements in given array along with their number of occurence
    maxCount = 0 # this variable stores the largest value (occurence) of an element in given array
    frequentItem = 0 # this variable stores the item having most number of occurences

    # element is added to dictionary if it already doesnt exist there
    # element's value (occurence) is incremented by 1 if it already exists there
    for element in list:
        if element not in tempDict:
            tempDict[element] = 1
        else:
            tempDict[element] = tempDict[element] + 1

    # check what is the largest value (occurence) for any key (element in given array)
    for element in tempDict:
        if(maxCount < tempDict[element]):
            maxCount = tempDict[element]
            frequentItem = element

    return frequentItem


simpleList = [1, 3, 4, 2, 3, 9, 6, 3, 4, 1, 9, 10, 5, 2, 5, 2, 7, 8, 6, 3, 9, 10, 1]

print(f"Most Freqquest Element: {mostFrequentElement(simpleList)}")