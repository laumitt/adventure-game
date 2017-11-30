class Place:
    def __init__(self, locnorth, loceast, locsouth, locwest, locup, locdown, player):
        self.NORTH = locnorth # so that each place can define its own
        self.EAST = loceast # surroundings but run off one class
        self.SOUTH = locsouth
        self.WEST = locwest
        self.UP = locup
        self.DOWN = locdown
        self.location = None
        self.blurb = None
    def description(self): # to describe each location and by extension
        print(self.blurb) # give the player possible directions
    def dir_check(self): # debug only
        print("You can go " +
              "\n" + "North = " + str(self.NORTH) +
              "\n" + "East = " + str(self.EAST) +
              "\n" + "South = " + str(self.SOUTH) +
              "\n" + "West = " + str(self.WEST) +
              "\n" + "Up = " + str(self.UP) +
              "\n" + "Down = " + str(self.DOWN))
    def change_location(self, player): # Place knows where Player ends up if
        if player.movement == 1: # they move a certain direction
            player.location = self.NORTH
        elif player.movement == 2: # the movement can't break until later
            player.location = self.EAST
        elif player.movement == 3:
            player.location = self.SOUTH
        elif player.movement == 4:
            player.location = self.WEST
        elif player.movement == 5:
            player.location = self.UP
        elif player.movement == 6:
            player.location = self.DOWN
        elif player.movement == "stop": # part of the loop break mechanism
            player.location = "stop"

class Player:
    def __init__(self): # where they are, where they want to go, and what they have
        self.movement = None
        self.location = None
        self.inventory = []
    def action_input(self): # Player knows where to move
        while True:
            action = input()
            if str(action) in ["go north", "go east", "go south", "go west", "go up", "go down"]:
                if action == "go north":
                    self.movement = 1
                    break
                elif action == "go east":
                    self.movement = 2
                    break
                elif action == "go south":
                    self.movement = 3
                    break
                elif action == "go west":
                    self.movement = 4
                    break
                elif action == "go up":
                    self.movement = 5
                    break
                elif action == "go down":
                    self.movement = 6
                    break
            elif str(action) == "stop": # to break the loop
                self.movement = "stop"
                break
            elif str(action) == "pick up torch":
                self.inventory.append("torch") # doesn't actually stop appending torches
                print("You gingerly pick up the torch and wonder how it got there.")
            elif str(action) == "light torch" and self.inventory.count("torch") >= 1:
                print("You try to light the torch but realize you forgot a lighter.")
            else: # if they make a typo or say something else
                print("You realize you are spouting gibberish into thin air.")

if __name__ == "__main__":
    player = Player()
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
    ford = Place("river one", None, "river two", None, None, None, player)
    ford.blurb = "You stand at a ford, with river burbling to the north and south."
    foresttwo = Place("forest path", "clearing", "clearing", "ford", None, None, player)
    foresttwo.blurb = "A path runs through the forest to the north, a clearing opens to the south and east, and the river runs over the ford to the west."
    clearing = Place("forest two", None, None, "forest two", None, None, player)
    clearing.blurb = "The clearing is empty. Forest stretches to the north and west."
    forestpath = Place("forest three", None, "forest two", None, "up tree", None, player)
    forestpath.blurb = "Forest surrounds the path to the north and south. It looks like you can climb a tree."
    uptree = Place(None, None, None, None, None, "forest path", player)
    uptree.blurb = "You find a beautiful view but not much else. The branches form a perfect ladder down to the path."
    rivertwo = Place("ford", None, None, None, None, None, player)
    rivertwo.blurb = "To the south, the river runs over an impassable waterfall. The ford crosses to the north."
    hill = Place(None, None, "forest one", "forest three", None, None, player)
    hill.blurb = "The majestic hill looks over the forest to the south and west."
    forestthree = Place("hill", None, "forest path", None, None, None, player)
    forestthree.blurb = "To the north, a hill rises. To the south, a path runs through the forest."
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
    print("Movement commands are go + north/south/east/west/up/down. All lowercase please. To exit, type stop." + '\n')
    player.location = "field" # start in the field
    while True:
        if player.location == "stop": # part of break loop function (easy out)
            break
        if player.location == None: # to give error if player moves somewhere they can't
            print("You stumble into an invisible wall and realize you can't go that way.")
        locs[player.location].description()
        current = player.location # to store location
        player.location = None # to run while loop
        while player.location == None:
            player.action_input()
            locs[current].change_location(player)
            if player.location == None:
                print("You stumble into an invisible wall and realize you can't go that way.")
