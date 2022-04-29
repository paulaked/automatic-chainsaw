class Animal:

    def __init__(self):
        self.alive = True
        self.eyes = True
        self.lungs = True
        self._location = "zoo"

    def breathe(self):
        return "One breath in and one out"

    def move(self):
        return "onwards and upwards and sometimes backwards"

    def get_location(self):
        return "The animal is located in: " + self._location

    def set_location(self, new_location):
        if new_location.isalpha():
            self._location = new_location


cat = Animal()
#print(cat.breathe())