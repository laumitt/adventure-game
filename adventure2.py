# to do list
# playtest
# rewrite descriptions

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
    def get_location(self, current, movement):
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
            if current == "forest path":
                return "forest path"
            elif current == "cave":
                return "lit ledge"
            elif current == "canyon":
                return "rainbow"
            elif current == "ledge":
                return "lit ledge"

class Inventory:
    def __init__(self):
        self.have = []
        self.check = None
    def inventory_add(self, item):
        self.have.append(item)
    def inventory_check(self, item):
        if self.have.count(item) >= 1:
            self.check = True

class Actions:
    def get_torch(self, current, inventory):
        print(current)
        if current == "cave":
            inventory.inventory_add("torch")
            print("You gingerly pick up the torch and wonder how it got there.")
        else:
            print("What torch?")
    def light_torch(self, current, inventory):
        inventory.inventory_check("torch")
        if inventory.check == True:
            print("The warm light of the torch flickers over your surroundings.")
            player.torchlit = True
        else:
            print("What torch?")
    def drop_torch(self, current, inventory):
        inventory.inventory_check("torch")
        if inventory.check == True:
            print("The torch clatters to the ground.")
        else:
            print("What torch?")
    def get_rock(self, current, inventory):
        if current == "ford":
            inventory.inventory_add("rock")
            print("You turn the smooth, shiny rock over in your hand.")
        else:
            print("What rock?")
    def look_rock(self, current, inventory):
        inventory.inventory_check("rock")
        if inventory.check == True:
            print("You look as hard as you can but can't see anything special about the rock.")
        else:
            print("What rock?")
    def drop_rock(self, current, inventory):
        inventory.inventory_check("rock")
        if inventory.check == True:
            print("The rock thuds to the ground.")
        else:
            print("What rock?")
    def move_leaves(self, current, inventory):
        if current == "clearing one":
            print("You kick the leaves aside to find a rusty old key.")
        else:
            print("What leaves?")
    def get_key(self, current, inventory):
        if current == "clearing one":
            inventory.inventory_add("key")
            print("You slip the key into your pocket.")
        else:
            print("What key?")
    def drop_key(self, current, inventory):
        inventory.inventory_check("key")
        if inventory.check == True:
            print("A bit of rust flutters off the key as it falls.")
        else:
            print("What key?")
    def unlock(self, current, inventory):
        if current == "forest path":
            inventory.inventory_check("key")
            if inventory.check == True:
                print("The gate swings open on rusty hinges, allowing you to climb the tree.")
                player.gateopen = True
            else:
                print("You don't have a key.")
        else:
            print("What gate?")
    def get_crown(self, current, inventory):
        if current == "up tree":
            inventory.inventory_add("crown")
            print("You admire the sparkling facets of the crown and wear it or something.")
        else:
            print("What crown?")
    def drop_crown(self, current, inventory):
        inventory.inventory_check("crown")
        if inventory.check == True:
            print("The crown sparkles as it falls.")
        else:
            print("What crown?")
    def present_crown(self, current, inventory):
        inventory.inventory_check("crown")
        if inventory.check == True:
            print("The queen smiles or something.")
        else:
            print("What crown?")
    def get_sword(self, current, inventory):
        if current == "lit ledge":
            inventory.inventory_add("sword")
            print("The sword gleams in the torchlight as you pick it up.")
        else:
            print("What sword?")
    def drop_sword(self, current, inventory):
        inventory.inventory_check("sword")
        if inventory.check == True:
            print("The sword falls with a crash.")
        else:
            print("What sword?")
    def get_scroll(self, current, inventory):
        if current == "cave":
            inventory.inventory_add("scroll")
            print("You gently pick up the old parchment.")
        else:
            print("What scroll?")
    def read_scroll(self, current, inventory):
        inventory.inventory_check("scroll")
        if inventory.check == True:
            print("scroll.")
        else:
            print("What scroll?")
    def drop_scroll(self, current, inventory):
        inventory.inventory_check("scroll")
        if inventory.check == True:
            print("The scroll flutters to the ground.")
        else:
            print("What scroll?")
    def hit_troll(self, current, inventory):
        if current == "forest four":
            inventory.inventory_check("sword")
            if inventory.check == True:
                print("hit troll.")
            else:
                print("What troll?")
    def get_gem(self, current, inventory):
        if current == "forest six":
            inventory.inventory_add("gem")
            print("You admire the sparkling facets of the gem and take it.")
        else:
            print("What gem?")
    def drop_gem(self, current, inventory):
        inventory.inventory_check("gem")
        if inventory.check == True:
            print("The gem sparkles as it falls.")
        else:
            print("What gem?")
    def get_flowers(self, current, inventory):
        if current == "field":
            inventory.inventory_add("flowers")
            print("You admire the bouquet.")
        else:
            print("What flowers?")
    def drop_flowers(self, current, inventory):
        inventory.inventory_check("flowers")
        if inventory.check == True:
            print("The flowers fall.")
        else:
            print("What flowers?")
    def present_flowers(self, current, inventory):
        inventory.inventory_check("flowers")
        if inventory.check == True:
            print("The queen is happy.")
        else:
            print("What flowers?")

