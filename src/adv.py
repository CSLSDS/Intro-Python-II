from room import Room
from player import Player
from item import Item
import sys

item = {
    'slinky': Item('slinky', 'an old rusty slinky with tangles'),
    'feather': Item('feather', 'a small gray feather'),
    'dust': Item('dust', 'just some dust'),
    'watch': Item('watch', 'a timex indiglo watch'),
    'amulet': Item('amulet', 'a sparkling amulet'), # taking this item teleports player across chasm
    'return': Item('amulet', 'a sparkling amulet')  # taking this item teleports player back to overlook
}

room = {
    'outside':  Room("You find yourself Outside Cave Entrance",
                     "North of you, the cave mouth beckons beckoningly", [item['slinky'].name]),

    'foyer':    Room("You find yourself in the Foyer", """Dim light filters in from the south. Dusty\
passages run north and east.""", [item['feather'].name]),

    'overlook': Room("You find yourself at a Grand Overlook", """A steep cliff appears before you, falling\
into the darkness. Ahead to the north, a light flickers in\
the distance, but there is no way across the chasm.""", [item['amulet'].name]),

    'across': Room('You find yourself across the chasm!', """Somehow, you are suddenly looking at a flickering\
torch next to a collapsed cave entrance, and when you turn around, you can see the cliff you were\
just standing on in the distance.""", [item['return'].name]),

    'narrow':   Room("You find yourself in a Narrow Passage", """The narrow passage bends here from west\
to north. The smell of gold permeates the air.""", [item['dust'].name]),

    'treasure': Room("You find yourself in the Treasure Chamber!", """You've found the long-lost treasure\
chamber! Sadly, it has already been completely emptied by\
earlier adventurers; an open, empty chest stands on a platform at the end of the room.\
There are vines growing up through cracks in the walls, continuing through a sizeable hole\
in the crumbling stone ceiling. The only exit is to the south.""", [item['watch'].name]),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].t_to = room['across']
#room['overlook'].n_to = room['outside'] kill player for walking off cliff; respawn outside
room['across'].t_to = room['overlook']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(room['outside'])

valid_dir = ['n', 's', 'e', 'w', 't']
item_action = ['get', 'drop']

while True:
    # orient player
    print(f'{player.location}\n')
    # sanitize input (whitespace, case, split)
    command = input('whatchu wanna do? ').strip().lower().split()
    if len(command) > 1:
        current_room = player.location
        item_names = []
        for var, info in item.items():
            item_names.append(info.name)
        if command[0] in item_action and command[1] in item_names:
            if command[1] == 'amulet':
                player.try_dir('t')
            elif command[0] == 'get':
                player.get_item(command[1])
                current_room.rem_item(command[1])
            elif command[0] == 'drop':
                player.rem_item(command[1])
                current_room.get_item(command[1])
        else:
            print("?")

    if command[0] == 'q':
        exit()

    elif command[0] in valid_dir:
        player.try_dir(command[0])
    
    # check validity of item_action, and availability of item
    # elif command[0] in item_action and command[1] in available_items:
    #     if command[1] == 'amulet':
    #         player.try_dir(t)
    #     elif command[0] == 'get':
    #         player.get_item(command[1])
    #         room.rem_item(command[1])
    #     elif command[0] == 'drop':
    #         player.rem_item(command[1])
    #         room.get_item(command[1])