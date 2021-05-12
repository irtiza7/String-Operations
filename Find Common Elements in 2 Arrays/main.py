# program to find common elements from two given arrays 

def findCommonElements(fList, sList):
    
    commonElements = [] # list to store common elements from two arrays 

    # lenght of both array will be check to solve the problem in O(max(n, m)) 
    # where n = lenght of first array and m = lenght of second array
    # if lenght of first array is smaller, then we compare its each element with second array
    # and vice versa 
    # we also check if the element is already in our commonElements array so we can avoid repeatition of elements
    if len(fList) < len(sList):
        for element in fList:
            if element in sList and element not in commonElements:
                commonElements.append(element)
    else:
        for element in sList:
            if element in fList and element not in commonElements:
                commonElements.append(element)

    
    return commonElements


fList = [1,9,8,1,2,5,6]
sList = [1,2,3,5,4,6]

print(f"Common Elements: {findCommonElements(fList, sList)}")