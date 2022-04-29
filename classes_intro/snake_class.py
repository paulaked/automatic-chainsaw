from reptile_class import Reptile
from classes_and_methods import Animal

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = False

    def move(self):
        return "slithering around"

python = Snake()
print(python.move())

cat = Animal()
print(cat.move())

Create the following classes:
Transport class, with vehicles, trains, planes, and boats
Use the 4 pillars

