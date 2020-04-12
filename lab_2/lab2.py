"""
Author: Yuze Ling

Created: Mar 24 2020
Last modified: Apr 12 2020

Lab 2: Python basics
"""


# Task 4: Calculator

from math import sin

x = int(input('Please input x: '))
y = int(input('Please input y: '))

print('x + y = ', x + y)
print('x - y = ', x - y)
print('x * y = ', x * y)
print('x % y = ', x % y)

# format method 1
print('x / y = ', format(x / y, ".2f"))

# format method 2
print('x sin(y) = %.2f' % (x * sin(y)))


# Task 6: Converting Temperature
temperatureF = int(input("Please enter a temperature Fahrenheit: "))
temperatureC = (temperatureF - 32) * 5 / 9
print("%.2f" % temperatureC)

# Task 7: Greetings


# Task 8: Shapes


# Task 9: Files

originalFile = open('numbers.txt', 'w')
originalFile.write('5\n')
originalFile.write('7\n')
originalFile.write('12\n')
originalFile.close()

inputFile = open('numbers.txt', 'r')
ls = inputFile.readlines()
inputFile.close()

contents = ''
for i in ls:
    contents += i
content = contents.split('\n')

simpleSum = 0
for j in content:
    if j != '':
        simpleSum += int(j)

outputFile = open('numbers.txt', 'a')
outputFile.write('sum: ' + str(simpleSum) + '\n')
outputFile.close()
