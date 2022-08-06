from socketserver import ThreadingUnixDatagramServer


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name 
        self.pet = pet 
        self.treats = treats
        self.pet_food = pet_food 
        self.health = 100
        self.energy = 50



    def walk(self):
        pass
    def feed(self):
        pass
    def bathe(self):
        pass
class Pet:
    def __init__(self, name, type, tricks, health, energy)
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.play += 5
        self.energy -= 15
        return self

    def noise(self):
        print("arf arf arf")
        return self
