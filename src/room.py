import textwrap

class Room():
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def __str__(self):

        return f"{self.name}, {self.descr}"

        output = f'{self.name}: '

        for text in textwrap.wrap(self.descr):
            output += '\n' + text
        
        output += f'\n\nchoose a direction (such as n, s, e, w)'

        return output
    

