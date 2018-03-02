# The Queen's Quest

The Queen's Quest is a fantasy-themed, text-based adventure game. The player inputs text commands to travel around a world, picking up and using items on a quest to find the queen's lost crown. This game was developed for Jen S.'s Object Oriented Programming class at The Nueva School, Fall 2017.

## Getting Started

This game is short and contained within one file (adventure2.py). The rest of the files in this repository document the development process of the game.

### Prerequisites

The Queen's Quest is written in Python 3.6.4.

### Installation

To play The Queen's Quest, simply download the repository, open Terminal (or equivalent), and run adventure2.py in Python 3. If properly installed, on startup the program should print

```
Instructions:
Movement commands are go + north/south/east/west/up/down. All lowercase please. To exit, type stop.

You stand in a large field with a forest to the west, a river to the east, and a cave to the north. There is a bouquet of flowers lying at your feet.
```

Commands are case sensitive and if the input is invalid, the program will print

```
You realize you are spouting gibberish into thin air.
```

An example of valid movement

```
Instructions:
Movement commands are go + north/south/east/west/up/down. All lowercase please. To exit, type stop.

You stand in a large field with a forest to the west, a river to the east, and a cave to the north. There is a bouquet of flowers lying at your feet.
go west 
From the forest, the field stretches to the east and a hill rises to the north.
go north
You stand halfway up the majestic hill, looking over the forest to the south and east.
go east
To the north, a hill rises. To the south, a path runs through the forest. To the east, a clearing appears through the trees.
```

A full list of object interaction commands can be found in commands.txt. Commands are simple verb-object commands. For example, to pick up the torch,

```
You stand at the mouth of a dark cave. There is an unlit torch and an old scroll on the ground. It looks like you can climb to a ledge above.
pick up torch
You gingerly pick up the torch and wonder how it got there.
light torch
The warm light of the torch flickers over your surroundings.
```

If the command is a valid command (for example, light torch) but not executable at the time (the player has not picked up the torch), the program will ask

```
What torch?
```

To exit the program at any time, input

```
stop
```

Upon processing the stop command, the program will terminate.

### Further Notes

Testers have had trouble running this code on Windows 10, apparently due to an error with printing the \n character. Because of this, empty lines are printed using

```
print(" ")
```

To report further bugs or for further information about the design and development of this game, contact laumitt@nuevaschool.org.

## Acknowledgments

* Jen Selby (teacher, debugger, and playtester)
* Osher L (debugger)
* Bob Mitton (debugger and playtester)
