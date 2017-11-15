import abc

class Place:
    __metaclass__ = abc.ABCMeta # never going to have an instance of just Place

    def __init__(self):
        self.north = None # you can't go north from nowhere
        self.east = None # all of these are individually declared instead of
        self.south = None # generated or read because the map won't change
        self.west = None # do i need to put self in front of these?
        self.up = None
        self.down = None
        self.ways = [self.north, self.east, # ways you can go from a place
                     self.south, self.west,
                     self.up, self.down]
        self.location = "none"
    def dir_check(self):
        print("You can go " +
              "\n" "North = " + str(self.north) +
              "\n" + "East = " + str(self.east) +
              "\n" + "South = " + str(self.south) +
              "\n" + "West = " + str(self.west) +
              "\n" + "Up = " + str(self.up) +
              "\n" + "Down = " + str(self.down))
    def description(self):
        self.blurb = "if you see this something broke"
        print(self.blurb)
    def move_input(self):
        go = input()
        ask = True
        while ask == True:
            if go == "go north" and self.north == True:
                self.movement = "move north"
            elif go == "go east" and self.east == True:
                self.movement = "move east"
            elif go == "go south" and self.south == True:
                self.movement = "move south"
            elif go == "go west" and self.west == True:
                self.movement = "move west"
            elif go == "go up" and self.up == True:
                self.movement = "move up"
            elif go == "go down" and self.down == True:
                self.movement = "move down"
            else:
                print("You can't go that way.")
            if self.movement == "move " + "north" or "east" or "south" or "west" or "up" or "down":
                print(self.movement)
                ask = False
        # how do i go through self.ways and figure out where i can go
        # without all this repetitive code?
    def change_location(self):
        if self.movement == "move north":
            self.location = "loc north"
        elif self.movement == "move east":
            self.location = "loc east"
        elif self.movement == "move south":
            self.location = "loc south"
        elif self.movement == "move west":
            self.location = "loc west"
        elif self.movement == "move up":
            self.location = "loc up"
        elif self.movement == "move down":
            self.location = "loc down"
        # how do i make this less repetitive? it's kind of all placeholder code
#    def enter_room(self): # is this a thing i can do?
#        dir_check(self)
#        description()
#        move_input(self)
#        change_location(self)

class Field(Place):
    def __init__(self): # all the locations should have their own directions
        self.north = True # and descriptions and movements
        self.east = True
        self.south = False
        self.west = True
        self.up = False
        self.down = False
        self.location = "field"
    def description(self): # each thing has its own description
        self.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
    def change_location(self):
        if self.movement == "north": # you can go north to the cave
            self.location = "cave"
        elif self.movement == "east": # you can go east to the river
            self.location = "river one"
        elif self.movement == "west": # you can go west to the forest
            self.location = "forest one"
        print(self.location)

class Cave(Place):
    def __init__(self): # all the locations should have their own directions
        self.north = False # and descriptions
        self.east = False
        self.south = True
        self.west = False
        self.up = True
        self.down = False
        self.location = "cave"
    def description(self): # each thing has its own description
        self.blurb = "You stand at the mouth of a dark cave. There is an unlit torch on the ground. It looks like you can climb to a ledge above."
    def change_location(self):
        if self.movement == "move south": # you can go back south to the field
            self.location = "field"
        elif self.movement == "move up": # you can climb up to the ledge
            self.location = "ledge"
        print(self.location)

if __name__ == "__main__":
    field = Field()
    cave = Cave()
    field.dir_check()
    field.description()
    field.move_input()
    field.change_location()
    if field.location == "cave":
        cave.dir_check()
        cave.description()
        cave.move_input()
        cave.change_location()
