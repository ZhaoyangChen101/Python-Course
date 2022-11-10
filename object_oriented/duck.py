class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work but i am flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)
        # composition

    def walk(self):
        print("Waddle")

    def swim(self):
        print("Come on in, the water is lovely")

    def quack(self):
        print("Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly for South")

    def quack(self):
        print("Are you kidding? I am a penguin!")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    # percy = Penguin()
    # test_duck(percy)
