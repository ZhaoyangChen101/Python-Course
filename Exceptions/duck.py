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

    def __init__(self):
        self.fly = self.aviat

    def walk(self):
        print("Waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly for South")

    def quack(self):
        print("Are you kidding? I am a penguin!")

    def aviat(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate")  # TODO remove this before release
                #  在try block里面raise except里面的异常，可以test这个异常。
            except AttributeError as e:
                print("One duck down")
                problem = e

        if problem:
            raise problem


if __name__ == "__main__":
    donald = Duck()
    donald.fly()

