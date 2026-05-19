class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health

# TODO: Create Superhero instances
sup1 = SuperHero("Batman", "Intelligence", 100)
sup2 = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(sup1.name)
print(sup1.power)
print(sup1.health)

print(sup2.name)
print(sup2.power)
print(sup2.health)
