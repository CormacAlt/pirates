from game import event
import random
from game.combat import Combat
from game.combat import Soilder
from game.display import announce
from game.display import menu
from game.ship import *
from game import config
from game.events import seagull

class Enemy_Pirates (event.Event):

    def __init__ (self):
        self.name = " Powerful Enemy Ship "

    def process (self, world):
        announce("You see a powerful enemy ship", "COMMENT")
        if( menu (["engage the shipe they have information and treasure","They are too powerful"])==0):
            result = {}
            result["message"] = "the soilders are defeated!"
            monsters = []
            monsters.append(Soilder("Soilder captain"))
            monsters[0].speed = 1.5*monsters[0].speed
            monsters[0].health = 2.5*monsters[0].health
            n = 1
            while n <= random.randrange(4, 6):
                monsters.append(Soilder("Pirates "+str(n)))
                n += 1
            announce ("You have attempted to attack the the strong pirates")
            Combat(monsters).combat()
            config.the_player.ship.take_food(random.randrange(-40,-20))
            config.the_player.ship.take_med(random.randrange(-5,-3))
            announce("You now have  requisitioned food and medicine from the defated ship\nYour food stocks are now: " + str(config.the_player.ship.get_food()) + "\nAnd your medicine is now: " + str(config.the_player.ship.get_med()),"")
            announce ("You also find a map to your home port which has the coordinates:" + str(config.the_player.world.homex) + ", " + str(config.the_player.world.homey))
            announce ("You also find a state of the art rifle")
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.add_to_inventory([BakerRifle()])
            result["newevents"] = [ self ]
            return result
        else:
            config.the_player.world.events.append(seagull.Seagull())
            config.the_player.world.events.append(seagull.Seagull())
            config.the_player.world.events.append(seagull.Seagull())
            config.the_player.world.events.append(seagull.Seagull())
            config.the_player.world.events.append(seagull.Seagull())
            announce("Your cowardice is noted")
            result = {}
            config.the_player
            result["message"] = "No Seagall in the land will now fear you"
            result["newevents"] = [ self ]
            return result
