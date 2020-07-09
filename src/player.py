# Write a class to hold player information, e.g. what room they are in
# currently.
 

from room import Room

class Player():

    def __init__(self, name):
        # initialize name on instantiation of class
        self.name = name
        # initialize room location
        self.current_room = None

    def set_current_room(self, room):
        # assign 'room' var as defined in ____
        self.current_room = room

    def return_current_room(self):
        return self.current_room

    def move(self, direction):
        current_room = self.return_current_room()

        # check if move is plausible
        if direction == 'n' and current_room.n_to:
            self.set_current_room(current_room.n_to)
            return True
        elif direction == 's' and current_room.s_to:
            self.set_current_room(current_room.s_to)
            return True
        elif direction == 'e' and current_room.e_to:
            self.set_current_room(current_room.e_to)
            return True
        elif direction == 'w' and current_room.w_to:
            self.set_current_room(current_room.w_to)
            return True
        elif direction == 'u' and current_room.u_to:
            self.set_current_room(current_room.u_to)
            return True
        elif direction == 'd' and current_room.d_to:
            self.set_current_room(current_room.d_to)
            return True            
        return False

    def print_descr(self):
        print(f'\n{self.return_current_room()}')