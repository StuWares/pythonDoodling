# The Collatz Sequence
# write a function with one parameter named number.
# if number is even it should print number // 2 and return this value
# if odd, it should print and return 3 * number + 1


    
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        global checkForOne
        checkForOne = number
        return
    else:
        number = number * 3 + 1
        print(number)
        checkForOne = number
        return



checkForOne = 0
print('Enter a number:')

userInput = ''

# Will keep looping until the user enters a valid integer
while userInput == '':
    try:
        userInput = int(input())
    except ValueError:
        print('Error: Please only enter a number:')


collatz(userInput)

# This loop will keep passing the returned
# value back into the function until the answer is 1
while checkForOne != 1:
    collatz(checkForOne)

