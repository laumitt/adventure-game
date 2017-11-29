import abc

class Place:
#    __metaclass__ = abc.ABCMeta # never going to have an instance of just Place
    def __init__(self, locnorth, loceast, locsouth, locwest, locup, locdown):
        self.NORTH = locnorth # you can't go north from nowhere
        self.EAST = loceast # all of these are individually declared instead of
        self.SOUTH = locsouth # generated or read because the map won't change
        self.WEST = locwest # do i need to put self in front of these?
        self.UP = locup
        self.DOWN = locdown
        self.location = None
        self.movement = None
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
    def move_input(self):
        go = input()
        if go == "go north" and self.NORTH is not None:
            self.movement = "move north"
        elif go == "go east" and self.EAST is not None:
            self.movement = "move east"
        elif go == "go south" and self.SOUTH is not None:
            self.movement = "move south"
        elif go == "go west" and self.WEST is not None:
            self.movement = "move west"
        elif go == "go up" and self.UP is not None:
            self.movement = "move up"
        elif go == "go down" and self.DOWN is not None:
            self.movement = "move down"
        else:
            print("You can't go that way.")
        if self.movement == "move " + "north" or "east" or "south" or "west" or "up" or "down":
            print(self.movement)
        # how do i go through self.ways and figure out where i can go
        # without all this repetitive code?
    def change_location(self):
        if self.movement == "move north":
            self.location = self.NORTH
        elif self.movement == "move east":
            self.location = self.EAST
        elif self.movement == "move south":
            self.location = self.SOUTH
        elif self.movement == "move west":
            self.location = self.WEST
        elif self.movement == "move up":
            self.location = self.UP
        elif self.movement == "move down":
            self.location = self.DOWN
        print(self.location)
        # how do i make this less repetitive? it's kind of all placeholder code
        # does it even need to exist?
#    def enter_room(self): # is this a thing i can do?
#        dir_check(self)
#        description(self)
#        move_input(self)
#        change_location(self)
#        this doesn't work when i run it

# class Field(Place):
#    def __init__(self): # all the locations should have their own directions
#        self.north = True # and descriptions and movements
#        self.east = True
#        self.south = False
#        self.west = True
#        self.up = False
#        self.down = False
#        self.location = "field"
#    @staticmethod
#    def description(): # each thing has its own description
#        print("You stand in a large field with a forest to the west, a river to the east, and a cave to the north.")
#    def change_location(self):
#        if self.movement == "move north": # you can go north to the cave
#            self.location = "cave"
#        elif self.movement == "move east": # you can go east to the river
#            self.location = "river one"
#        elif self.movement == "move west": # you can go west to the forest
#            self.location = "forest one"
#        print(self.location)

# class Cave(Place):
#    def __init__(self): # all the locations should have their own directions
#        self.north = False # and descriptions
#        self.east = False
#        self.south = True
#        self.west = False
#        self.up = True
#        self.down = False
#        self.location = "cave"
#        self.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
#    def description(self): # each thing has its own description
#        print(self.blurb)
#    def change_location(self):
#        if self.movement == "move south": # you can go back south to the field
#            self.location = "field"
#        elif self.movement == "move up": # you can climb up to the ledge
#            self.location = "ledge"
#        print(self.location)

if __name__ == "__main__":
    game = True
    field = Place("cave", "river one", None, "forest one", None, None)
    cave = Place(None, None, "field", None, "ledge", None)
#    field.NORTH = True
#    field.EAST = True
#    field.WEST = True
    field.location = "field"
    field.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
#    cave.SOUTH = True
#    cave.UP = True
    cave.location = "cave"
    cave.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
    if cave.movement == "move south": # you can go south to the field
        cave.location = "field"
    elif cave.movement == "move up": # you can climb up to the ledge
        cave.location = "ledge"
    field.dir_check() # debug only
    field.description()
    field.move_input()
    while game == True:
        if field.movement == "move north": # you can go north to the cave
            field.location = "cave"
        elif field.movement == "move east": # you can go east to the river
            field.location = "river one"
        elif field.movement == "move west": # you can go west to the forest
            field.location = "forest one"
        if cave.movement == "move south": # you can go south to the field
            cave.location = "field"
        elif cave.movement == "move up": # you can climb up to the ledge
            cave.location = "ledge"
        print("field.location is " + str(field.location))
        if field.location == "cave":
            cave.dir_check() # debug only
            cave.description()
            cave.move_input()
            cave.change_location()
        if field.location == "river one":
            print("haven't made the river yet")
            break
        if field.location == "forest one":
            print("haven't made the forest yet")
            break
        if cave.location == "field":
            field.dir_check() # debug only
            field.description()
            field.move_input()
            field.change_location()
        if cave.location == "ledge":
            print("haven't made the ledge yet")
            break
