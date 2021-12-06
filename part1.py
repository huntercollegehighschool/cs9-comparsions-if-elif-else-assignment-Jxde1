'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

# attempt 1

numberOne = int(input("Enter a number: "))
numberTwo = int(input("Enter another number: "))
numberThree = int(input("Enter another number: "))

def smallerTwo(x, y):
  if x < y:
    return x
  else:
    return y
def smallerThree(x, y, z):
  return smallerTwo(x, smallerTwo(y, z))

print("The smallest number is", smallerThree(numberOne, numberTwo, numberThree))