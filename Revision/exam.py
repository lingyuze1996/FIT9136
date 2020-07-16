class Stack:

    def __init__(self):
        self.data = []
        self.count = 0

    def __str__(self):
        return f"{self.data}"

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def push(self, item):
        self.data.append(item)
        self.count += 1

    def pop(self):
        assert not self.is_empty()
        self.count -= 1
        return self.data.pop()

    def peek(self):
        assert not self.is_empty()
        return self.data[-1]

def mystery_func(n):
    if n < 2:

        return 1

    else:

        return 1 / n + (mystery_func(n - 1))

mystery_func(10)


def find_student_union(inputFile1, inputFile2, outputFile):
    try:
        input1 = open(inputFile1, "r")
        input2 = open(inputFile2, "r")

        id_set = set()
        for id1 in input1.readlines():
            id_set.add(id1.strip("\n"))
        for id2 in input2.readlines():
            id_set.add(id2.strip("\n"))

        input1.close()
        input2.close()
        output = open(outputFile, "w")
        for each_id in id_set:
            output.write(each_id + "\n")
    except FileNotFoundError:
        print("Please check your input files")



def special_string_formatter(my_string):
    my_stack = Stack()
    reverse = ""
    for char in my_string:
        my_stack.push(char)

    while len(my_stack) > 0:
        reverse += my_stack.pop()


class AlphabetStack(Stack):
    def push(self, item):
        if len(str(item)) != 1:
            print("Input Length error!")
            return
        if "a" <= str(item) <= "z":
            super().push(str(item))
        else:
            print("Input Character Error!")

    def get_largest_alphabet(self):
        largest = "a"
        temp = list()
        while not self.is_empty():
            pop = self.pop()
            temp.append(pop)
            if pop > largest:
                largest = pop
        while len(temp) != 0:
            self.push(temp[-1])
        return largest


def mystery_func_loop(n):
    s = 0
    for i in range(1, n + 1):
        s += 1/i
    return s
a = mystery_func_loop(10)

'''
a = AlphabetStack()
a.push("a")
a.push("b")
a.push("z")
a.get_largest_alphabet()'''
mystery_func(10)