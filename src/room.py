# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    e_to = None
    w_to = None
    n_to = None
    s_to = None
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
    
    def __str__(self):
        return '{}\n{}'.format(self.name, self.description)

    