# this is the python class
from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.Large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "Enjoy what ever you can get"

    def constrict(self):
        return "Choke out the prey "

    def climb(self):
        return "Can climb very fast"

    def shed_skin(self):
        return "Time to crawl out myself"

    def __Private(self):#use double __ to make a function private
        return "This function is private and cannot be called by anywhere else"

python_object = Python()

print(f" This is from python class {python_object.two_lungs}")
print(f" This is from snake class {python_object.use_tongue_to_smell()}")
