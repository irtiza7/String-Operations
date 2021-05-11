def findLongestWord(wordsList):
    longestWord = ""

    for word in wordsList:

        temp1 = []
        temp2 = []
        
        for char in word:
            temp1.append(char)

        for char in longestWord:
            temp2.append(char)
        
        if(len(temp2) <= len(temp1)):
            longestWord = word
    
    return longestWord


words = ["important", "is", "their", "elephants", "oblivious", "cheems", "extraordinary", "expeliarmus", "luminous"]

print(f"Longest Word: {findLongestWord(words)}")
