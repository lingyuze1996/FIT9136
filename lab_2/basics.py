'''
NAME:


'''

from math import sin

x = int(input('Please input x: '))
y = int(input('Please input y: '))

'''
outputFile = open('output.txt', 'w')
outputFile.write("aaa\n")
outputFile.write("df")
outputFile.close()
'''

print('x + y = ', x + y)
print('x - y = ', x - y)
print('x * y = ', x * y)
print('x % y = ', x % y)

# format method 1
print('x / y = ', format(x / y, ".2f"))

# format method 2
print('x sin(y) = %.2f' % (x * sin(y)))

print(__name__)

