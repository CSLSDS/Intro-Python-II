import textwrap

class Room():
    def __init__(self, name, descr, inv):
        self.name = name
        self.descr = descr
        self.inv = inv

    def __str__(self):

        return f"{self.name}, {self.descr}; you see the following: {self.inv}"

        output = f'{self.name}: '

        for text in textwrap.wrap(self.descr):
            output += '\n' + text
        
        output += f'\n\nchoose a direction (such as n, s, e, w)'

        return output

    # roomventory = []
    # for name, info in inv.items():
    #     roomventory.append(name)
    def rem_item(self, item):
        return self.inv.remove(item)
    def get_item(self, item):
        return self.inv.append(item)