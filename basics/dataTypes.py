"""
Week 4 Lecture: Data Types
"""

# list

ls1 = [6, 7, "a", 4, 1]
ls3 = ["bcdefg", "bcd"]

item1 = ls1[0]
ls1[1] = 8

ls2 = ls1[0::2]

ls4 = ls1 + ls2

ls5 = ls2 * 2

ls6 = [a ** 2 for a in range(5)]

min(ls3)
max(ls3)
len(ls3)
ls1.index(1)
ls3.count("a")
ls3.sort()
ls3.sort(reverse=True)
ls3.append(3)
ls3.insert(1, "a")
ls4.pop()
itemPop = ls4.pop(3)
ls4.remove(6)
ls4.reverse()
ls4.extend(ls5)

r1 = range(5)
r2 = range(0, 5, 2)

ls = ["aa", "bb"]
" ".join(ls)

# tuple

tp1 = (1, 3, 5)
x, y, z = tp1

tp2 = (2, "a5")

tp1000 = tuple(range(1000))
ls1000 = list(range(1000))
tp1000.__sizeof__()
ls1000.__sizeof__()

# set

set0 = {1, 2, 3, 4, 5, 6, 7}
set1 = {1, "two"}
set2 = {False, True}
set3 = {True, 1}

set0.add(10)
set0.remove(6)
set0.discard(8)
set0.pop()
set3.clear()

s1 = set0 | set1
s2 = set0 & set1
s3 = set0 - set1
s4 = set0 ^ set1

s = set([1, "zero", 4, "four", "zero", 8, 2])
list(s)

# dictionary

