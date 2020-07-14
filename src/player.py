# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    items = []
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
    
    def __str__(self):
        return 'Name: {}, Current Room: {}'.format(self.name, self.current_room.name)

    def addItem(self, item):
        self.items.append(item)
        print('{} added to the inventory'.format(item.name))
    
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            print('{} removed from the inventory'.format(item.name))
        else:
            print('Item not available to', self.name)
    
    def move(self, move):
        moveVar = move + '_to'
        if getattr(self.current_room, moveVar) != None:
            print('Moving to ', move)
            self.current_room = getattr(self.current_room, moveVar)
        else:
            print('Movement not allowed!')
    
    def action(self, verb, item):
        if (verb == 'get' or verb == 'take') and (item in self.current_room.items):
            item.on_take()
            self.addItem(item)
            self.current_room.removeItem(item)
        elif (verb == 'drop' or verb == 'leave') and (item in self.items):
            item.on_drop()
            self.removeItem(item)
            self.current_room.addItem(item)
        else:
            print('Invalid item/action')
            return None