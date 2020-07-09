from room import Room
from player import Player
 
# Declare all the rooms

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

    'secret': Room("You have discovered Chelsea's Top-Secret Hideout!", """hey! what do you think \
you're doing here?? didn't that treasure room description say the only exit was SOUTH?? \
how did you even get IN here? do you even know the password??!""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].u_to = room['secret']
room['secret'].d_to = room['treasure']

#
# Main
#
name = input('WHAT... is your name? \n\n...')
# Make a new player object that is currently in the 'outside' room.
player = Player(name)
player.set_current_room(room['outside'])
print(f'\nwelcome to adventure, {player.name}!!')
player.print_descr()


# define plausible inputs
def valid_input(input):
    valid_inputs = ['n', 's', 'e', 'w', 'u', 'd']
    if input not in valid_inputs:
        return False
    return True
# define how stuff happens
def do_thing(input, player):
    
    if input == 'q':
        print('ok!')
        exit()
    else:
        if player.move(input): # case sensitivity?
            player.print_descr()
        else:
            print('I\'m sorry Dave; I\'m afraid I can\'t do that.\
                \n[that was invalid input... try again!]')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * valid commands are n s e w
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    user_input = input('\nyour choice: ')

    if not valid_input(user_input):
        print('invalid entry; reattmpt?')
        continue

    do_thing(user_input, player)
