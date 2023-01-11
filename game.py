from classes.ninja import Ninja
from classes.pirate import Pirate
# from classes.character import Character

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()