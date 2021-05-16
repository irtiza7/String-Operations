# Program to print a string in reverse order using Recusion.

def printReverse(string):

    # Base Case: if the lenght of given string is 0 then it means
    # empty string has been passed.
    if len(string) == 0:
        return "Reverse: "

    # Recusive Case
    return printReverse(string[1:]) + string[0]


def main():

    string = "abcdefg"
    print(printReverse(string))


if __name__ == '__main__':
    
    main()