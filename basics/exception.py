def division(a, b):
    return a / b


#division(3, 0)
x = int(input("a: "))
y = int(input("b: "))
try:
    print(division(x, y))
except Exception as d:
    pass
