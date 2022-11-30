
from game import location
from game import config
from game.display import announce
from game.events import *

class Island (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "island"
        self.symbol = 'I'
        self.visitable = True
        self.starting_location = Dock_with_ship(self)
        self.locations = {}
        self.locations["Dock_with_ship"] = self.starting_location
        self.locations["soilder_office"] = soilder_office(self)
        self.locations["marketplace"] = soilder_office(self)
    def enter (self, ship):
        announce ("You and your crew come apon the coast of a vast island\nYou pass various large sugar planations and notice ominous plooms of smoke\nYou also see what seems to be a busy port in the distance", types = "COMMENT")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Dock_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "dock"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 0
    def enter (self):
        announce ("You enter the port and begin to approuch a small dock \nYou notice great ships of war was well as various commercial ships moving around in a great sence of panic\nAs you get closer to the dock you notice military men dressed in a depp navy blue waiting to question you", types = "COMMENT")
        announce("          |   North   |\n          |  Soldiers |\n          |           |\n _________|           |__________\n\n  West                      east\n  Market                    merchant ships\n\n_________              __________\n          |    you    |\n          |   South   |\n          |  *Leave*  |", pause = False)
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["soilder_office"]
        elif (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["marketplace"]
        elif (verb == "east"):
            config.the_player.next_loc = self.main_location.locations[""]

class soilder_office (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "office"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 0

    def enter (self):
        announce ("Soilder Captain: Hola inglés I assume? please come into my offive", types = "STRING")
        announce ("You and your crew enter the soilder's office.\n Three of his comrades follow in behind you shutting the door")
        announce ("Soilder Captain: Pirates or some paupers it doesn't matter we are desperate for men and will offer you food for mannig the cities walls against the rebels\nAs it stands we are under seige and all of you would be of great use to us", types = "STRING")
        announce ("This is not up for debate please sign here *unfurles a contract of enlistment*")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]


class marketplace (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "market"
        self.verbs['trade'] = self
        self.verbs['north'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 50

    def enter (self):
        announce ("**********HUSTLE AND BUSTLE MARKET**********")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]



##          |   North   |
##          |  Soldiers |
##          |           |
## _________|           |__________
##
##  West                      east
##  Market                    merchant ships
## _________             __________
##          |    you    |
##          |   South   |
##          |  *Leave*  |





##                  (escape 2)
## ______________       _____
## |            (go window) |
## |                        |
## |      |   desk |        |
## |      |        |        |
## |      (go  sign)        |
## |                        |
## |                        |
## |                   Door   /
## |      (escape enlistment)/
## |________________________/
##
##
##


























            
