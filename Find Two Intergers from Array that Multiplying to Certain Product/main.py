# find two integers from an array which multiple to a certain product

# OPTIMIZED SOLUTION O(n)

def func(intList, product):

  for i in intList:
    
    temp = product/i

    if temp in intList:
      
      print(f"Numbers are {i} and {int(temp)}")
      return None

# NON OPTIMIZED SOLUTION O(n^2)
# def func(intList, product):

#   for i in range(len(intList)):

#     j = i + 1

#     for j in range(j, len(intList)):

#       if((intList[i] * intList[j]) == product):

#         print(f"Numbers are {intList[i]} and {intList[j]}")

intList = [1, 4, 7, 2, -6, 8, 6]
product = 24

func(intList, product)