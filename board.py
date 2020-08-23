from disk import Disk

BLACK = 0
WHITE = 255
STROKE_WEIGHT = 1.5
SPACING = 100
LOCATION = 50
DIAMATER = 90


class Board:
    '''draw the board and keep track of available spaces'''
    def __init__(self, rows, columns, spacing):
        self.ROWS = rows
        self.COLUMNS = columns
        self.SPACING = spacing
        self.spaces = [[None for x in range(self.ROWS)] for y in
                       range(self.COLUMNS)]

        # the initial four tiles
        i = int(self.COLUMNS / 2)
        j = int(self.ROWS / 2)
        disk_1 = Disk(WHITE, SPACING, DIAMATER, LOCATION, i, j)
        disk_2 = Disk(WHITE, SPACING, DIAMATER, LOCATION, i-1, j-1)
        disk_3 = Disk(BLACK, SPACING, DIAMATER, LOCATION, i, j-1)
        disk_4 = Disk(BLACK, SPACING, DIAMATER, LOCATION, i-1, j)
        self.spaces[i][j] = disk_1
        self.spaces[i-1][j-1] = disk_2
        self.spaces[i][j-1] = disk_3
        self.spaces[i-1][j] = disk_4
        ## redundant location information. only the board needs it

    def display(self):
        '''display the board as well as the four starter tiles'''
        stroke(BLACK)
        strokeWeight(STROKE_WEIGHT)
        # draw the horizontal lines
        for i in range(self.ROWS):
            line(0, i * self.SPACING, self.ROWS * self.SPACING,
                 i * self.SPACING)
        # draw the vertical lines
        for i in range(self.COLUMNS):
            line(i * self.SPACING, 0, i * self.SPACING,
                 self.COLUMNS * self.SPACING)

        # display all the disks on the board
        for i in range(len(self.spaces)):
            for disk in self.spaces[i]:
                if disk:
                    disk.display()
