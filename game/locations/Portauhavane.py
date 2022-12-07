
from game import location
from game import config
from game.display import announce
from game.events import *
## in posrgress sub locations
## merchant ships(from dock)
## road to wall (from office)
##street outside (from office)
##
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
        self.locations["marketplace"] = marketplace(self)
        self.locations["merchant"] = merchant(self)
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
            config.the_player.next_loc = self.main_location.locations["merchant"]

class soilder_office (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "office"
        self.verbs['window'] = self
        self.verbs['sign'] = self
        self.verbs['escape'] = self
        self.verbs['BESERK'] = self
    def enter (self):
        announce ("Soilder Captain: Hola inglés I assume? please come into my offive", types = "STRING")
        announce ("You and your crew enter the soilder's office.\n Four of his comrades follow in behind you shutting the door")
        announce ("Soilder Captain: Pirates or some paupers it doesn't matter we are desperate for men and will offer you food for mannig the cities walls against the rebels\nAs it stands we are under seige and all of you would be of great use to us", types = "STRING")
        announce ("This is not up for debate please sign here *unfurles a contract of enlistment*")
        announce ("______________       _____\n|            (go window) |\n|                        |\n|      |   desk |        |\n|      |        |        |\n|      (go  sign)        |\n|                        |\n|                        |\n|                   Door   /\n|      (escape enlistment)/\n|________________________/\n\n ******** GO BESERK ********\n*** for combat encounter ***", types = "COMMENT")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            return
class marketplace (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "marketplace"
        self.verbs['north'] = self
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.event_chance = 51
        self.events.append(soilderOFF.Soildersquad())

    def enter (self):
        announce ("As you make your way your way to the market the soildes dart to catch you!")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north" or verb == "east" or verb == "west"):
            pass

class merchant (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "marketplace"
        self.verbs['ship'] = self
        self.verbs['west'] = self

    def enter (self):
        announce ("CHECK")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "ship" or verb == "west"):
            pass














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
## |                go Door   /
## |      (escape enlistment)/
## |________________________/
##
##  ******** GO BESERK ********
## *** for combat encounter ***
##




##          |   North   |
##          |   slums   |
##          |           |
## _________|           |__________
##
##  West                      east
##  park                      Docks
## ________________________________
##          



##                                       /| 
##                                      / |
##                                     /  |
##                                    /___|
##                             \        |        /
##                              \_______|_______/
##                               \_____________/
##                    _____________________________
##                   |                Ship         |
##                   |                             |
##                   |                             |
##                   |                             | 
## __________________|                             |
##                                                 |
##  West                                           |
##  Docks                                          |
## ________________________________________________|
##
##
##



        