class Player:
    def __init__(self, actions, current, inventory):
    # where they want to go and where they are
    # object status also stored here
        self.movement = None
        self.location = None
        self.gateopen = False
        self.torchlit = False
        self.magical = False
        self.moves = {"go north" : 1,
                        "go east" : 2,
                        "go south" : 3,
                        "go west" : 4,
                        "go up" : 5,
                        "go down" : 6,
                        "stop" : "stop"}
        # dictionary of non-movement actions linked to methods in Actions
        # light torch is special and different
        self.action_list = {"pick up torch" : lambda current:actions.get_torch(current, inventory),
                            "drop torch" : lambda current:actions.drop_torch(current, inventory),
                            "pick up rock" : lambda current:actions.get_rock(current, inventory),
                            "inspect rock" : lambda current:actions.look_rock(current, inventory),
                            "drop rock" : lambda current:actions.drop_rock(current, inventory),
                            "move leaves" : lambda current:actions.move_leaves(current, inventory),
                            "pick up key" : lambda current:actions.get_key(current, inventory),
                            "drop key" : lambda current:actions.drop_key(current, inventory),
                            "unlock gate" : lambda current:actions.unlock(current, inventory),
                            "pick up crown" : lambda current:actions.get_crown(current, inventory),
                            "present crown" : lambda current:actions.present_crown(current, inventory),
                            "pick up sword" : lambda current:actions.get_sword(current, inventory),
                            "drop sword" : lambda current:actions.drop_sword(current, inventory),
                            "pick up scroll" : lambda current:actions.get_scroll(current, inventory),
                            "read scroll" : lambda current:actions.read_scroll(current, inventory),
                            "drop scroll" : lambda current:actions.drop_scroll(current, inventory),
                            "hit troll" : lambda current:actions.hit_troll(current, inventory),
                            "pick up gem" : lambda current:actions.get_gem(current, inventory),
                            "drop gem" : lambda current:actions.drop_gem(current, inventory),
                            "pick up flowers" : lambda current:actions.get_flowers(current, inventory),
                            "present flowers" : lambda current:actions.present_flowers(current, inventory),
                            "drop flowers" : lambda current:actions.drop_flowers(current, inventory)}
    def action_input(self, current, actions, inventory):
    # Player knows where to move but doesn't know where that movement will take them
        while True:
            action = input()
            if str(action) in ["go north", "go east", "go south", "go west", "go up", "go down"]:
                self.movement = self.moves[action]
                if action == "go up":
                    if current == "forest path":
                        if self.gateopen == True:
                            self.movement = 5
                            break
                        else:
                            print("The gate isn't open yet.")
                            self.movement = 9
                            break
                    elif current == "cave":
                        if self.torchlit == True:
                            self.movement = 9
                            break
                        else:
                            self.movement = 5
                            break
                    else:
                        break
                elif action == "go west":
                    if current == "canyon":
                        if self.magical == True:
                            self.movement = 9
                            break
                        else:
                            break
                    else:
                        break
                else:
                    break
            elif str(action) in self.action_list:
                self.action_list[action](current)
            elif str(action) == "light torch":
                if current == "ledge":
                    self.movement = 9
                    break
                else:
                    actions.light_torch(current, inventory)
            elif str(action) == "xyzzy":
                if current == "hill":
                    self.magical = True
                    print("You begin to glow faintly with a magical aura.")
                else:
                    print("A hollow voice says 'Cretin'")
            elif str(action) == "stop": # to break the loop
                self.movement = "stop"
                break
            else: # if they make a typo or say something else
                print("You realize you are spouting gibberish into thin air.")
    def change_location(self, location):
    # set location to what Place said
        self.location = location

