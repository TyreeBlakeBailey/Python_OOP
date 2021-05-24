# animal file to create Animal class

class Animal:
    # pass # will allow the class to do nothing

    def __init__(self):  # self refers to this current class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "nom nom nom"

    def move(self):
        return " Moving around the world"


# create an object of our animal class to use the methods above

#cat = Animal()  # created an object of our animal class named cat
#print(cat.breathe())  # breathing for cat is abstracted
