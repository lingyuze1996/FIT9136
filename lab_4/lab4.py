"""
Lab 4: Data Types
"""

# Task 1: Sets

s1 = {1, 2, 3} | {2, 3, 4}
s2 = {1, 2, 3} & set()

# Task 2: Lists vs Tuples


# Task 3: Copies

base = [[]] * 5
base[1].append(1)

# Task 4: Dictionary Keys



# Task 5: Dictionary vs Lists



# Task 6: Load of Strings

strings = list()
while True:
    stringInput = input("Please enter a String: ")
    if stringInput.lower() != "quit":
        strings.append(stringInput)
    else:
        break
print(",".join(strings))

# Task 7: Analysing Literature

# Task 8 Tic-Tac-Toe
