def f1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f1(n - 1) + f1(n - 2)


def f2(n):
    numbers = list()
    numbers.append(1)
    numbers.append(1)
    if n == 1 or n == 2:
        return numbers[n - 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers[n - 1]


def l1(number, ls):
    if len(ls) == 0:
        return False
    if ls[0] == number:
        return True
    else:
        return l1(number, ls[1:])


print(f1(30))
print(f2(30))

lss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1(11, lss)
