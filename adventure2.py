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
        print("You have " + str(player.inventory)) # show the player what they have
    def dir_check(self): # debug only
        print("You can go " +
              "\n" + "North = " + str(self.NORTH) +
              "\n" + "East = " + str(self.EAST) +
              "\n" + "South = " + str(self.SOUTH) +
              "\n" + "West = " + str(self.WEST) +
              "\n" + "Up = " + str(self.UP) +
              "\n" + "Down = " + str(self.DOWN))
    def change_location(self, player): # Place knows where Player ends up if
        if player.movement == 1: # they move a direction
            player.location = self.NORTH
        elif player.movement == 2: # the movement can't break until later
            player.location = self.EAST  # and only if self.DIR is None
        elif player.movement == 3:
            player.location = self.SOUTH
        elif player.movement == 4:
            player.location = self.WEST
        elif player.movement == 5:
            player.location = self.UP
        elif player.movement == 6:
            player.location = self.DOWN
        elif player.movement == 0: # part of the loop break mechanism
            player.location = "stop"
        # print(player.location) # debug only

class Player:
    def __init__(self): # Player knows where they are and where they want to go
        self.movement = None
        self.location = None
        self.inventory = []
    def action_input(self): # Player knows where to move
        while True:
            action = input()
            if str(action) == "go " + "north" or "east" or "south" or "west" or "up" or "down":
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
                self.movement = 0 # special symbol for breaking the loop
                break
            elif str(action) == "pick up torch": # this part isn't working
                self.inventory.append("torch")
                print("You gingerly pick up the torch and wonder how it got there.")
                print("You have " + str(self.inventory))
            elif str(action) == "light torch" and self.inventory.count("torch") >= 1:
                print("You try to light the torch but realize you forgot a lighter.")

if __name__ == "__main__":
    player = Player()
    field = Place("cave", "river one", None, "forest one", None, None, player)
    field.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
    cave = Place(None, None, "field", None, "ledge", None, player)
    cave.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
    riverone = Place(None, None, None, "field", None, None, player)
    riverone.blurb = "The river is burbling happily. You can't see anything interesting but the field to the west."
    forestone = Place(None, "field", None, None, None, None, player)
    forestone.blurb = "The forest is peaceful but empty. You can't see anything interesting but the field to the east."
    ledge = Place(None, None, None, None, None, "cave", player)
    ledge.blurb = "The ledge is dark and empty. You can't see anything interesting but the cave below."
    print("Movement commands are go + north/south/east/west/up/down. All lowercase please. To exit, type stop." + '\n')
    player.location = field # start in field but stay in while loop later
    field.description() # would also put inventory here later
    player.action_input()
    field.change_location(player)
    while True:
        if player.location == "cave":
            cave.description()
            #cave.dir_check()
            player.action_input()
            cave.change_location(player)
        elif player.location == "ledge":
            ledge.description()
            #ledge.dir_check()
            player.action_input()
            ledge.change_location(player)
        elif player.location == "river one":
            riverone.description()
            #riverone.dir_check()
            player.action_input()
            riverone.change_location(player)
        elif player.location == "forest one":
            forestone.description()
            #forestone.dir_check()
            player.action_input()
            forestone.change_location(player)
        elif player.location == "field":
            field.description()
            #field.dir_check()
            player.action_input()
            field.change_location(player)
        elif player.location == "stop":
            break # because breaks can't be outside of loops
