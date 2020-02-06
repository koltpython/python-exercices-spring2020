"""
FizzBuzz is a classical interview question. 
We will implement a modified version of it, however, you can also find the original version on the web if you are interested.

Write a program that takes a number from the user.
If this number is negative, print an error message
if this number is a multiple of 3, print 'Fizz'
if this number is a multiple of 5, print 'Buzz'
if this number is a multiple of 15, print 'FizzBuzz'
otherwise, print the number itself.

You can assume user will enter a valid integer value.

Examples:
Please enter a number: 25
Buzz

Please enter a number: -5
You entered a negative number!

Please enter a number: 2
2

Please enter a number: 36
Fizz

Please enter a number: 3330
FizzBuzz
"""

number = int(input('Enter a number: '))

if number < 0:
    print('You entered a negative number!')
elif number % 15 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
