class Place:
    def __init__(self, locnorth, loceast, locsouth, locwest, locup, locdown):
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
        if player.movement == 1: # they move a direction
            player.location = self.NORTH
        elif player.movement == 2: # the movement cant break until later
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
    def move_input(self): # Player knows where to move
        move = input()
        if move == "go north":
            self.movement = 1
        elif move == "go east":
            self.movement = 2
        elif move == "go south":
            self.movement = 3
        elif move == "go west":
            self.movement = 4
        elif move == "go up":
            self.movement = 5
        elif move == "go down":
            self.movement = 6
        elif move == "stop": # to break the loop
            self.movement = 0 # special symbol for breaking the loop
        elif move == "pick up torch":
            self.inventory.append("torch")
            print("You gingerly pick up the torch and wonder how it got there.")
            move = input() # can this be simplified?
            if move == "go north":
                self.movement = 1
            elif move == "go east":
                self.movement = 2
            elif move == "go south":
                self.movement = 3
            elif move == "go west":
                self.movement = 4
            elif move == "go up":
                self.movement = 5
            elif move == "go down":
                self.movement = 6
            elif move == "stop": # to break the loop
                self.movement = 0 # special symbol for breaking the loop
            elif move == "light torch":
                print("You try to light the torch but realize you forgot a lighter.")
                move = input()
                if move == "go north":
                    self.movement = 1
                elif move == "go east":
                    self.movement = 2
                elif move == "go south":
                    self.movement = 3
                elif move == "go west":
                    self.movement = 4
                elif move == "go up":
                    self.movement = 5
                elif move == "go down":
                    self.movement = 6
                elif move == "stop": # to break the loop
                    self.movement = 0 # special symbol for breaking the loop
        elif move == "light torch":
            print("You try to light the torch but realize you forgot a lighter.")
            move = input()
            if move == "go north":
                self.movement = 1
            elif move == "go east":
                self.movement = 2
            elif move == "go south":
                self.movement = 3
            elif move == "go west":
                self.movement = 4
            elif move == "go up":
                self.movement = 5
            elif move == "go down":
                self.movement = 6
            elif move == "stop": # to break the loop
                self.movement = 0 # special symbol for breaking the loop
        else:
            print("You realize you are spouting gibberish into thin air.")


if __name__ == "__main__":
    field = Place("cave", "river one", None, "forest one", None, None)
    field.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
    cave = Place(None, None, "field", None, "ledge", None)
    cave.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
    riverone = Place(None, None, None, "field", None, None)
    riverone.blurb = "The river is burbling happily. You can't see anything interesting but the field to the west."
    forestone = Place(None, "field", None, None, None, None)
    forestone.blurb = "The forest is peaceful but empty. You can't see anything interesting but the field to the east."
    ledge = Place(None, None, None, None, None, "cave")
    ledge.blurb = "The ledge is dark and empty. You can't see anything interesting but the cave below"
    player = Player()
    print("Movement commands are go + north/south/east/west/up/down. All lowercase please. To exit, type stop." + '\n')
    player.location = field # start in field but stay in while loop later
    field.description() # would also put inventory here later
    print(player.inventory)
    player.move_input()
    field.change_location(player)
    while True:
        if player.location == "cave":
            cave.description()
            #cave.dir_check()
            player.move_input()
            cave.change_location(player)
        elif player.location == "ledge":
            ledge.description()
            #ledge.dir_check()
            player.move_input()
            ledge.change_location(player)
        elif player.location == "river one":
            riverone.description()
            #riverone.dir_check()
            player.move_input()
            riverone.change_location(player)
        elif player.location == "forest one":
            forestone.description()
            #forestone.dir_check()
            player.move_input()
            forestone.change_location(player)
        elif player.location == "field":
            field.description()
            #field.dir_check()
            player.move_input()
            field.change_location(player)
        elif player.location == None:
            print("You realize you have been spouting gibberish into thin air.")
            player.location = field # reset to field
            field.description()
            player.move_input()
            field.change_location(player)
        elif player.location == "stop":
            break # because breaks can't be outside of loops
