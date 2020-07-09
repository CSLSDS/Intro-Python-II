# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room():

    def __init__(self, name, descr):
        # initialize name, description on instantiation
        self.name = name
        self.descr = descr

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.u_to = None
        self.d_to = None

    def __str__(self):
        output = f'{self.name}: '

        for text in textwrap.wrap(self.descr):
            output += '\n' + text
        
        output += f'\n\nchoose a direction (such as n, s, e, w)'

#        output += f'\n\nAvailable paths [{self.available_path()}]'

        return output
    
    # def available_path(self):
    #     path_list = []

    #     if self.n_to:
    #         path_list.append('n')
    #     if self.s_to:
    #         path_list.append('s')
    #     if self.e_to:
    #         path_list.append('e')
    #     if self.w_to:
    #         path_list.append('w')

    #     return ", ".join(path_list)