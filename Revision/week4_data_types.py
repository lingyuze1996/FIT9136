list1 = [1, 2, 8, 4]
list2 = [1, 2, 3, 4, 5]

set1 = {1, 2, 3}
set2 = {0, 2, 4}

a = "12345"

list1 + list2
set1.add(set2)

list1.sort()
list1.reverse()
list1.extend(list2)
print(list1)

list3 = ["a", "b", "c", "ddd"]
",".join(list3)

tuple1 = (1, 2, 3)

dict1 = {1: 4, 2: 5}
dict1["a"] = 5

del (dict1[1])

dict1.keys()
dict1.values()

for (key, value) in dict1.items():
    print(str(key) + str(value))

print((3 > 4) and (1 < 2))
