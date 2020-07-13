# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    e_to = None
    w_to = None
    n_to = None
    s_to = None
    items = []
    def __init__(self, name, desc, room_e = None, ):
        self.name = name
        self.description = desc
    
    def __str__(self):
        return '{}: {}'.format(self.name, self.description)

    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self, item):
        self.items.remove(item)

    