# Program to calculate Greatest Common Divisor for 2 given numbers.

# Using Eucliidean Algorithm to calculate GCD

def greatestCommonDivisor(num1, num2):

    assert num1 == int(num1) and num2 == int(num2), "Numbers should be integer"
    assert num1 >= 0 and num2 >= 0, "Invalid Values Entered"


    # Convert negative numbers into positve, if any, because GCD of negative numbers is same as that of positive numbers.
    if num1 < 0 or num2 < 0:
        num1 = abs(num1)
        num2 = abs(num2)

    # Base Condition
    if num2 == 0:
        return num1

    # Recursive Case
    return greatestCommonDivisor(num2, num1%num2)


number1 = 12
number2 = 8

print(f"GCD: {greatestCommonDivisor(number1, number2)}")