from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# list of items
itemList = {
    'Brick': Item('Brick', 'Build settlement and roads'),
    'Wood': Item('Wood', 'Build settlement and roads'),
    'Sheep': Item('Sheep', 'Build settlement and get development cards'),
    'Grain': Item('Grain', 'Build settlement, cities and get development cards'),
    'Stone': Item('Stone', 'Build cities and get development cards'),
    'DCard': Item('Development Cards', 'Get special powers')
}

# items assignment to rooms
room['outside'].items = [itemList['Brick'], itemList['Wood']]
room['foyer'].items = [itemList['Brick'], itemList['Grain'], itemList['Sheep']]
room['overlook'].items = [itemList['Wood'], itemList['Sheep'], itemList['Grain']]
room['narrow'].items = [itemList['Stone'], itemList['Grain']]
room['treasure'].items = [itemList['Brick'], itemList['Grain'], itemList['Wood']]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Get Player Name
playerName = input('Hello, What is your name?\n')

# Initialize player with given name
player = Player(playerName, room['outside'])

while True:
    print('--------------------------------------------------')
    # print player item inventory
    print('\nPlayer Items:')
    for item in player.items:
        print('\t', item)
    print('\n')
    
    # print current room and items available in the room
    print('Room - ', player.current_room)
    print('\nItems in Room:')
    for item in player.current_room.items:
        print('\t', item)

    print('\n')
    print('--------------------------------------------------')
    # Get the User Input
    userInput = input('\nWhat would you like to do? \n\tEnter [n], [s], [e] or [w] to move across rooms \n\tEnter \"take [item_name]\" or \"drop [item_name]\" to add or remove items \n\tEnter [q] to quit the game\n')

    userInputWords = userInput.split(' ')

    if userInput == 'q':
        print('You chose to quit!')
        break
    elif len(userInputWords) == 1:
        player.move(userInput)
    elif len(userInputWords) == 2:
        verb = userInputWords[0]
        itemName = userInputWords[1]
        if itemName in itemList:
            player.action(verb, itemList[itemName])
        else:
            print('Invalid item choice')

