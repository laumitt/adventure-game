# to do list
# storyline

class Place:
    def __init__(self, locnorth, loceast, locsouth, locwest, locup, locdown, player):
    # so that each place can define its own surroundings but run off one class
        self.NORTH = locnorth
        self.EAST = loceast
        self.SOUTH = locsouth
        self.WEST = locwest
        self.UP = locup
        self.DOWN = locdown
        self.location = None
        self.blurb = None
    def description(self):
    # to describe each location and by extension give player possible directions
        print(self.blurb)
#    def dir_check(self): # debug only - doesn't actually run in __main__
#        print("You can go " +
#              "\n" + "North = " + str(self.NORTH) +
#              "\n" + "East = " + str(self.EAST) +
#              "\n" + "South = " + str(self.SOUTH) +
#              "\n" + "West = " + str(self.WEST) +
#              "\n" + "Up = " + str(self.UP) +
#              "\n" + "Down = " + str(self.DOWN))
    def get_location(self, movement):
    # tell Player where they'd end up after moving a certain way
        if movement == 1:
            return self.NORTH
        elif movement == 2:
            return self.EAST
        elif movement == 3:
            return self.SOUTH
        elif movement == 4:
            return self.WEST
        elif movement == 5:
            return self.UP
        elif movement == 6:
            return self.DOWN
        elif movement == "stop": # part of the loop break mechanism
            return "stop"
        elif movement == 9:
            return "forest path"

class Inventory:
    def __init__(self):
        self.have = []
        self.check = None
    def inventory_add(self, item):
        self.have.append(item)
    def inventory_check(self, item):
        if self.have.count(item) >= 1:
            self.check = True

class Player:
    def __init__(self):
    # where they want to go, where they are, and what they have
    # gate status also stored here
        self.movement = None
        self.location = None
        self.inventory = []
        self.gateopen = False
        self.actions = {"go north" : 1,
                        "go east" : 2,
                        "go south" : 3,
                        "go west" : 4,
                        "go up" : 5,
                        "go down" : 6,
                        "stop" : "stop"}
    def action_input(self):
    # Player knows where to move but doesn't know where that movement will take them
        while True:
            action = input()
            if str(action) in ["go north", "go east", "go south", "go west", "go up", "go down"]:
                self.movement = self.actions[action]
                if action == "go up":
                    if current == "forest path":
                        if self.gateopen == True:
                            self.movement = 5
                        else:
                            print("The gate isn't open yet.")
                            self.movement = 9
                            break
                    else:
                        break
                break
            elif str(action) == "stop": # to break the loop
                self.movement = "stop"
                break
            # beginning of non-movement actions
            elif str(action) == "pick up torch":
                if current == "cave":
                    inventory.inventory_add("torch")
                    print("You gingerly pick up the torch and wonder how it got there.")
                else:
                    print("What torch?")
            elif str(action) == "light torch":
                inventory.inventory_check("torch")
                if inventory.check == True:
                    print("You try to light the torch but realize you forgot a lighter.")
                else:
                    print("What torch?")
            elif str(action) == "drop torch":
                inventory.inventory_check("torch")
                if inventory.check == True:
                    print("The torch clatters to the ground.")
                else:
                    print("What torch?")
            elif str(action) == "pick up rock":
                if current == "ford":
                    inventory.inventory_add("rock")
                    print("You turn the smooth, shiny rock over in your hand.")
                else:
                    print("What rock?")
            elif str(action) == "inspect rock":
                inventory.inventory_check("rock")
                if inventory.check == True:
                    print("You look as hard as you can but can't see anything special about the rock.")
                else:
                    print("What rock?")
            elif str(action) == "drop rock":
                inventory.inventory_check("rock")
                if inventory.check == True:
                    print("The rock thuds to the ground.")
                else:
                    print("What rock?")
            elif str(action) == "move leaves":
                if current == "clearing":
                    print("You kick the leaves aside to find a rusty old key.")
                else:
                    print("What leaves?")
            elif str(action) == "pick up key":
                if current == "clearing":
                    inventory.inventory_add("key")
                    print("You slip the key into your pocket.")
                else:
                    print("What key?")
            elif str(action) == "unlock gate":
                if current == "forest path":
                    inventory.inventory_check("key")
                    if inventory.check == True:
                        print("The gate swings open on rusty hinges, allowing you to climb the tree.")
                        self.gateopen = True
                    else:
                        print("You don't have a key.")
                else:
                    print("What gate?")
            elif str(action) == "pick up gem":
                if current == "up tree":
                    inventory.inventory_add("gem")
                    print("You admire the sparkling facets of the gem and slip it into your pocket.")
                else:
                    print("What gem?")
            elif str(action) == "drop gem":
                inventory.inventory_check("gem")
                if inventory.check == True:
                    print("The gem sparkles as it falls.")
                else:
                    print("What gem?")
            else: # if they make a typo or say something else
                print("You realize you are spouting gibberish into thin air.")
    def change_location(self, location):
    # set location to what Place said
        self.location = location

