class Pig:
    def __init__(self, name="", age=0):
        self.age = age
        self.name = name

    def __str__(self):
        return "My name is " + self.name + ", I am " + str(self.age) + " years old."


class Ppz(Pig):
    def __init__(self, cute=True):
        super().__init__()
        self.cute = cute

    def shout(self, content):
        print(content + self.name)


ppz1 = Pig()
ppz2 = Pig("ppz", 25)
ppz3 = Ppz(cute=True)

print(ppz1)
print(ppz2)
print(ppz3)
ppz3.shout("我是最骚的")
