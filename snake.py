# Creating snake class as child class of reptile

from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.coldblooded = True
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    def use_tongue_to_smell(self):
        return "I can small the taste...."


snake_object = Snake()

# print(f"This is from snake class, {snake_object.use_tongue_to_smell()}")
# print(f"This function is from reptile class {snake_object.seek_heat()}")
# print(f"This function is from Animal class {snake_object.eat()}")