if __name__ == "__main__":
    player = Player()
    inventory = Inventory()
    # initiation (map location) of locations and descriptions
    field = Place("cave", "river one", None, "forest one", None, None, player)
    field.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
    cave = Place(None, None, "field", None, "ledge", None, player)
    cave.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
    riverone = Place(None, None, "ford", "field", None, None, player)
    riverone.blurb = "You stand next to a river burbling south to a ford along the field to the west."
    forestone = Place("hill", "field", None, None, None, None, player)
    forestone.blurb = "From the forest, the field stretches to the east and a hill rises to the north."
    ledge = Place(None, None, None, None, None, "cave", player)
    ledge.blurb = "The ledge is dark and empty. You can't see anything interesting but the cave below."
    ford = Place("river one", "forest two", "river two", None, None, None, player)
    ford.blurb = "You stand at a ford, with river burbling to the north and south and forest to the east. There is a shiny rock on the ground."
    foresttwo = Place("forest path", "clearing", "clearing", "ford", None, None, player)
    foresttwo.blurb = "A path runs through the forest to the north, a clearing opens to the south and east, and the river runs over the ford to the west."
    clearing = Place("forest two", None, None, "forest two", None, None, player)
    clearing.blurb = "The clearing is empty except a pile of leaves on the ground. Forest stretches to the north and west."
    forestpath = Place("forest three", None, "forest two", None, "up tree", None, player)
    forestpath.blurb = "Forest surrounds the path to the north and south. A high fence surrounds a tree that it looks like you could climb up."
    uptree = Place(None, None, None, None, None, "forest path", player)
    uptree.blurb = "You find a beautiful view and a sparkling red gem. The branches form a perfect ladder down to the path."
    rivertwo = Place("ford", None, None, None, None, None, player)
    rivertwo.blurb = "To the south, the river runs over an impassable waterfall. The ford crosses to the north."
    hill = Place(None, None, "forest one", "forest three", None, None, player)
    hill.blurb = "You stand halfway up the majestic hill, looking over the forest to the south and west."
    forestthree = Place("hill", None, "forest path", None, None, None, player)
    forestthree.blurb = "To the north, a hill rises. To the south, a path runs through the forest."
    # dictionary of locations and objects
    locs = {"field" : field,
            "cave" : cave,
            "river one" : riverone,
            "forest one" : forestone,
            "ledge" : ledge,
            "ford" : ford,
            "forest two" : foresttwo,
            "clearing" : clearing,
            "forest path" : forestpath,
            "up tree" : uptree,
            "river two" : rivertwo,
            "hill" : hill,
            "forest three" : forestthree}
    # basic setup instructions, to run once
    print('\n' + "Instructions:" + '\n' + "Movement commands are go + north/south/east/west/up/down. All lowercase please. To exit, type stop." + '\n')
    player.location = "field" # start in the field
    while True:
        if player.location == "stop": # part of break loop function (easy out)
            break
        locs[player.location].description()
        current = player.location # to store location
        player.location = None # to run while loop
        while player.location == None:
            player.action_input()
            player.change_location(locs[current].get_location(player.movement))
            if player.location == None: # if they go somewhere they can't
                print("You stumble into an invisible wall and realize you can't go that way.")
