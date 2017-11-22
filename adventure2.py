class Place:
    def __init__(self, locnorth, loceast, locsouth, locwest, locup, locdown):
        self.NORTH = locnorth
        self.EAST = loceast
        self.SOUTH = locsouth
        self.WEST = locwest
        self.UP = locup
        self.DOWN = locdown
        self.location = None
        self.blurb = None
    def description(self):
        print(self.blurb)
    def dir_check(self):
        print("You can go " +
              "\n" + "North = " + str(self.NORTH) +
              "\n" + "East = " + str(self.EAST) +
              "\n" + "South = " + str(self.SOUTH) +
              "\n" + "West = " + str(self.WEST) +
              "\n" + "Up = " + str(self.UP) +
              "\n" + "Down = " + str(self.DOWN))
    def change_location(self, player):
        if player.movement == 1:
            player.location = self.NORTH
        elif player.movement == 2:
            player.location = self.EAST
        elif player.movement == 3:
            player.location = self.SOUTH
        elif player.movement == 4:
            player.location = self.WEST
        elif player.movement == 5:
            player.location = self.UP
        elif player.movement == 6:
            player.location = self.DOWN
        print(player.location)

class Player:
    def __init__(self):
        self.movement = None
        self.location = None
    def move_input(self):
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
        else:
            print("You can't go that way.")

if __name__ == "__main__":
    game = True
    field = Place("cave", "river one", None, "forest one", None, None)
    field.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
    cave = Place(None, None, "field", None, "ledge", None)
    cave.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
    riverone = Place(None, None, None, "field", None, None)
    riverone.blurb = "nonexistent"
    forestone = Place(None, "field", None, None, None, None)
    forestone.blurb = "nope"
    ledge = Place(None, None, None, None, None, "cave")
    ledge.blurb = "no existe"
    player = Player()
    player.location = field
    while game == True:
        field.description()
        field.dir_check()
        player.move_input()
        field.change_location(player)
        if player.location == "cave":
            cave.description()
            cave.dir_check()
            player.move_input()
            cave.change_location(player)
        elif player.location == "river one":
            riverone.description()
            riverone.dir_check()
            player.move_input()
            riverone.change_location(player)
        elif player.location == "forest one":
            forestone.description()
            forestone.dir_check()
            player.move_input()
            forestone.change_location(player)
        elif player.location == "field":
            field.description()
            field.dir_check()
            player.move_input()
            field.change_location(player)
