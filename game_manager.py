import random
from disk import Disk
WHITE = 255
BLACK = 0
SPACING = 100
LOCATION = 50
DIAMATER = 90
TEXT_COLOR = (178, 34, 34)
TEXT_SIZE_BIG = 50


class GameManager:
    ## probrably change the name to "player", "move_manager"
    '''alternates between white and black tiles'''

    def __init__(self, board):
        self.turn = True
        self.board = board
        self.no_ai_moves = False
        self.no_player_moves = False
        # 8 directions to find legal moves
        self.directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1),
                           (-1, 0), (-1, 1)]
        self.legal_move = dict()  # a dictionary to store all legal moves
        print("Player's turn")  # prompt the human player to play

    def player_make_move(self, x, y):
        self.legal_move = dict()  # reset the dictionary in every turn

        # get the x and y coordinates from the mouse click
        x = x//self.board.SPACING
        y = y//self.board.SPACING

        # find legal moves
        for i in range(len(self.board.spaces)):
            for item in self.board.spaces[i]:
                if item and item.color == BLACK:
                    self.find_moves(item, WHITE)

        # check if there is any legal move for the player.
        # if none, pass it to the AI.
        ## better to relocate these methods in game controller
        if not self.legal_move:
            self.turn = not self.turn
            self.no_player_moves = True
            self.turn_display("Computer's turn")
            return
        # update the player's move when every requirement is met.
        if (x, y) in self.legal_move and not self.board.spaces[x][y]:
            disk = Disk(BLACK, SPACING, DIAMATER, LOCATION, x, y)
            self.board.spaces[x][y] = disk
            disks_to_flip = self.legal_move[(x, y)]
            self.flip(disks_to_flip, BLACK)

            self.turn = not self.turn  # pass it to AI
            self.turn_display("Computer's turn")  # display that it's AI's turn

    def ai_make_move(self):
        self.legal_move = dict()  # reset the dictionary in every turn

        # find all the legal moves
        for i in range(len(self.board.spaces)):
            for item in self.board.spaces[i]:
                if item and item.color == WHITE:
                    self.find_moves(item, BLACK)

        # check if there are any legal moves for the AI.
        # if not, switch back to human player.
        if not self.legal_move:
            self.no_ai_moves = True
            self.turn = not self.turn
            self.turn_display("Player's turn")
            return
        # let the AI choose the "smartest" move
        ai_move = self.smart_ai(self.legal_move)

        # update the move: create the disk and flip the flippable steps
        disk = Disk(WHITE, SPACING, DIAMATER, LOCATION, ai_move[0],
                    ai_move[1])
        self.board.spaces[ai_move[0]][ai_move[1]] = disk
        disks_to_flip = self.legal_move[ai_move]
        self.flip(disks_to_flip, WHITE)

        self.turn = not self.turn  # pass it to human player
        self.turn_display("Player's turn")  # display it's player's turn

    def find_moves(self, item, opposite_color):
        '''determine legal moves for a single tile'''
        for dir in self.directions:
            # make one step in the direction
            x = item.x + dir[0]
            y = item.y + dir[1]
            flippable = False

            # check if (x, y) is within the range of board, and if there is
            # a disk in (x, y) whose color is the opposite of the playing color
            while (self.on_board((x, y)) and
                    self.board.spaces[x][y] and
                    self.board.spaces[x][y].color == opposite_color):
                # make step(s) until (x, y) doesn't meet the requirements.
                x += dir[0]
                y += dir[1]
                # We get a legal move (x, y), and can turn the boolean variable
                # to true.
                if not flippable:
                    flippable = True

            if flippable:
                # find and store flippable disks into the dictionary
                if self.on_board((x, y)) and not self.board.spaces[x][y]:
                    flip_x = x - dir[0]
                    flip_y = y - dir[1]
                    if (x, y) not in self.legal_move:
                        self.legal_move[(x, y)] = [(flip_x, flip_y)]
                    else:
                        self.legal_move[(x, y)].append((flip_x, flip_y))
                    while flip_x != item.x + dir[0] or \
                            flip_y != item.y + dir[1]:
                        flip_x -= dir[0]
                        flip_y -= dir[1]
                        self.legal_move[(x, y)].append((flip_x, flip_y))

    def turn_display(self, message):
        '''display whose turn it is to the terminal'''
        print(message)

    def on_board(self, item):
        '''determines if a disk is on board'''
        return item[0] >= 0 and item[0] <= self.board.COLUMNS - 1 and \
            item[1] >= 0 and item[1] <= self.board.ROWS - 1

    def flip(self, items, color):
        '''change the color of the disk to flip'''
        for item in items:
            self.board.spaces[item[0]][item[1]].color = color

    ## probrably a separate class if I work on a sophisticated AI
    def smart_ai(self, items):
        '''let the AI choose the legal move that will flip most disks'''
        max_flip_steps = 0
        smart_ai_move = (0, 0)
        for item in items:
            if len(items[item]) > max_flip_steps:
                max_flip_steps = len(items[item])
                smart_ai_move = item
        return smart_ai_move

## can break the methods furthur down and put some of them in disks or board