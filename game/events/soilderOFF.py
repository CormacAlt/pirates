from game import event
import random
from game.combat import Combat
from game.combat import Soilder
from game.display import announce

class Soildersquad (event.Event):

    def __init__ (self,add):
        self.name = " The soilders attack! "
        self.add = add
    def process (self, world):
        result = {}
        result["message"] = "the soilders are defeated!"
        monsters = []
        monsters.append(Soilder("Soilder captain"))
        monsters[0].speed = 1.2*monsters[0].speed
        monsters[0].health = 2*monsters[0].health
        n = 1
        while n <= self.add:
            monsters.append(Soilder("soidlers "+str(n)))
            n += 1
        announce ("The soidlers attack you and your crew")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result
