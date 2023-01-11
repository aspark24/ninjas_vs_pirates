class Character:

    def __init__(self, name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    # def health(self, amount):
    #     if self.health >=amount:
    #         self.health -=amount
    #     else:
    #         print("Player is dead!")
    #         self.health -=0




class Ninja(Character):

    def __init__(self, name, strength, speed, health):
        super().__init__(name, strength, speed, health)

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self, pirate, amount):
        if self.health >=amount:
            self.health-=amount
        else:
                print("ded")
                self.health -=0

        pirate.health -= self.strength
        return self



class Pirate(Character):

    def __init__(self, name, strength, speed, health):
        super().__init__(name, strength, speed, health)

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack (self, ninja):
        ninja.health -= self.strength
        return self

n1 = Ninja("Shadow", 10, 5, 100)

p1 = Pirate("Patches", 15, 3, 100)

p1.attack(n1)
n1.show_stats()
p1.attack(n1)
n1.show_stats()
p1.attack(n1)
n1.show_stats()
p1.attack(n1)
n1.show_stats()
p1.attack(n1)
n1.show_stats()
p1.attack(n1)
n1.show_stats()
p1.attack(n1)
n1.show_stats()