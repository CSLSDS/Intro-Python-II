from room0 import Room
from player0 import Player

room = {
    'outside':  Room("You find yourself Outside Cave Entrance",
                     "North of you, the cave mount beckons beckoningly"),

    'foyer':    Room("You find yourself in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("You find yourself at a Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("You find yourself in a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("You find yourself in the Treasure Chamber!", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by 
earlier adventurers; an open, empty chest stands on a platform at the end of the room.
There are vines growing up through cracks in the walls, continuing through a sizeable hole
in the crumbling stone ceiling. The only exit is to the south."""),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(room['outside'])

valid_dir = ['n', 's', 'e', 'w']

while True:
    # sanitize input (whitespace, case, split)
    print(f'{player.location}\n')
    command = input('whatchu wanna do? ').strip().lower().split()
    command = command[0]
    if command == 'q':
        exit()

    if command in valid_dir:
        # check
        # go there
        player.try_dir(command)