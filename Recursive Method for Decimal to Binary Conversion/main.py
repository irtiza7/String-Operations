# Program to convert a positive decimal number into binary number.

def decimalToBinary(num):

    assert num >= 0, "Number is not a Positive Decimal Number"

    # Binary of decimal 0 is also 0
    if num == 0:
        return 0

    # Base Case: if num 1 then return 1 because 1 can not be divided by 2
    if num == 1:
        return num

    # Recusive Case
    return int(str(decimalToBinary(num//2)) + str(num%2))



for deciNumber in range(11):

    print(decimalToBinary(deciNumber))