# creating a reptile class to inherit everything from animal class

from Animal import Animal


class Reptile(Animal):

    def __init__(self):
        # we have a key word called super which allows it to inherit everything from parent class
        super().__init__()
        self.coldblooded = True
        self.tetrapod = None
        self.heart_chambers = [ 3, 4 ]

    def seek_heat(self):
        return "It's rainy and windy where is the sun "

    def hunt(self):
        return "Keep hunting for food "

    def use_venom(self):
        return "If i've got it im using it "


reptile_object = Reptile()

# print(f"This function is from the reptile class {reptile_object.hunt()}")
# print(f"This function is from the Animal class {reptile_object.eat()}")
