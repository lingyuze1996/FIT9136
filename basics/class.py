class Pig:
    def __init__(self, name="a"):
        x = 3
        self.name = name
        self.age = 0
        self.x = x

    def shout(self):
        print("我是最骚的")


class Ppz(Pig):
    def __init__(self):
        self.ch = "骚"

    def shout(self):

        super().shout()
        print("我才是最骚的")


ppz = Ppz()
ppz.shout()

a = "ddfs"
Ppz.__base__
Ppz
Pig.__subclasses__()

type.__class__
object.__class__
type
object

aaa = type(ppz)


def hello(self):
    self.name = 10
    print("fdsadfs")

hello.__str__()

t = type("eg", (), {"g": hello})
t
Ppz
tt = t()


ttt = type(tt)

a = ttt()
a.g()