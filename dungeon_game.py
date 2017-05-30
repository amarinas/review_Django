import random

#draw the grid
#random location for player
#pick random location for door
#pick random location for the monster
#draw player in grid
#take input for movement
#move player, unless invalid move(wall)
#win/lose check
#clear screen and redraw grid

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1, 1), (2,1), (3,1), (4,1),
         (0,2), (1, 2), (2,2), (3,2), (4,2),
         (0,3), (1, 3), (2,3), (3,3), (4,3),
         (0,4), (1, 4), (2,4), (3,4), (4,4),

]

def get_locations():
    monster = None
    door = None
    player = None

    return monster, door, player

def move_player(player, move):
    #get the players location#
    #left, x-1
    #right, x +1
    #up, y-1
    #down, y+1
    return player

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'DOWN', 'UP']
    #if y == 0, cant go up
     #if y == 4, cant go DOWN
     #if x == 0, cant go LEFT
     #if x == 4, cant go RIGHT
    return moves


while True:
    print("Welcome to the dungeon!!")
    print("You're currently in room {}") # position of player
    print("You can move {}") #moves available
    print ("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    #good move = change the player postition
    #bad move = dont change
    #on the door? win
    #on the monster the lose
    #if not loop back around
