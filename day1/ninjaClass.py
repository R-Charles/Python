from socketserver import ThreadingUnixDatagramServer


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name 
        self.pet = pet 
        self.treats = treats
        self.pet_food = pet_food 

    def walk(self):
        print(f"I'm going to take my {self.pet} on a walk")
    def feed(self):
        print(f"I'm going to feed my {self.pet} some {self.treats}")
    def bathe():
        print()
class Pet:
    def __init__(self, name, type, tricks, health, energy)
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print()
    def eat(self):
        print()
    def play(self):
        print()
    def noise():
        print()
