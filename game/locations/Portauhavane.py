
from game import location
from game import config
from game.display import announce
from game.events import *
from game.ship import *
from game import config
from game.items import BakerRifle
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
        self.checks = False
        self.locations = {}
        self.locations["Dock_with_ship"] = self.starting_location
        self.locations["soilder_office"] = soilder_office(self)
        self.locations["marketplace"] = marketplace(self)
        self.locations["merchant"] = merchant(self)
        self.locations["Wall"] = Wall(self)
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
        self.verbs['north'] = self
        self.agree = False
    def enter (self):
        announce ("Soilder Captain: Hola inglés I assume? please come into my offive", types = "STRING")
        announce ("You and your crew enter the soilder's office.\n Four of his comrades follow in behind you shutting the door")
        announce ("Soilder Captain: Pirates or some paupers it doesn't matter we are desperate for men and will offer you food for mannig the cities walls against the rebels\nAs it stands we are under seige and all of you would be of great use to us", types = "STRING")
        announce ("This is not up for debate please sign here *unfurles a contract of enlistment*")
        announce ("______________       _____\n|            (go window) |\n|                        |\n|      |   desk |        |\n|      |        |        |\n|      (go  sign)        |\n|                        |\n|                        |\n|                   Door   /\n|      (escape enlistment)/\n|________________________/\n\n ******** GO BESERK ********\n*** for combat encounter ***", types = "COMMENT")
        x = menu (["Sign the elismment papers","Run for the window","Run for the door","Flip the tabele and fight!"])
        if x == 0:
            announce("Thank you for your compliance here is our stock of rifels take and equip them before heading north as wells as some food and medicine")
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.add_to_inventory([BakerRifle()])
            config.the_player.ship.take_food(-10)
            config.the_player.ship.take_med(-2)
            self.agree = True
        elif x == 1:
            self.escape_attempt(3,False)
        elif x == 2:
            self.escape_attempt(2,False)
        elif x == 3:
            self.escape_attempt(1,True)
        
    def escape_attempt(self,chance, addvantage):
        if addvantage: 
            announce("You were able to kill two soilders before they could even react")
            soilderOFF.Soildersquad(3).process(config.the_player.world)
        elif random.randrange(1,chance) == 1:
            soilderOFF.Soildersquad(4).process(config.the_player.world)

            
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north" and self.agree):
            config.the_player.next_loc = self.main_location.locations["Wall"]
        elif(self.agree):
            announce ("are you sure you want to head the wrong direction? The soilders will attack you for this disloyalty")
            y = menu(["Lets get out of here","lets just head north"])
            if y == 0:
                soilderOFF.Soildersquad(5).process(config.the_player.world)
                announce("You win but this act of desertion will not be tolerated you must return to your ship")
                config.the_player.next_loc = config.the_player.ship
                config.the_player.visiting = False
            elif y == 1:
                config.the_player.next_loc = self.main_location.locations["Wall"]
        else:
            announce("You win but this act of desertion will not be tolerated you must return to your ship")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = Fals  

class marketplace (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "marketplace"
        self.verbs['north'] = self
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.event_chance = 50
        self.events.append(soilderOFF.Soildersquad(4))

    def enter (self):
        announce ("As you make your way your way to the market the soildes dart to catch you!")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north"):
            announce("The slums look far too dangerous to enter")
        elif (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Dock_with_ship"]
        elif (verb == "west"):
            announce("A georgious park with a fishable pond")
class Wall (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Wall"
        self.verbs['south'] = self
    def enter (self):
        announce("Welcome to the wall men we another wave of drowned are approuching be alert!")
        announce("survive three waves to earn your keep")
        drowned_pirates.DrownedPirates().process(config.the_player.world)
        announce("Thank you for your service you can head south to return to your ship")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        else:
            announce("there is nothing arround so you head back to your ship")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False





class merchant (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "merchant"
        self.verbs['north'] = self
        self.verbs['west'] = self
    def enter (self):
        announce ("A dead end but you see a grand ship docked")
        announce("                                       /| \n                                      / |\n                                     /  |\n                                    /___|\n                             \        |        /\n                              \_______|_______/\n                    __________________________\n                   |                         |\n                   |                         |\n                   |                         |\n                   |                         | \n __________________|                         |\n                                             |\n  West                                       |\n  Docks                                      |\n_____________________________________________|\n Go North to see ship","COMMENT")
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Dock_with_ship"]
        if(verb == "north"):
            if(not(self.main_location.checks)):
                Enemy_Pirates.Enemy_Pirates().process(config.the_player.world)
                self.main_location.checks = True
            else:
                announce("You can't do that again")
             









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
##                    __________________________
##                   |                         |
##                   |                         |
##                   |                         |
##                   |                         | 
## __________________|                         |
##                                             |
##  West                                       |
##  Docks                                      |
## ____________________________________________|
##
##
##



        
