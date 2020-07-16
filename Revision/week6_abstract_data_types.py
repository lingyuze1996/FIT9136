class Stack:
    def __init__(self):
        self.my_stack = list()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.my_stack.append(item)
        self.size = self.size + 1

    def pop(self):
        self.size = self.size - 1
        return self.my_stack.pop(self.size - 1)


    def peek(self):
        return self.my_stack[self.size - 1]


class MyQueue:
    def __init__(self):
        self.my_queue = list()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def append(self, item):
        self.size += 1
        self.my_queue.append(item)

    def serve(self):
        self.size -= 1
        return self.my_queue.pop(0)


