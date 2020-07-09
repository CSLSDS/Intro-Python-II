class Player():
    def __init__(self, location):
        self.location = location

    def try_dir(self, command):
        attribute = command + '_to'

        # see if current room has attribute
        # we can use py func 'hasattr'
        if hasattr(self.location, attribute):
            # use 'getattr' to actually move to the room
            self.location = getattr(self.location, attribute)
        else:
            print('you can\'t go there')