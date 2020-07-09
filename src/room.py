import textwrap

class Room():
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def __str__(self):
        return f"{self.name}, {self.descr}"