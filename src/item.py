class Item():
    def __init__(self, name, descr):
        # initialize name, descr on instantiation
        self.name = name
        self.descr = descr

    def __str__(self):
        return f'{self.name}, {self.descr}'