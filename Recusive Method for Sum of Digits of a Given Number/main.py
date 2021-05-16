# Program to print the sum of all the digits in a given number.

def sumOfDigits(number):

    # Base Case: if the number is only a single digit return that number
    if len(str(number)) == 1:
        return number

    temp = len(str(number)) # temp stores the length of the number given
    divisor = 10 # divisor will be used to separate each digit of number

    # convert divisor into a factor of 10 based on the length of number
    # for example: for 238 the divisor should be 100 and for 12 it should be 10
    for i in range(0, temp-2):
        divisor = divisor * 10

    # Recursuve Case
    return  (number//divisor) + sumOfDigits(number%divisor)

number = 55512

print(sumOfDigits(number))