if __name__ == "__main__":
    current = None
    actions = Actions()
    inventory = Inventory()
    player = Player(actions, current, inventory)
    # initiation (map location) of locations and descriptions
    field = Place("cave", "river one", None, "forest one", None, None, player)
    field.blurb = "You stand in a large field with a forest to the west, a river to the east, and a cave to the north."
    cave = Place(None, None, "field", None, "ledge", None, player)
    cave.blurb = "You stand at the mouth of a dark cave. There is an unlit torch and an old scroll on the ground. It looks like you can climb to a ledge above."
    riverone = Place(None, None, "ford", "field", None, None, player)
    riverone.blurb = "You stand next to a river burbling south to a ford along the field to the west."
    forestone = Place("hill", "field", None, None, None, None, player)
    forestone.blurb = "From the forest, the field stretches to the east and a hill rises to the north."
    ledge = Place(None, None, None, None, None, "cave", player)
    ledge.blurb = "The ledge is dark and empty. Only a little light shines up from the cave below."
    ford = Place("river one", "forest two", "river two", None, None, None, player)
    ford.blurb = "You stand at a ford, with river burbling to the north and south and forest to the east. There is a shiny rock on the ground."
    foresttwo = Place("forest path", "clearing one", "clearing one", "ford", None, None, player)
    foresttwo.blurb = "A path runs through the forest to the north, a clearing opens to the south and east, and the river runs over the ford to the west."
    clearingone = Place("forest two", None, None, "forest two", None, None, player)
    clearingone.blurb = "The clearing is empty except a pile of leaves on the ground. Forest stretches to the north and west."
    forestpath = Place("forest three", None, "forest two", None, "up tree", None, player)
    forestpath.blurb = "Forest surrounds the path to the north and south. A high fence surrounds a tree that it looks like you could climb up."
    uptree = Place(None, None, None, None, None, "forest path", player)
    uptree.blurb = "You find a beautiful view and a beautiful crown. The branches form a perfect ladder down to the path."
    rivertwo = Place("ford", None, "cliff", None, None, None, player)
    rivertwo.blurb = "To the south, the river runs over an impassable waterfall. The ford crosses to the north."
    hill = Place(None, None, "forest one", "forest three", None, None, player)
    hill.blurb = "You stand halfway up the majestic hill, looking over the forest to the south and west."
    forestthree = Place("hill", "clearing two", "forest path", None, None, None, player)
    forestthree.blurb = "To the north, a hill rises. To the south, a path runs through the forest."
    litledge = Place(None, None, None, None, None, "cave", player)
    litledge.blurb = "The torch shines around the ledge, revealing a gleaming antique sword."
    cliff = Place(None, None, None, None, "river two", "canyon", player)
    cliff.blurb = "cliff."
    canyon = Place(None, None, None, None, "cliff", None, player)
    canyon.blurb = "canyon."
    rainbow = Place(None, "canyon", None, None, None, None, player)
    rainbow.blurb = "rainbow."
    clearingtwo = Place(None, "forest five", "forest four", "forest three", None, None, player)
    clearingtwo.blurb = "clearing two."
    forestfour = Place("clearing two", None, "forest six", None, None, "cave", player)
    forestfour.blurb = "forest four."
    forestfive = Place("castle", None, None, "clearing two", None, None, player)
    forestfive.blurb = "forest five."
    forestsix = Place("forest four", None, None, None, None, None, player)
    forestsix.blurb = "forest six."
    castle = Place(None, None, "forest five", None, None, None, player)
    castle.blurb = "castle."
    # dictionary of locations and objects
    locs = {"field" : field,
            "cave" : cave,
            "river one" : riverone,
            "forest one" : forestone,
            "ledge" : ledge,
            "ford" : ford,
            "forest two" : foresttwo,
            "clearing one" : clearingone,
            "forest path" : forestpath,
            "up tree" : uptree,
            "river two" : rivertwo,
            "hill" : hill,
            "forest three" : forestthree,
            "lit ledge" : litledge,
            "cliff" : cliff,
            "canyon" : canyon,
            "rainbow" : rainbow,
            "clearing two" : clearingtwo,
            "forest four" : forestfour,
            "forest five" : forestfive,
            "forest six" : forestsix,
            "castle" : castle}
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
            player.action_input(current, actions, inventory)
            player.change_location(locs[current].get_location(current, player.movement))
            if player.location == None: # if they go somewhere they can't
                print("You stumble into an invisible wall and realize you can't go that way.")
